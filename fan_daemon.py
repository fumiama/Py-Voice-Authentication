from time import sleep
import recognize
from os import chdir, system, getcwd
from os.path import exists

def led_on():
    system("echo 1 > /sys/class/gpio/gpio13/value")

def led_off():
    system("echo 0 > /sys/class/gpio/gpio13/value")

def fan_run():
    system("echo 1 > /sys/class/gpio/gpio26/value")

def fan_stop():
    system("echo 0 > /sys/class/gpio/gpio26/value")

if __name__ == "__main__":
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
