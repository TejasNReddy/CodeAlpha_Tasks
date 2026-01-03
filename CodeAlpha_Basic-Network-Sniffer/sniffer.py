# Import required classes and functions from Scapy
# sniff  -> captures packets from the network
# IP     -> represents IP layer
# TCP    -> represents TCP protocol
# UDP    -> represents UDP protocol
# ICMP  -> represents ICMP protocol
# Raw   -> used to extract raw payload data
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


# This function is called automatically for EVERY captured packet
def packet_analyzer(packet):

    # Check whether the packet contains an IP layer
    if IP in packet:

        # Extract source and destination IP addresses
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Extract protocol number (6 = TCP, 17 = UDP, 1 = ICMP)
        protocol = packet[IP].proto

        # Print packet separator for readability
        print("\n==============================")

        # Display IP details
        print("Source IP      :", src_ip)
        print("Destination IP :", dst_ip)

        # Check if the packet uses TCP protocol
        if packet.haslayer(TCP):
            print("Protocol       : TCP")

            # Extract TCP source and destination ports
            print("Source Port    :", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        # Check if the packet uses UDP protocol
        elif packet.haslayer(UDP):
            print("Protocol       : UDP")

            # Extract UDP source and destination ports
            print("Source Port    :", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        # Check if the packet is ICMP (used for ping, traceroute)
        elif packet.haslayer(ICMP):
            print("Protocol       : ICMP")

        # Check if packet contains raw payload data
        if packet.haslayer(Raw):
            print("Payload        :", packet[Raw].load)


# Function that starts packet sniffing
def start_sniffing():

    print("Starting Network Sniffer...")
    print("Press CTRL + C to stop\n")

    # sniff() captures packets continuously
    # prn=packet_analyzer → sends each packet to packet_analyzer()
    # store=False → does NOT store packets in memory (saves RAM)
    sniff(prn=packet_analyzer, store=False)


# Program execution starts here
start_sniffing()
