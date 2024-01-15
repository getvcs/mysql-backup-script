# Weekly MySQL Database Backup

## Description

This Python script automates backing up a MySQL database on a regular schedule. It prompts the user for the database connection details, name of the database to backup, backup location, and frequency. It then uses the `schedule` and `subprocess` modules to run `mysqldump` at the specified interval to create a timestamped SQL backup file. 

## Usage

1. Install required Python packages:

    ```bash
    pip install schedule
    ```

2. Run the script:

    ```bash
    python backup.py
    ```

3. Enter the requested info when prompted:
   - MySQL username
   - MySQL password  
   - Database name
   - Backup frequency (days)
   - Backup file location

4. The script will now automatically backup the database to the specified location per the set schedule.

## Credits

Written by [Alfie](https://github.com/alfiegnu)

## License

This project is open source and available under the [MIT License](LICENSE).
