
from apscheduler.schedulers.background import BackgroundScheduler
from cron_jobs.otpJobs.job import unbanUserOTP
def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(unbanUserOTP, 'cron', second='*/1')
    scheduler.start()
    return scheduler
