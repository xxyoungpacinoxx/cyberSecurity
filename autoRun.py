from pathlib import Path
import subprocess

subprocess.run(['python3', "D:\YoungPacino\Cyber Security\Projects\wifi-netsh\windows-10-wifi-netsh\main.py"],
               capture_output=True).stdout.decode()
