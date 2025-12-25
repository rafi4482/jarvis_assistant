import json
import os

class Memory:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def add(self, role, message):
        with open(self.file_path, "r") as f:
            data = json.load(f)
        data.append({"role": role, "message": message})
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def get_history(self):
        with open(self.file_path, "r") as f:
            data = json.load(f)
        return "\n".join([f"{d['role']}: {d['message']}" for d in data])

    def clear(self):
        with open(self.file_path, "w") as f:
            json.dump([], f)
