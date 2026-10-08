from scapy.all import rdpcap, Raw


# Part 3: Read the PCAP

packets = rdpcap(
    "botnet-capture-20110812-rbot.pcap"
)


# Part 3 Step 2: Check first packet for Raw payload

pkt = packets[0]

print(
    "Contains Raw payload?",
    Raw in pkt
)


# Part 3 Step 3: Show short payload sample if available

if Raw in pkt:

    print(
        repr(
            bytes(pkt[Raw].load)[:80]
        )
    )

else:

    print(
        "No Raw payload in this packet"
    )


# Part 3 Step 4: Find the first packet with a payload

print()
print("First Raw payload sample:")

for pkt in packets:

    if Raw in pkt:

        print(
            repr(
                bytes(pkt[Raw].load)[:80]
            )
        )

        break


# Part 3 Step 5: Try to display readable text

print()
print("Readable payload sample:")

for pkt in packets:

    if Raw in pkt:

        sample = bytes(
            pkt[Raw].load
        )[:80]

        print(
            sample.decode(
                "utf-8",
                errors="replace"
            )
        )

        break


# Part 3 Step 6: Search for User-Agent header

found = False

for pkt in packets[:500]:

    if Raw in pkt:

        data = bytes(
            pkt[Raw].load
        )

        if b"User-Agent:" in data:

            print()
            print(
                "Possible plaintext HTTP header found"
            )

            found = True

            break


if not found:

    print()
    print(
        "No matching header found in the first 500 packets"
    )