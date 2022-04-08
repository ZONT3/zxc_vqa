from argparse import ArgumentParser
p = ArgumentParser()


p.add_argument('--train', action='store_true', help="Do train")
p.add_argument('--test', action='store_true', help="Do test")
p.add_argument('--val', action='store_true', help="Do val")

p.add_argument('--ds_feats', type=str, default=None,
               help='Dataset image features file [.pt] (ignores ds_img_dir if set)')
p.add_argument('--ds_img_dir', type=str, default=None, help='Dataset raw images dir [*.png]')
p.add_argument('--ds_text', type=str, default=None, help='Dataset text data [.json]')


def parse_args(src=None):
    return p.parse_args(src)
