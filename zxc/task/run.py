"""
Файл запуска проекта
"""

import zxc.task.arg as arg
from zxc.vqa.zxc_vqa import VQA

if __name__ == '__main__':
    args = arg.parse_args()
    vqa = VQA(args)

    if args.train:
        vqa.train()

    elif args.test:
        vqa.test()

    elif args.val:
        vqa.val()
