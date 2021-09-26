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

reader：type="VoxelFeatureExtractorV3",取平均

输入torch.Size([体素数, 10, 5])"features"， torch.Size([体素数])"num_voxels"，输出torch.Size([体素数, 5])input_features



backbone：type="SpMiddleResNetFHD"

输入torch.Size([体素数, 5])，torch.Size([体素数, 4]) coordinate[0,位置坐标]，batch_size:1，data[input_shape]：[1440 1440   40]，输出x.shape：torch.Size([1, 256, 180, 180])，{'conv1': <spconv.SparseConvTensor object at 0x7f8f56e68ef0>, 'conv2': <spconv.SparseConvTensor object at 0x7f8f56e68b70>, 'conv3': <spconv.SparseConvTensor object at 0x7f8f56e68f98>, 'conv4': <spconv.SparseConvTensor object at 0x7f8f56e68d30>} voxel_feature



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

H,W为180

batch_box_preds：tensor[(1, 32400, 9)]，32400=180*180，9=xs(1)+ys(1)+batch_hei(1)+batch_dim(3)+batch_vel(2)+batch_rot(1)



dataloader处理后的数据为{'metadata': {'image_prefix': PosixPath('data/nuScenes'), 'num_point_features': 5, 'token': 'e411f0ab3a0243f1bea593bed340894f'}, 'points':（点数，5）, 'voxels'（体素数，10，5）:'shape': array([1440, 1440,   40]), 'num_points': 表示每个体素中的点云数量), 'num_voxels': 体素数), 'coordinates': (体素数，3)array([[ 16, 717, 682],
       [ 16, 717, 680],
       [ 16, 717, 678],
       ...,
       [ 28, 701, 636],
       [ 28, 701, 641],
       [ 28, 702, 638]], dtype=int32)}

每个体素最多10个点

NuScenes数据集中lidar文件名用时间戳区分文件

![](2021-9-17-Centerpoint-based-3D-Tracking.assets/image-20210919105257159-16320199793771.png)

```txt
汽车编号-时间-相机位置-时间戳.jpg
汽车编号-时间-雷达位置-时间戳.pcd.bin
```

 'num_point_features'：前4个是点feature，一般是xyz和反射率，后一个是时间信息

‘feature_map_size’：180*180

for i，data in enumerate（dataloader）：一次性导入num_work个batch



data中point是10个lidar文件中的点拼接在一起，第一个文件读入的为最大的时间戳

Sparse Convolution成功用于3D目标检测的网络，相比于3D Convolution，在运算速度和显存消耗中有巨大的优势。

python前r表示禁止转义



backbone中对于feature进行卷积，体素数减少，最后dense生成密集要求size的vector

output的结果

```json
[{'box3d_lidar': tensor([[ 9.5765e-01, -8.1574e+00, -1.1584e+00,  ...,  2.3936e-01,
          1.7465e+00, -3.0140e+00],
        [ 1.0656e+01,  2.0182e+01,  2.1907e-02,  ...,  1.6337e+00,
          1.6447e+00, -2.3173e+00],
        [ 3.9706e-01, -3.0798e+01, -1.4518e+00,  ..., -1.4510e-01,
          4.8273e+00, -3.1372e+00],
        ...,
        [ 2.1409e+00,  2.1294e+01, -6.0946e-02,  ...,  7.9199e-09,
          9.7809e-10, -2.8571e+00],
        [-1.5230e+01,  1.1139e+01, -6.7530e-01,  ...,  4.3063e-03,
          1.9419e-04, -3.6318e-01],
        [-1.5802e+01, -6.9950e+00,  1.3413e+00,  ..., -4.8845e-04,
          1.7079e-03, -3.0042e+00]], device='cuda:0'), 'scores': tensor([0.8431, 0.6624, 0.5860, 0.5637, 0.3287, 0.1784, 0.1722, 0.1657, 0.1492,
        0.1128, 0.3096, 0.2991, 0.2722, 0.2451, 0.2037, 0.1750, 0.1609, 0.1528,
        0.1380, 0.1141, 0.1139, 0.1119, 0.1094, 0.1057, 0.1026, 0.1006, 0.1001,
        0.1001, 0.2855, 0.1238, 0.1084, 0.1011, 0.3027, 0.2017, 0.1995, 0.1879,
        0.1484, 0.1203, 0.1194, 0.1112, 0.1097, 0.1060, 0.1019, 0.1005, 0.3652,
        0.3497, 0.2844, 0.2724, 0.2464, 0.2014, 0.1862, 0.1774, 0.1621, 0.1597,
        0.1568, 0.1543, 0.1427, 0.1394, 0.1370, 0.1329, 0.1289, 0.1259, 0.1242,
        0.1232, 0.1224, 0.1131, 0.1129, 0.1102, 0.1082, 0.1037, 0.1033, 0.1011,
        0.1008, 0.1002, 0.1001, 0.3860, 0.3815, 0.2732, 0.2582, 0.2510, 0.2181,
        0.2094, 0.2045, 0.1980, 0.1971, 0.1832, 0.1817, 0.1743, 0.1688, 0.1662,
        0.1655, 0.1621, 0.1613, 0.1432, 0.1402, 0.1349, 0.1346, 0.1345, 0.1308,
        0.1301, 0.1300, 0.1275, 0.1198, 0.1164, 0.1160, 0.1044, 0.1038, 0.1027,
        0.1027, 0.1019, 0.1007, 0.1002], device='cuda:0'), 'label_preds': tensor([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2,
        2, 2, 2, 1, 4, 4, 4, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 6,
        7, 7, 7, 7, 6, 7, 7, 7, 7, 6, 7, 7, 7, 6, 6, 7, 6, 7, 7, 7, 7, 7, 7, 7,
        6, 6, 7, 8, 8, 8, 9, 8, 8, 8, 8, 8, 9, 9, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8,
        9, 8, 9, 8, 8, 9, 8, 8, 9, 8, 8, 8, 9, 9, 8, 8], device='cuda:0'), 'metadata': {'image_prefix': PosixPath('data/nuScenes'), 'num_point_features': 5, 'token': 'b4b81cfd5d734881ad386e5c2b00ed4a'}}]
```

使用token对应相关的图片，主要看create_date时对数据集做的处理，每个数据有对应的lidar_path和info[“sweeps”]包含9个另外的雷达数据文件，邻近的
