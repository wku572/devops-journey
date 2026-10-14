# Week 2: Bash Scripting

## What's here
- `basics.sh`: practice script covering variables, arguments, conditions, and loops.
- `backup.sh`: backs up a folder into a timestamped `.tar.gz` archive and logs
  SUCCESS or FAILED to `~/backups/backup.log`.

## How to run
```
chmod +x backup.sh
./backup.sh ~/practice
```
Running it with no folder prints a usage message. A missing folder prints an
error and exits with code 1.

## Scheduling
I scheduled the backup with cron to run daily at 6 PM:
```
0 18 * * * /home/santa/scripts/backup.sh /home/santa/practice
```

## What I learned
- Exit codes: `exit 1` signals failure, and `echo $?` shows the last result.
- Always check that input exists before acting on it.
- A `*` pattern that matches nothing is passed through as plain text, so a
  loop can run on a folder that does not exist.
- Cron needs full paths and only runs while WSL is open.

