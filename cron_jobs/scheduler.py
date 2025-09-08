<<<<<<< HEAD
# from apscheduler.schedulers.background import BackgroundScheduler
# from .jobs.say_hello import scheduled_say_hello

# def init_scheduler():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(scheduled_say_hello, 'cron', minute='*/1')
#     scheduler.start()
#     return scheduler
=======
from apscheduler.schedulers.background import BackgroundScheduler
from cron_jobs.otpJobs.job import unbanUserOTP
def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(unbanUserOTP, 'cron', second='*/1')
    scheduler.start()
    return scheduler
>>>>>>> 4adc65a67a0fb1c71747d6bc2d95dd606f5c9e34
