
import socket


# Part 4: Create a function to scan one TCP port

def scan_port(target, port):

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.settimeout(0.5)

    result = sock.connect_ex(
        (target, port)
    )

    sock.close()

    if result == 0:
        return True
    else:
        return False


# Part 7: Accept user input and resolve the target

target = input("Enter target host: ")

try:
    target_ip = socket.gethostbyname(target)
    print("Scanning:", target_ip)

except socket.gaierror:
    print("Invalid hostname or IP address")
    exit()


# Part 7: Get the start and end ports from the user

try:
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

except ValueError:
    print("Invalid port. Please enter numbers only.")
    exit()


# Part 8: Validate the port range

if start_port < 1 or start_port > 65535:
    print("Start port must be between 1 and 65535.")
    exit()

if end_port < 1 or end_port > 65535:
    print("End port must be between 1 and 65535.")
    exit()

if start_port > end_port:
    print("Start port cannot be greater than end port.")
    exit()

if end_port - start_port > 1000:
    print("Port range cannot be larger than 1000 ports.")
    exit()


# Part 5: Scan a small range of ports and track open ports

open_ports = []

for port in range(start_port, end_port + 1):

    if scan_port(target_ip, port):
        open_ports.append(port)


        # Part 6: Identify the likely service for each open port

        try:
            service = socket.getservbyport(
                port,
                "tcp"
            )
        except OSError:
            service = "unknown"

        print(
            "Port",
            port,
            "is OPEN - likely service:",
            service
        )


# Part 9: Display the final scan results

if len(open_ports) == 0:
    print("No open ports found in range sorry!")
else:
    print(len(open_ports), "open port(s) found.")

print("Scan complete.")