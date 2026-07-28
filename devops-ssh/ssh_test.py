import paramiko

host = "192.168.99.179"
user = "ksadmin"
password = "test@123"
commands = [
	"hostname",
	"uptime -p",
	"free -h",
	"df -h"
]


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=host, username=user, password=password)

for cmd in commands:
	print(f"====={cmd}======")
	stdin, stdout, stderr = ssh.exec_command(cmd)
	print(stdout.read().decode())

ssh.close()
