from .zxc_text import ZXCText
from .zxc_vision import ZXCVision

import zxc.util.modeling as zm


class ZXCModel(zm.Module):
    """
    Итоговая модель VQA
    Здесь все модули собираются воедино
    и определена архитектура "головы" модели.
    """

    def __init__(self, args):
        super().__init__(args)
        self.vision = ZXCVision(args)
        self.text = ZXCText(args)


class ZXCXModal(zm.Module):
    """
    Модуль кросс-модальности.
    Оперирует текстовыми и визуальными данными,
    возвращая их объединение.
    """

    def __init__(self, args):
        super().__init__(args)

    def forward(self, visual_data, text_data):
        pass
