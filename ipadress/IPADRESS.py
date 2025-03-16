import socket
import requests

# Local IP address find karein
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

# Public IP address find karein
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        public_ip = response.json()['ip']
        return public_ip
    except Exception as e:
        return "Unable to fetch public IP"

# IP addresses print karein
print("Local IP Address:", get_local_ip())
print("Public IP Address:", get_public_ip())