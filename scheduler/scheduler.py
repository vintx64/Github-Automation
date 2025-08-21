## Folder: scheduler
# File: scheduler.py

from datetime import datetime, timedelta
from config.settings import START_DATE, TOTAL_DAYS, TASK_MAPPING
from utils.helpers import logger

class Scheduler:
    def __init__(self, start_date: datetime, total_days: int, mapping: dict):
        self.start_date = start_date
        self.total_days = total_days
        self.mapping = mapping

    def get_today_task(self) -> str:
        today = datetime.now().date()
        delta = (today - self.start_date.date()).days
        logger.info(f"Today is {today}, project started {delta} days ago.")

        if delta < 0:
            logger.warning("Project hasn't started yet.")
            return "not_started"
        elif delta >= self.total_days:
            logger.info("Project duration completed.")
            return "completed"
        else:
            return self.mapping.get(delta, "unknown_task")

    def is_today_valid(self) -> bool:
        today = datetime.now().date()
        return self.start_date.date() <= today < (self.start_date + timedelta(days=self.total_days)).date()

    def get_remaining_days(self) -> int:
        today = datetime.now().date()
        remaining = (self.start_date + timedelta(days=self.total_days)).date() - today
        return max(0, remaining.days)


scheduler = Scheduler(START_DATE, TOTAL_DAYS, TASK_MAPPING)
