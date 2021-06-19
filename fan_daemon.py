from time import sleep
import recognize
from os import chdir, system, getcwd
from os.path import exists

def led_on():
    system("echo 1 > /sys/class/gpio/gpio25/value")

def led_off():
    system("echo 0 > /sys/class/gpio/gpio25/value")

if __name__ == "__main__":
    cwd = getcwd()
    chdir("/sys/class/gpio/")
    if not exists("gpio21"):
        print("Exporting GPIO 21...")
        system("echo 21 > export")
        system("echo out > gpio21/direction")
    if not exists("gpio25"):
        print("Exporting GPIO 25...")
        system("echo 25 > export")
        system("echo out > gpio25/direction")
    if exists("gpio21") and exists("gpio25"):
        print("GPIO ports exported")
        chdir(cwd)
        system("echo 0 > /sys/class/gpio/gpio21/value")
        system("echo 0 > /sys/class/gpio/gpio25/value")
        fan_on = False
        recognize.led_on = led_on
        recognize.led_off = led_off
        while True:
            if recognize.recognize():
                if not fan_on:
                    fan_on = True
                    system("echo 1 > /sys/class/gpio/gpio21/value")
            elif fan_on:
                system("echo 0 > /sys/class/gpio/gpio21/value")
                fan_on = False
            sleep(8)
