import psutil
import socket
from datetime import datetime

config = {}
with open('config.txt') as f:
	for line in f:
		key,Value = line.strip().split('=')
		config[key] = Value
print(config)
print(config['url'])

def get_cpu():
	return psutil.cpu_percent(interval=1)

def get_mem():
	return psutil.virtual_memory().percent

def get_disk():
	return psutil.disk_usage('/').percent

print("======xunjian======")
print(f"host: {socket.gethostname()}")
print(f"time: {datetime.now()}")
print(f"cpu: {get_cpu()}%")
print(f"mem: {get_mem()}%")
print(f"disk: {get_disk()}%")




cpu = psutil.cpu_percent(interval=1)
print(f"CPU: {cpu}%")
mem = psutil.virtual_memory()
print(f"total: {mem.total / 1024**3:.2f} GB")
print(f"used: {mem.used /1024**3:.2f} GB")
print(f"use: {mem.percent}%")

disk = psutil.disk_usage('/')
print(f"total: {disk.total / 1024**3:.2f} GB")
print(f"used: {disk.used / 1024**3:.2f} GB")
print(f"use: {disk.percent}%")


report = f"""
report:
time: {datetime.now()}
cpu: {cpu}%
mem: {mem.percent}%
disk: {disk.percent}%

"""
with open('report.txt', 'w') as f:
	f.write(report)

print("is ook")

