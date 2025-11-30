import json
from datetime import datetime

class Logger:
    def __init__(self, filename="ai_study_planner.log"):
        self.filename = filename

    def log(self, event, details):
        entry = {
            "time": datetime.now().isoformat(timespec="seconds"),
            "event": event,
            "details": details,
        }
        with open(self.filename, "a") as f:
            f.write(json.dumps(entry) + "\n")

