docker-compose down
apt install python3-pip python3 -y
apt install tshark -y
pip3 install -r requirements.txt
apt install docker docker-compose -y
docker-compose up -d
sleep 5
nohup python3 listener.py -i br-800e2d7000bc -f "tcp port 80" >./listener.log 2>&1 &  
# For example: python3 listener.py -i br-800e2d7000bc -f "tcp port 80"
