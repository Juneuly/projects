from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

#define jobs
#def job():
#    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#    os.system('date >> time.log')

def task(fre, time):
    scheduler = BlockingScheduler()
    scheduler.add_job(job, fre , seconds = time)
    scheduler.start()

if __name__ == '__main__':
    fre = 'interval'
    time = 5
    task(fre, time)
