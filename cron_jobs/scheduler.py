from apscheduler.schedulers.background import BackgroundScheduler
from .jobs.say_hello import scheduled_say_hello

def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_say_hello, 'cron', minute='*/1')
    scheduler.start()
    return scheduler
