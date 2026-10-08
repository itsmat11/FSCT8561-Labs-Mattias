from scapy.all import rdpcap, IP, TCP, UDP


# Part 5: Load the PCAP

packets = rdpcap(
    "botnet-capture-20110812-rbot.pcap"
)


# Part 5: Sort packets by timestamp

packets = sorted(
    packets,
    key=lambda pkt: float(pkt.time)
)


# Part 5: Counters

tcp_count = 0
udp_count = 0


# Part 5: Store recent timestamps for each source IP

recent_packets = {}


# Part 5: Store IPs that already triggered an alert

alerted_ips = set()


# Part 5: Analyze packets

for pkt in packets:

    if IP in pkt and (TCP in pkt or UDP in pkt):

        source_ip = pkt[IP].src
        current_time = float(pkt.time)


        # Count TCP and UDP packets

        if TCP in pkt:
            tcp_count += 1

        elif UDP in pkt:
            udp_count += 1


        # Create a timestamp list for new IPs

        if source_ip not in recent_packets:
            recent_packets[source_ip] = []


        # Remove timestamps older than 5 seconds

        recent_packets[source_ip] = [
            timestamp
            for timestamp in recent_packets[source_ip]
            if current_time - timestamp <= 5
        ]


        # Add current packet timestamp

        recent_packets[source_ip].append(
            current_time
        )


        # Alert if more than 20 packets occur in 5 seconds

        if (
            len(recent_packets[source_ip]) > 20
            and source_ip not in alerted_ips
        ):

            print(
                "ALERT:",
                source_ip,
                "sent more than 20 packets within 5 seconds"
            )

            alerted_ips.add(
                source_ip
            )


# Part 5: Print final summary

print()
print("IDS Summary:")
print("Total TCP packets:", tcp_count)
print("Total UDP packets:", udp_count)
print("Suspicious IPs:", len(alerted_ips))