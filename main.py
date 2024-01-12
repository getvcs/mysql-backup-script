import schedule
import time
import os
import datetime
import subprocess
import getpass

db_username = input("Enter your username to connect to MySQL. ")
db_pass = getpass.getpass("Enter the password for " + db_username + ". ")
db_name = input("Enter database you would like to backup. ")
backup_time = int(input("How long do you want each backup? (in days) "))
backup_path = input("Enter where you would like backups to be stored. ")


def backup():
    print("[Weekly Backup] Backing up MySQL Database.")

    backup_folder = backup_path + db_name
    if not (os.path.exists(backup_folder)):
        try:
            os.makedirs(backup_folder)
        except OSError as e:
            print("Failed to create directory:", e)

    today = datetime.date.today()
    today_str = today.strftime("%m-%d-%Y")

    file_name = today_str + ".sql"
    backup_file = os.path.join(backup_folder, file_name)

    cmd = f"mysqldump -u {db_username} -p{db_pass} {db_name} > {backup_file}"
    try:
        with open(backup_file, "w", encoding="utf-8") as f:
            subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error opening backup file:", e)

    print(f'[Weekly Backup] Made {file_name} in {backup_folder}')


schedule.every(backup_time).seconds.do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)
