# Python default imports
import os, time, socket
from datetime import datetime

# Third party libs
from pyfiglet import Figlet
import streamlit as st

# Main method
def main():
    st.switch_page("./pages/00_home.py")

# Main route declaration
if __name__ == "__main__":

    # Get server start info
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:")
    hostname = socket.gethostname()

    try:
        # Get the primary local IP (the one used to connect to the internet)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        local_ip = "Unable to detect"

    # Print the app info
    print(f"---------------------------------------------------")
    f = Figlet(font="small")
    print(f.renderText("ML playbook V0.1"))
    print(f"-- Starting at {start_time} by {os.getlogin()}...")
    print(f"-- {hostname} | {local_ip}")
    print(f"---------------------------------------------------")
    print(f"-- Local Access: http://localhost:8501")
    print(f"-- Local Access: http://127.0.0.1:8501")
    print(f"-- Network Access: http://{local_ip}:8501")
    print(f"-- Network Access: http://{hostname}:8501")
    print(f"")
    print(f"---------------------------------------------------")

    # Effectively start the app
    main()