from scapy.all import *
import netifaces

DNS_IP = '127.0.0.1'

FILTER = 'udp port 53'

def dns():
    print("DNS is listening...")
    interfaces = netifaces.interfaces()
    while True:
        packet = sniff(filter=FILTER, iface = interfaces, count=1)
        print(packet.summary())


if __name__ == '__main__':
    dns()
