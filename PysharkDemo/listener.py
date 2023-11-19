import pyshark
import argparse
import json

from dbconn import conn


def main():
    parser = argparse.ArgumentParser(description='network interface listener')
    parser.add_argument('-i', '--interface', help='interface name', required=True)
    parser.add_argument('-f', '--filter', help='bpf filter', default='')
    args = parser.parse_args()
    interface = args.interface
    bpf_filter = args.filter
    capture = pyshark.LiveCapture(interface=interface, bpf_filter=bpf_filter)
    print("listening on eth interface: " + interface)
    with open(f'{interface}.txt', 'w') as file:
        for packet in capture.sniff_continuously():
            # print(packet.sniff_time)
            # print(packet.layers)
            if 'http' in packet:
                src_addr = packet.ip.src
                dst_addr = packet.ip.dst
                time = packet.sniff_time
                top_layer = str(packet.layers[-1].layer_name)
                sql_cursor = conn.cursor()
                sql = ("INSERT INTO xhcms (timestamp, top_layer, src_ip, dst_ip, http_header, http_data) "
                       "VALUES (%s, %s, %s, %s, %s, %s)")
                http_header = {}
                for field in packet.http.field_names:
                    # print(f"{field}: {packet.http.get(field)}")
                    http_header[field] = packet.http.get(field)
                http_data = {}
                if packet[-1] != packet.http:
                    if packet[-1].layer_name == 'data-text-lines':
                        http_data = str(packet[-1])
                    else:
                        for field in packet[-1].field_names:
                            # print(f"{field}: {packet[-1].get(field)}")
                            http_data[field] = packet[-1].get(field)
                sql_cursor.execute(sql,
                                   (
                                       time, top_layer, src_addr, dst_addr, json.dumps(http_header),
                                       json.dumps(http_data)))
                conn.commit()
            # file.write(str(packet) + '\n')


if __name__ == "__main__":
    main()
