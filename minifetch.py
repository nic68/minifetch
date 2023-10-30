#!/data/data/com.termux/files/usr/bin/python3
from os import system as sy
try:
	import psutil
except Exception:
	sy("pip3 install psutil")
	import psutil
import platform
def conv(bytes, suffix="B"):
    fact = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < fact:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= fact
inf = platform.uname()
mem = psutil.virtual_memory()
frq = psutil.cpu_freq()
os_name = "Windows"
if inf.system == "Windows":
	sy("cls")
elif inf.system == "Linux":
    sy("clear")

    os_name_file = open("/etc/os-release",'r')
    os_name = os_name_file.readline()
    os_name_file.close()
    os_name = os_name[13:len(os_name)-2]

    # print(os_name)
#print("\033[33;1m=\033[m"*32)
print("  ", f"\033[37;1m• System:           \033[34;1m{os_name}\033[m")
print("  ", f"\033[37;1m• System version:   \033[36;1m{inf.release}\033[m")
print("  ", f"\033[37;1m• Architecture:     \033[35m{inf.machine}\033[m")
print("  ", f"\033[37;1m• RAM:              \033[32;1m{conv(mem.used)} / {conv(mem.total)} ({mem.percent}%)\033[m")
print("  ", f"\033[37;1m• CPU frequency:    \033[33;1m{frq.current:.2f}Mhz ({psutil.cpu_count(logical=False)} cores)\033[m")
