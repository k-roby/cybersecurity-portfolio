# Update Allow List Using Python

This script demonstrates how to update an `allow_list.txt` file by removing IP addresses that match any in a predefined `remove_list`.

## 🗂️ Project Purpose

Automating the cleanup of an allow list can help streamline access control in environments where IP restrictions are used. This script simulates a scenario where a security analyst needs to revoke access for outdated or malicious IPs.

## 🧪 What the Script Does

- Reads a file called `allow_list.txt` containing allowed IP addresses
- Compares those against a predefined list of IPs to remove
- Removes matching IPs
- Overwrites the original file with the updated list

## 🧾 Example Code

```python
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
```

## ✅ Skills Demonstrated

- File I/O and data sanitation
- List operations in Python
- Basic scripting for cybersecurity automation
