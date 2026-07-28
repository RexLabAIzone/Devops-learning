import paramiko

from datetime import datetime
server = [
	{"host": "192.168.99.179", "user": "ksadmin", "password": "test@123"},
	{"host": "192.168.99.184", "user": "ksadmin", "password": "test@123"},
]


def run_command(server, command):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server["host"], username=server["user"], password=server["password"])

	stdin, stdout, stderr = ssh.exec_command(command)
	result = stdout.read().decode()

	ssh.close()
	return result
print("=======xunjian=========")
for servers in server:
	hostname = run_command(servers, "hostname")
	uptime = run_command(servers, "uptime -p")
	cpu = run_command(servers, "top -bn1 |grep Cpu | awk '{print $2}'")
	disk = run_command(servers, "df -h / |tail -1 | awk '{print $5}'")
	

	print("--------------------")
	print(f"serverip: {servers['host']}")
	print(f"servename: {hostname}")
	print(f"uptime: {uptime}")
	print(f"cpu: {cpu}")
	print(f"disk: {disk}")
