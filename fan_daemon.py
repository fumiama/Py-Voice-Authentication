from recognize import recognize
from os import chdir, system, getcwd
from os.path import exists

if __name__ == "__main__":
    cwd = getcwd()
    chdir("/sys/class/gpio/")
    if not exists("gpio21"):
        print("Exporting GPIO 21...")
        system("echo 21 > export")
        system("echo out > gpio21/direction")
    if exists("gpio21"):
        print("GPIO 21 exported")
        chdir(cwd)
        system("echo 0 > /sys/class/gpio/gpio21/value")
        fan_on = False
        while True:
            if recognize():
                if not fan_on:
                    fan_on = True
                    system("echo 1 > /sys/class/gpio/gpio21/value")
            elif fan_on:
                system("echo 0 > /sys/class/gpio/gpio21/value")
                fan_on = False
            system("sleep 1")
