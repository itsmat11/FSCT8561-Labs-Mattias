from scapy.all import rdpcap, IP, TCP, UDP


# Part 4: Load the PCAP

packets = rdpcap(
    "botnet-capture-20110812-rbot.pcap"
)


# Part 4: Counters

tcp_count = 0
udp_count = 0
shown = 0


print("First 20 IPv4 TCP/UDP packets:")
print()


# Part 4: Analyze packets

for pkt in packets:

    if IP in pkt:

        # TCP packet

        if TCP in pkt:

            tcp_count += 1

            if shown < 20:

                print(
                    "Source:", pkt[IP].src,
                    "Destination:", pkt[IP].dst,
                    "Protocol: TCP",
                    "Source port:", pkt[TCP].sport,
                    "Destination port:", pkt[TCP].dport
                )

                shown += 1


        # UDP packet

        elif UDP in pkt:

            udp_count += 1

            if shown < 20:

                print(
                    "Source:", pkt[IP].src,
                    "Destination:", pkt[IP].dst,
                    "Protocol: UDP",
                    "Source port:", pkt[UDP].sport,
                    "Destination port:", pkt[UDP].dport
                )

                shown += 1


# Part 4: Print summary

print()
print("Traffic Summary:")
print("Total TCP packets:", tcp_count)
print("Total UDP packets:", udp_count)