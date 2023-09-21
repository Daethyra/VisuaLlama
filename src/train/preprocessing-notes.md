# How to fine tune DETR

Training procedure
Preprocessing
The exact details of preprocessing of images during training/validation can be found here.

Images are resized/rescaled such that the shortest side is at least 800 pixels and the largest side at most 1333 pixels, and normalized across the RGB channels with the ImageNet mean (0.485, 0.456, 0.406) and standard deviation (0.229, 0.224, 0.225).

Source: [{LINK}](https://huggingface.co/facebook/detr-resnet-101-panoptic#:~:text=Training%20procedure,0.229%2C%200.224%2C%200.225) "{CLICK ME BRUH}")
