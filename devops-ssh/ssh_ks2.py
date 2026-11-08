import os
import paramiko

def run_command(host, user, password, command):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host, username=user, password=password)

	stdin, stdout, stderr = ssh.exec_command(command)
	result = stdout.read().decode()

	ssh.close()
	return result
print(run_command(
	os.environ["LAB_HOST_1"],
	os.environ.get("LAB_USER", "ksadmin"),
	os.environ["LAB_SSH_PASSWORD"],
	"uptime -p",
))
