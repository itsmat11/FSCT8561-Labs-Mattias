from scapy.all import rdpcap, IP, TCP, UDP


# Part 2: Read the PCAP

packets = rdpcap(
    "botnet-capture-20110812-rbot.pcap"
)


# Part 2 Step 1: Display all fields of the first packet

print("First packet details:")
packets[0].show()


# Part 2 Step 2: Check if first packet contains IPv4

pkt = packets[0]

print()
print("Contains IPv4?", IP in pkt)


# Part 2 Step 3: Print source and destination IP if available

if IP in pkt:
    print("Source IP:", pkt[IP].src)
    print("Destination IP:", pkt[IP].dst)
else:
    print("First packet does not contain IPv4")


# Part 2 Step 4: Show first five IPv4 packets

print()
print("First five IPv4 packets:")

shown = 0

for pkt in packets:

    if IP in pkt:

        print(
            pkt[IP].src,
            "->",
            pkt[IP].dst
        )

        shown = shown + 1

        if shown == 5:
            break


# Part 2 Step 5: Find a TCP packet and display its flags

print()
print("TCP flags:")

for pkt in packets:

    if TCP in pkt:

        print(pkt[TCP].flags)

        break


# Part 2 Step 6: Display packet size and timestamp

pkt = packets[0]

print()
print("Size (bytes):", len(pkt))
print("Timestamp:", float(pkt.time))


# Part 2 Step 7: Combine fields for five IPv4 packets

print()
print("First five IPv4 packet details:")

shown = 0

for pkt in packets:

    if IP in pkt:

        print(
            "Source:", pkt[IP].src,
            "Destination:", pkt[IP].dst,
            "Bytes:", len(pkt),
            "Time:", float(pkt.time)
        )

        shown = shown + 1

        if shown == 5:
            break