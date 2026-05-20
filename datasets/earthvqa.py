from .base import BaseDataset
class EarthVQADataset(BaseDataset):
    def __init__(self, data_path):
        self.data_path = data_path

    def load(self):
        """
        This is where EarthVQA loading logic would be added.

        For now, this returns an empty list as a simple starting point.
        """
        samples = []

        return samples