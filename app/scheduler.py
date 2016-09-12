
from apscheduler.schedulers.background import BackgroundScheduler

__scheduler = BackgroundScheduler()
__scheduler.start()


def get_scheduler():
    return __scheduler
