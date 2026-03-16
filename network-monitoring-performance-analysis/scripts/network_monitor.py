import subprocess
import time

target = "8.8.8.8"

print("Starting Network Monitoring...")

while True:
    response = subprocess.run(["ping","-n","1",target],capture_output=True,text=True)

    if "TTL=" in response.stdout:
        print("Network reachable")
    else:
        print("Packet loss detected")

    time.sleep(5)