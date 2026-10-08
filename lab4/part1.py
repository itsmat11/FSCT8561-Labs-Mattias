from scapy.all import rdpcap, TCP, UDP


# Part 1 Step 1-2: Read the PCAP file

packets = rdpcap("botnet-capture-20110812-rbot.pcap")


# Part 1 Step 3: Count total packets

print("Number of packets:", len(packets))


# Part 1 Step 4: Show the first packet

print()
print("First packet:")
print(packets[0].summary())


# Part 1 Step 5: Show the first five packets

print()
print("First five packets:")

for pkt in packets[:5]:
    print(pkt.summary())


# Part 1 Step 6: Check if the first packet is TCP

pkt = packets[0]

print()
print("Is first packet TCP?", TCP in pkt)


# Part 1 Step 7: Keep only TCP packets

tcp_packets = []

for pkt in packets:
    if TCP in pkt:
        tcp_packets.append(pkt)

print()
print("TCP packets:", len(tcp_packets))


# Part 1 Step 8: Show up to 50 TCP packets

print()
print("First TCP packets:")

for pkt in tcp_packets[:50]:
    print(pkt.summary())


# Part 1 Step 9: Filter TCP port 80

http_packets = []

for pkt in tcp_packets:
    if pkt[TCP].sport == 80 or pkt[TCP].dport == 80:
        http_packets.append(pkt)

print()
print("TCP port 80 packets:", len(http_packets))


# Part 1 Step 10: Filter UDP port 53

dns_packets = []

for pkt in packets:
    if UDP in pkt:
        if pkt[UDP].sport == 53 or pkt[UDP].dport == 53:
            dns_packets.append(pkt)

print("UDP port 53 packets:", len(dns_packets))