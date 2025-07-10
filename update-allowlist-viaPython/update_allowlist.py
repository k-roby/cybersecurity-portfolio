# Load and clean allow_list.txt by removing any IPs in the remove_list

# Read the allow list
with open("allow_list.txt", "r") as file:
    ip_addresses = file.read()

# Convert to list
ip_addresses = ip_addresses.split()

# Define the remove list (example IPs)
remove_list = ["192.168.1.10", "10.0.0.5"]

# Remove matching IPs
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Convert back to string
ip_addresses = "\n".join(ip_addresses)

# Overwrite the original file
with open("allow_list.txt", "w") as file:
    file.write(ip_addresses)
