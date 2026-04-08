import time
import webbrowser
from datetime import datetime

def main():
    print("Starting AEP Grid Monitoring")
    
    # First cycle: get data and create initial map
    print("Initial data collection...")
    
    # Step 1: Get weather data
    from weathercsv import process_all_transmission_lines_vectorized
    process_all_transmission_lines_vectorized()
    
    # Step 2: Run thermal analysis  
    from formulas import main as thermal_main
    thermal_main()
    
    # Step 3: Create initial map
    from map import update_map
    update_map()
    
    # Open map in browser
    print("Opening map in browser...")
    webbrowser.open("simple_power_map.html")
    
    # Auto-update every 5 minutes
    print("Auto-updating every 5 minutes...")
    cycle_count = 1
    
    while True:
        time.sleep(300)  # 5 minutes
        cycle_count += 1
        print(f"Update #{cycle_count} at {datetime.now().strftime('%H:%M:%S')}")
        
        try:
            process_all_transmission_lines_vectorized()
            thermal_main()
            update_map()
        except Exception as e:
            print(f"Update failed: {e}")

if __name__ == "__main__":
    main()