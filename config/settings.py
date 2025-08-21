## Folder: config
# File: settings.py

from datetime import datetime

# --- Project Timeline Settings ---
START_DATE = datetime(2025, 6, 1)  # Define when to start simulating commits
TOTAL_DAYS = 7  # Number of days to simulate daily project work

# --- Repository Settings ---
REPO_PATH = "C:/Users/YourName/Projects/AutoGitRepo"  # Local repo path to automate
GIT_USERNAME = "your-username"  # Git username to configure for commits
GIT_EMAIL = "your-email@example.com"  # Git email to configure for commits

# --- Database Connection ---
DB_CONN_STRING = (
    "Driver={SQL Server};"
    "Server=YOUR_SERVER;"
    "Database=AutoGitDB;"
    "Trusted_Connection=yes;"
)  # SQL Server string to log task activities

# --- Task Mapping ---
TASK_MAPPING = {
    0: "init_config",       # Day 0: Setup base config and project layout
    1: "db_setup",          # Day 1: Create SQL tracking models
    2: "logging_engine",    # Day 2: Implement logging features
    3: "file_changes",      # Day 3: Simulate file edits
    4: "git_commits",       # Day 4: Apply commits & pushes
    5: "ai_commit_msgs",    # Day 5: Generate AI messages
    6: "final_wrap_up"       # Day 6: Documentation & polish
}  # Map days to task modules
