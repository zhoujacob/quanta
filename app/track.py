import psutil
import time

# # Checks if the selected app is running
def is_app_running(app_name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == app_name:
            print(f"{app_name} is running with PID: {proc.info['pid']}")
            return
    print(f"{app_name} is not currently running.")
    return 

# Retrieve app usage
# def track_app_usage(app_name):
