from time import sleep
import recognize
from os import chdir, system, getcwd, fork, setsid, dup2, wait
from path import exists
import sys

def led_on():
	system("echo 1 > /sys/class/gpio/gpio13/value")

def led_off():
	system("echo 0 > /sys/class/gpio/gpio13/value")

def fan_run():
	system("echo 1 > /sys/class/gpio/gpio26/value")

def fan_stop():
	system("echo 0 > /sys/class/gpio/gpio26/value")

def flush_io() -> None:
	sys.stdout.flush()
	sys.stderr.flush()

def handle_client():
	cwd = getcwd()
	chdir("/sys/class/gpio/")
	if not exists("gpio26"):
		print("Exporting GPIO 26...")
		system("echo 26 > export")
	system("echo out > gpio26/direction")
	if not exists("gpio13"):
		print("Exporting GPIO 13...")
		system("echo 13 > export")
	system("echo out > gpio13/direction")
	if exists("gpio26") and exists("gpio13"):
		print("GPIO ports exported")
		chdir(cwd)
		fan_stop()
		led_off()
		fan_on = False
		recognize.led_on = led_on
		recognize.led_off = led_off
		while True:
			if recognize.recognize():
				if not fan_on:
					fan_on = True
					fan_run()
			elif fan_on:
				fan_stop()
				fan_on = False
			sleep(8)

if __name__ == "__main__":
	if fork() == 0:		#创建daemon
			setsid()
			#创建孙子进程，而后子进程退出
			if fork() > 0: sys.exit(0)
			#重定向标准输入流、标准输出流、标准错误
			flush_io()
			si = open("/dev/null", 'r')
			so = open("./log.txt", 'w')
			se = open("./log_err.txt", 'w')
			dup2(si.fileno(), sys.stdin.fileno())
			dup2(so.fileno(), sys.stdout.fileno())
			dup2(se.fileno(), sys.stderr.fileno())
			pid = fork()
			while pid > 0:			#监控服务是否退出
				#signal(SIGCHLD, SIG_IGN)
				#signal(SIGPIPE, SIG_IGN)		# 忽略管道错误
				wait()
				print("Subprocess exited, restarting...")
				pid = fork()
			if pid < 0: print("Fork error!")
			else: handle_client()
	else: print("Creating daemon...")
