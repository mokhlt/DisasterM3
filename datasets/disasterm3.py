from .base import BaseDataset
class DisasterM3Dataset(BaseDataset):
    def __init__(self, data_path):
        self.data_path = data_path

    def load(self):
        """
        This is where DisasterM3 loading logic would be added.

        For now, this returns an empty list as a simple starting point.
        """
        samples = []

        return samples