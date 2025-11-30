import json
import os

class LongTermMemory:
    def __init__(self, filename="user_profiles.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f)

    def load_all(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_all(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_profile(self, name):
        data = self.load_all()
        return data.get(name)

    def save_profile(self, name, profile):
        data = self.load_all()
        data[name] = profile
        self.save_all(data)

