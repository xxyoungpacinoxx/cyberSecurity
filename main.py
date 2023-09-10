import subprocess
import re
import datetime


start_time = datetime.datetime.now()
netsh_wlan_show_profiles_command = subprocess.run('netsh wlan show profiles', capture_output=True).stdout.decode()
wifi_ssid_list = re.findall('All User Profile     : (.*)\r', netsh_wlan_show_profiles_command)

final_export = list()

for ssid in wifi_ssid_list:
    if len(ssid) != 0:
        wifi_profile = dict()
        netsh_wlan_show_profile_command = subprocess.run(f'netsh wlan show profile "{ssid}"', capture_output=True).stdout.decode()
        if re.search('Security key           : Absent', netsh_wlan_show_profile_command):
            continue
        else:
            wifi_profile['ssid'] = ssid

            netsh_wlan_show_profile_key_clear_command = subprocess.run(
                f'netsh wlan show profile "{ssid}" key=clear',
                capture_output=True).stdout.decode()
            key_content = re.search('Key Content            : (.*)\r', netsh_wlan_show_profile_key_clear_command)

            wifi_profile['password'] = key_content[1]
            final_export.append(wifi_profile)
for item in final_export:
    print(item)
end_time = datetime.datetime.now()

print(f'Duration:{end_time - start_time}')

