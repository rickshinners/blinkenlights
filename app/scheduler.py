
from apscheduler.schedulers.background import BackgroundScheduler


def get_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.start()
    return scheduler
