#!/usr/bin/env python3
from crontab import CronTab

# Init cron.
cron = CronTab(user = "pi")
cron.remove_all()

# Add new cron job.
job = cron.new(command = "monitorAndNotify.py")

# Job settings.
job.minute.every(1)
cron.write()