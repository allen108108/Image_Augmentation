Image Augmentation Pyhton Library
===
###### tags: `README`

Getting Started
---

This Repository can help us to facilitate image data augment and we can deploy this lib on any computer vision task. If you want to train a deep learning model for image classification or object detection data augmentation will make your model more robust.


Requirements
---

* Python
* Open CV
* Numpy


Usage
---

First, git this repo to local

```
$ git clone https://github.com/allen108108/Image_Augmentation.git
$ cd Image_Augmentation
```

`src` is the images source folder, and this is necessary parameter.In the source images, you can give a propotion `-f` to dicide how much images you want to augment.

Finally, check what augmentation type that you want : 
(Note : `-hf`, `-vf`, `-cs`, `-hs` or `vs` that you must choose only one type. )


```
$ python run.py
  -h, --help  show this help message and exit
   src        image src path
  -f F        proportion of augmentation 
  -hf         Horizontal Flip
  -vf         Vertical Flip
  -cs         Color Shift
  -hs         Horizontal Shift
  -vs         Vertical Shift
```

The augmented images saved in `./augmention/<augment type>`. You can change the location in  `run.py`.