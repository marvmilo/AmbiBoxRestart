import psutil
import time
import subprocess
import os

os.chdir("C:\\Program Files (x86)\\AmbiBox")
# subprocess.Popen(["AmbiBox.exe"])

N_CPU_TIME_NOT_CHANGED = 5

current_cpu_time = 0
cpu_time_not_changed = 0

while True:
    for proc in psutil.process_iter():
        if proc.name().startswith("AmbiBox"):
            if proc.cpu_times().user == current_cpu_time:
                cpu_time_not_changed += 1
            else:
                cpu_time_not_changed = 0
            current_cpu_time = proc.cpu_times().user
            if cpu_time_not_changed >= N_CPU_TIME_NOT_CHANGED:
                proc.kill()
                time.sleep(1)
                subprocess.Popen(["AmbiBox.exe"])
                cpu_time_not_changed = 0
            print(current_cpu_time, cpu_time_not_changed)
    time.sleep(5)