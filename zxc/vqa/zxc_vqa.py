from .zxc_dataset import Dataset


class VQA:
    def __init__(self, args):
        self.args = args
        self.dataset = Dataset(args)

    def train(self):
        pass

    def val(self):
        pass

    def test(self):
        pass
