import os
import time
import subprocess

def write_to_log(message):
    with open('/var/log/KI-Rijnyak.log', 'a') as f:
        f.write(message + '\n')

def run_command():
    result = subprocess.run(['timedatectl'], stdout=subprocess.PIPE)
    lines = result.stdout.decode('utf-8').split('\n')
    for line in lines:
        if 'Local time' in line:
            return line
    return ''

def main():
    if not os.path.exists('/var/log/KI-Rijnyak.log'):
        write_to_log('Service started successfully')
    while True:
        output = run_command()
        write_to_log(output)
        time.sleep(6)

if __name__ == '__main__':
    main()
