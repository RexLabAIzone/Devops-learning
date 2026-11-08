import os
import paramiko

host = os.environ["LAB_HOST"]
user = os.environ.get("LAB_USER", "ksadmin")
password = os.environ["LAB_SSH_PASSWORD"]
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
