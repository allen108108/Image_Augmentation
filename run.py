import argparse
import os,sys
from random import sample
from utils.augmentation import h_flip_img, v_flip_img, c_shift_img, h_shift_img, v_shift_img



def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('src', help='來源圖像位址')
    parser.add_argument('-f', default=1, help='增強比例')
    group.add_argument('-hf', action='store_true', help='Horizontal Flip')
    group.add_argument('-vf', action='store_true', help='Vertical Flip')
    group.add_argument('-cs', action='store_true', help='Color Shift')
    group.add_argument('-hs', action='store_true', help='Horizontal Shift')
    group.add_argument('-vs', action='store_true', help='Vertical Shift')

    args = parser.parse_args()

    opt={v:k for k,v in vars(args).items()}
    key = opt[True]
)
    src_path = args.src
    dst_path = './augmentation/' + {'hf' : 'h_flip',
                                    'vf' : 'v_flip',
                                    'cs' : 'c_shift',
                                    'hs' : 'h_shift',
                                    'vs' : 'v_shift'}.get(key)

    frac = args.f

    if not os.path.isdir(src_path):
        print(f"DirectoryNotFound : '{src_path}' was not found, please enter a correct directory. ")
        sys.exit(0)

    if not os.path.isdir('./augmentation'):
        os.mkdir('./augmentation')

    if not os.path.isdir(dst_path):
        os.mkdir(dst_path)

    if ( frac < 0 ) or ( frac > 1 ):
        print(f"ValueError : -f must be positive float less than or equal to 1")
        sys.exit(0)

    img_paths = []

    for dpath, _, fnames in os.walk(src_path) :
        for fname in fnames :
            print(fname)
            if '.jpg' in fname or '.png' in fname or '.JPG' in fname or '.PNG' in fname:
                img_path = os.path.join(dpath, fname)
                img_paths.append(img_path)

    
    aug_num = int(len(img_paths)*frac)
    def_dict = {
        'hf' : h_flip_img,
        'vf' : v_flip_img,
        'cs' : c_shift_img,
        'hs' : h_shift_img,
        'vs' : v_shift_img
        }

    for path in sample(img_paths, aug_num):
        path = path.replace('\\', '/')
        print(path)
        def_dict[key](path, dst_path)

    print(f"Data augment done! There were  {aug_num} images be augmented.")

if __name__ == '__main__':
    main()