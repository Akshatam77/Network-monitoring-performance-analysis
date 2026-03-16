import pandas as pd

data = pd.read_csv("../data/network_metrics.csv")

print("Average Latency:", data["Latency_ms"].mean())
print("Average Throughput:", data["Throughput_Mbps"].mean())
print("Total Packet Loss:", data["Packet_Loss_%"].sum())