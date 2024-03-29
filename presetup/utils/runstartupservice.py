import os
import getpass
import subprocess
from logger.logger import setup_logger
p = setup_logger()

def create_systemd_service(script_path, service_name,desc):
    service_content = f"""[Unit]
Description={desc}
After=network.target

[Service]
ExecStart=/usr/bin/python3 {script_path}
WorkingDirectory={os.path.dirname(script_path)}
Restart=always
User={getpass.getuser()}

[Install]
WantedBy=multi-user.target
"""

    service_file_path = f'/etc/systemd/system/{service_name}.service'
    with open(service_file_path, 'w') as service_file:
        service_file.write(service_content)

    return True

def enable_start_systemd_service(service_name):
    try:
        res = os.system(f'sudo systemctl enable {service_name}.service')
        res2 = os.system(f'sudo systemctl start {service_name}.service')
        p.info(f"run {service_name} ,{res} , {res2}")
        return True
    except subprocess.CalledProcessError as e:
        p.error(f"error : {str(e)}")
    


def run_startup(script_name,service_name,script_path):
    service_file_path = create_systemd_service(script_path, service_name,script_name+".rentdrive")
    enable_start_systemd_service(service_name)

    print(f"Systemd service file created at: {service_file_path}")
    print(f"Service '{service_name}' enabled and started.")