class BaseDataset:
    """
    Basic dataset interface.

    Any dataset loader should have a load() method.
    """

    def load(self):
        raise NotImplementedError("Each dataset must implement its own load method.")