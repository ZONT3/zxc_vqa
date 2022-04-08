from .zxc_text import ZXCText
from .zxc_vision import ZXCVision

import zxc.util.modeling as zm


class ZXCModel(zm.Module):
    def __init__(self, args):
        super().__init__(args)
        self.vision = ZXCVision(args)
        self.text = ZXCText(args)
