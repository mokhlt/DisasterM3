import json
from .base import BaseDataset
class EarthVQADataset(BaseDataset):
    def __init__(self, data_path):
        self.data_path = data_path

    def load(self):
        with open(self.data_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        samples = []

        for item in data:
            sample = {
                "image_path": item.get("image"),
                "question": item.get("question"),
                "answer": item.get("answer"),
                "task_type": "vqa",
            }

            samples.append(sample)

        return samples