from zxc.modeling.zxc_model import ZXCModel

from .zxc_dataset import Dataset


class VQA:
    """
    Класс для работы с моделью ZXCModel и датасетом.
    Здесь определены методы обучения и обработки результатов
    """

    def __init__(self, args):
        self.args = args
        self.dataset = Dataset(args)
        self.model = ZXCModel(args)

    def train(self):
        pass

    def val(self):
        pass

    def test(self):
        pass
