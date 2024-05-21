# Task pom:

Task Pom is a simple command-line Pomodoro clock for Macs that logs your tasks to a text log file and records them in DuckDB for later analysis.

Currently, it is created specifically for Macs. 

The Mac-specific function is `play_sound(sound_file)`, which uses AppKit NSSound.

## Basic Usage: Time is in minutes

`python3 task_pom.py --time 10 --log "Testing dbtask"`

### Example Output:

```
python task_pom --time 15 --log "Terraform cleanup on st "
Started at 11:10 PM
Progress: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 [01:00<00:00,  1.00s/it]
Time is UP! 11:25 PM

Logs from the last 12 hours:
+------------------------+------------+----------+----------+----------------------------+------------------------------------------------------+
|       File Name        | Start Time | End Time | Duration |         Created On         |                       Comment                        |
+------------------------+------------+----------+----------+----------------------------+------------------------------------------------------+
| task_logs_20240520.log |  08:32 AM  | 08:47 AM |    15    | 2024-05-20 08:47:11.553615 |           Emails for access and tag Review           |
| task_logs_20240520.log |  09:33 AM  | 09:48 AM |    15    | 2024-05-20 09:48:25.519892 |    Add granular logging - set_schema function        |
| task_logs_20240520.log |  09:52 AM  | 10:07 AM |    15    | 2024-05-20 10:07:43.912468 |         Git actions sync fix for schemachange        |
| task_logs_20240520.log |  10:14 AM  | 10:29 AM |    15    | 2024-05-20 10:29:47.666206 |                 Morning Review Jira                  |
| task_logs_20240520.log |  11:10 AM  | 11:25 AM |    15    | 2024-05-20 11:25:51.225721 |            Terraform cleanup on st                   |
+------------------------+------------+----------+----------+----------------------------+------------------------------------------------------+

```

This command will run a task for the specified time in minutes.

- Once the time is up, it will play an audible sound.
- The task will be logged to a database and a log file.
- The program will then display logs from the last 24 hours to review what you have completed for the day.

## What is inside? 


### Directory structure:

```
├── README.md
├── bin
│   └── create_db.py                 (Creates Database if it doesn't exist)
├── data
│   ├── stop_clock_completed.mp3     (Audible Sound file for completion)
│   └── task_pom.db                  (Duck DB Serverless File)
├── requirements.txt                 (requirements for install)
├── task_log
│   ├── task_logs_20240326.log       (Writes a log file in this format)
└── task_pom                         (Main processing)
```

### Third Party Modules:
```
duckdb         DuckDB Serveless Database
AppKit         To play sounds    
tqdm           Graphs the time to see the progress 
prettytable    When querries the DB it shows in a formated table.  
```

## Install:

either run the requirements on your system pip or run use a 