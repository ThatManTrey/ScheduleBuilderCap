# scheduler
from rq import Queue
from rq_scheduler import Scheduler

from datetime import datetime

def start_scraper():
    scheduler.schedule(
        scheduled_time=datetime.utcnow()+60,
        func=scrape,
        interval=86400  # once a day
    )

def scrape():
    # do stuff here
    print()