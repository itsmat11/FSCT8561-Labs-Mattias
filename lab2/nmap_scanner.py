import socket
import nmap


# Part 12: Create the Nmap scanner object

scanner = nmap.PortScanner()


# Part 12: Accept user input and resolve the target

target = input("Enter target host: ")

try:
    target_ip = socket.gethostbyname(target)
    print("Target:", target_ip) 

except socket.gaierror:
    print("Invalid hostname or IP address")
    exit()


# Part 12: Get the start and end ports

try:
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

except ValueError:
    print("Invalid port. Please enter numbers only.")
    exit()


# Part 12: Validate the port range

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


# Part 12: Convert the port range into Nmap format

port_range = str(start_port) + "-" + str(end_port)


# Part 12: Run the Nmap scan

try:
    scanner.scan(
        target_ip,
        port_range
    )

except Exception as error:
    print("Nmap scan failed:", error)
    exit()


# Part 12: Make sure Nmap returned results for the target

if target_ip not in scanner.all_hosts():
    print("No scan results were returned.")
    exit()


# Part 12: Display TCP scan results

if "tcp" in scanner[target_ip]:

    print()
    print("PORT      STATE      SERVICE")

    for port in sorted(scanner[target_ip]["tcp"]):

        state = scanner[target_ip]["tcp"][port].get(
            "state",
            "unknown"
        )

        service = scanner[target_ip]["tcp"][port].get(
            "name",
            "unknown"
        )

        print(
            port,
            "     ",
            state,
            "     ",
            service
        )

else:
    print("No TCP ports found.")


# Part 12: Finish the scan

print()
print("Scan complete.")