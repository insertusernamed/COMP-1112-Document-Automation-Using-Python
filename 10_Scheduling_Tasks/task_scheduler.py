import schedule
import time


def task():
    print("Scheduled task is running...")


# Scheduling the task to run every 10 seconds
schedule.every(10).seconds.do(task)

# Scheduling the task to run every minute
# schedule.every().minute.do(task)

# Scheduling the task to run daily at a specific time
# schedule.every().day.at("10:30").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
