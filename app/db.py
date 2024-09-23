import sqlite3
from datetime import datetime

# Initialize the SQLite connection
def get_db_connection():
    conn = sqlite3.connect('app_usage.db')
    return conn

# Create the app_usage table with the new schema if it doesn't exist.
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS app_usage (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        app_name TEXT,
                        start_time TEXT,
                        end_time TEXT,
                        active_time REAL
                      )''')
    conn.commit()
    conn.close()

# Insert a new entry for when the app starts running
def log_app_start(app_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO app_usage (app_name, start_time) VALUES (?, ?)', 
                   (app_name, start_time))
    conn.commit()
    print(f"Logged start time for {app_name} at {start_time}")
    conn.close()

def log_app_end(app_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''SELECT id, start_time FROM app_usage 
                      WHERE app_name = ? AND end_time IS NULL 
                      ORDER BY start_time DESC LIMIT 1''', 
                   (app_name,))
    row = cursor.fetchone()
    
    if row:
        log_id, start_time_str = row
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
        active_time = (datetime.now() - start_time).total_seconds()
        
        # Update the row with end_time and active_time
        cursor.execute('''UPDATE app_usage 
                          SET end_time = ?, active_time = ? 
                          WHERE id = ?''', 
                       (end_time, active_time, log_id))
        conn.commit()
        print(f"Logged end time for {app_name} at {end_time} with active time {active_time} seconds")
    else:
        print(f"No matching start entry found for {app_name}.")
    conn.close()
