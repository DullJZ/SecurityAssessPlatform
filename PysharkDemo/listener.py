import pyshark
import argparse
import json

from dbconn import conn

def detect_sql_injection(url):
    sql_keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'DROP', 'UNION', 'EXEC', 'TRUNCATE', 'OR', 'AND']
    # 提取URL中的参数
    params = url.split('?')
    if len(params) < 2:
        return False
    url = params[1]
    url = url.split('&')
    if len(url) == 0:
        return False
    for i in url:
        t = i.split('=')
        if len(t) < 2:
            continue
        for keyword in sql_keywords:
            if keyword in t.upper():
                print('SQL Injection detected!')
                return True
    return False

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
                sql = ("INSERT INTO xhcms (timestamp, top_layer, src_ip, dst_ip, http_header, http_data, is_sql_hack) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)")  # Updated SQL statement
                http_header = {}
                for field in packet.http.field_names:
                    # print(f"{field}: {packet.http.get(field)}")
                    http_header[field] = packet.http.get(field)
                # 检测full_uri
                is_sql_hack = 0
                if 'request_full_uri' in http_header:
                    if detect_sql_injection(http_header['request_full_uri']):
                        is_sql_hack = 1
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
                                        json.dumps(http_data), is_sql_hack)) 
                conn.commit()
                # file.write(str(packet) + '\n')


if __name__ == "__main__":
    main()
