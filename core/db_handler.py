## Folder: core
# File: db_handler.py

import pyodbc
from config.settings import DB_CONN_STRING
from utils.helpers import logger, format_date

class DBHandler:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(DB_CONN_STRING)
            self.cursor = self.conn.cursor()
            logger.info("Database connection established successfully.")
        except Exception as e:
            logger.exception("Failed to connect to the database.")
            self.conn = None
            self.cursor = None

    def insert_activity(self, module: str, message: str, status: str = "OK"):
        if not self.cursor:
            logger.error("No active DB connection to insert activity.")
            return False

        query = """
        INSERT INTO ActivityLog (module, message, status, created_at)
        VALUES (?, ?, ?, ?)
        """
        try:
            self.cursor.execute(query, (module, message, status, format_date()))
            self.conn.commit()
            logger.info(f"Activity logged: {module} - {status}")
            return True
        except Exception as e:
            logger.exception("Failed to insert activity log.")
            return False

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            logger.info("Database connection closed.")
        except Exception as e:
            logger.warning("Issue during DB close.")


# Example usage:
# db = DBHandler()
# db.insert_activity("db_handler", "Test insert log")
# db.close()