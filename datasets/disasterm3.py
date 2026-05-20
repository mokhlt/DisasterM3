import json
from pathlib import Path
from .base import BaseDataset

class DisasterM3Dataset(BaseDataset):
    """
    Basic DisasterM3 dataset loader.

    This loader reads a JSON or JSONL annotation file and returns samples
    in a common format that can be used by the rest of the framework.
    """

    def __init__(self, data_path):
        self.data_path = Path(data_path)
        self.samples = []

    def load(self):
        if not self.data_path.exists():
            raise FileNotFoundError(f"Data file not found: {self.data_path}")

        if self.data_path.suffix == ".json":
            with open(self.data_path, "r", encoding="utf-8") as file:
                data = json.load(file)

        elif self.data_path.suffix == ".jsonl":
            data = []
            with open(self.data_path, "r", encoding="utf-8") as file:
                for line in file:
                    data.append(json.loads(line))

        else:
            raise ValueError("Only .json and .jsonl files are supported for now.")

        if isinstance(data, dict):
            data = data.get("data", data.get("samples", []))

        self.samples = []

        for item in data:
            sample = {
                "image_path": item.get("image_path") or item.get("image"),
                "question": item.get("question") or item.get("prompt"),
                "answer": item.get("answer") or item.get("ground_truth"),
                "task_type": item.get("task_type") or item.get("task"),
                "metadata": item,
            }

            self.samples.append(sample)
        return self.samples