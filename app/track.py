import psutil
import time
import subprocess
from datetime import datetime
from app.db import log_app_start, log_app_end, init_db, get_db_connection


# Detects the idle time
def get_idle_time():
    idle_time_cmd = 'ioreg -c IOHIDSystem | awk \'/HIDIdleTime/ {print $NF/1000000000; exit}\''
    idle_time = subprocess.check_output(idle_time_cmd, shell=True)
    return float(idle_time)

# Checking if the app is in the foreground
def is_app_in_foreground(app_name):
    active_app_cmd = '''osascript -e 'tell application "System Events" to get name of first application process whose frontmost is true' '''
    try:
        frontmost_app = subprocess.check_output(active_app_cmd, shell=True).strip().decode('utf-8')
        return frontmost_app == app_name
    except subprocess.CalledProcessError:
        return False

# Retrive app usage using psutil, run in the background
def track_app_usage(app_name):
    init_db()
    print(f"Starting app usage tracking for {app_name}...")  # Add this to verify function call
    app_running = False

    while True:
        print(f"Checking if {app_name} is in foreground...")
        app_is_foreground = is_app_in_foreground(app_name)
        
        print(f"Checking idle time for {app_name}...")
        idle_time = get_idle_time()

        print(f"App {app_name} in foreground: {app_is_foreground}, Idle time: {idle_time}")


        # Only log active time if app is in foreground and user is not idle
        if app_is_foreground and idle_time < 300:  # User is not idle if idle time < 300 seconds (5 mins)
            if not app_running:
                print(f"{app_name} is actively being used.")
                log_app_start(app_name)
                app_running = True
        elif app_running:
            # JACOB CHECK THIS
            print(f"{app_name} is no longer actively used or user is idle.")
            log_app_end(app_name)
            app_running = False
        
        time.sleep(30)  # Poll every 30 seconds to reduce CPU usage


