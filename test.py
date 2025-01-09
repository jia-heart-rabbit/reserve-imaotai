import schedule
import time

def my_task():
    print("定时任务执行中...")

schedule.every(3).seconds.do(my_task)
schedule.every(2).seconds.do(my_task)

while True:
    schedule.run_pending()
    # time.sleep(1)
