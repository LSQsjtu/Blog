---
layout: post
title: Centerpoint based 3D Tracking
slug: 3Dtracking
date: 2021-9-17
status: publish
author: 刘胜琪
categories: 
  - 默认分类
tags: 
  - 深度学习
excerpt: 项目学习
---

**Centerpoint**

voxel网络结构和输出tensor形状

reader：type="VoxelFeatureExtractorV3",

输入torch.Size([110066, 10, 5])"features"， torch.Size([110066])"num_voxels"，输出torch.Size([82289, 5])



backbone：type="SpMiddleResNetFHD"

输入torch.Size([82289, 5])，torch.Size([82345, 4]) coordinate，batch_size:1，data[input_shape]：[1440 1440   40]，输出x.shape：torch.Size([1, 256, 180, 180])，{'conv1': <spconv.SparseConvTensor object at 0x7f8f56e68ef0>, 'conv2': <spconv.SparseConvTensor object at 0x7f8f56e68b70>, 'conv3': <spconv.SparseConvTensor object at 0x7f8f56e68f98>, 'conv4': <spconv.SparseConvTensor object at 0x7f8f56e68d30>} voxel_feature



neck：type="RPN"

输入x.shape：torch.Size([1, 256, 180, 180])，输出x.shape：torch.Size([1, 512, 180, 180])



bbox_head：type="CenterHead"

输入x.shape：torch.Size([1, 512, 180, 180])，输出list为

**[**

**{'reg': tensor([1, 2, 180, 180]), 'height': tensor([1, 1, 180, 180]), 'dim': tensor([1, 3, 180, 180]), 'rot': tensor([1, 2, 180, 180]), 'vel': tensor([1, 2, 180, 180]), 'hm': tensor()},** 

**{'reg': tensor([1, 2, 180, 180]), 'height': tensor([1, 1, 180, 180]), 'dim': tensor([1, 3, 180, 180]), 'rot': tensor([1, 2, 180, 180]), 'vel': tensor([1, 2, 180, 180]), 'hm': tensor()},** 

**{'reg': tensor([1, 2, 180, 180]), 'height': tensor([1, 1, 180, 180]), 'dim': tensor([1, 3, 180, 180]), 'rot': tensor([1, 2, 180, 180]), 'vel': tensor([1, 2, 180, 180]), 'hm': tensor()},**

 **{'reg': tensor([1, 2, 180, 180]), 'height': tensor([1, 1, 180, 180]), 'dim': tensor([1, 3, 180, 180]), 'rot': tensor([1, 2, 180, 180]), 'vel': tensor([1, 2, 180, 180]), 'hm': tensor()},** 

**{'reg': tensor([1, 2, 180, 180]), 'height': tensor([1, 1, 180, 180]), 'dim': tensor([1, 3, 180, 180]), 'rot': tensor([1, 2, 180, 180]), 'vel': tensor([1, 2, 180, 180]), 'hm': tensor()},** 

**{'reg': tensor([1, 2, 180, 180]), 'height': tensor([1, 1, 180, 180]), 'dim': tensor([1, 3, 180, 180]), 'rot': tensor([1, 2, 180, 180]), 'vel': tensor([1, 2, 180, 180]), 'hm': tensor([1, 2, 180, 180])}**

**]**

```python
tasks = [
    dict(num_class=1, class_names=["car"]),
    dict(num_class=2, class_names=["truck", "construction_vehicle"]),
    dict(num_class=2, class_names=["bus", "trailer"]),
    dict(num_class=1, class_names=["barrier"]),
    dict(num_class=2, class_names=["motorcycle", "bicycle"]),
    dict(num_class=2, class_names=["pedestrian", "traffic_cone"]),
]
```

六种种类一个batch_size

猜想输出为regression，height-above-ground，dimension，rotation，velocity，heat-map

