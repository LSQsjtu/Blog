---
layout: post
title: 3D Tracking on NuScences
slug: 3DtrackingOnNuScences
date: 2021-9-17
status: publish
author: 刘胜琪
categories: 
  - 默认分类
tags: 
  - 深度学习
excerpt: 项目学习
---

**3D Tracking on NuScences**

detection loss采用Focal loss

Focal Loss 就是一个解决**分类问题中类别不平衡、分类难度差异**的一个 loss。



​	Cameras provide a dense and rich visual signal that helps to localize even distant objects. LiDAR provide a sparse signal in 3D space.



给跟踪结果打上ID标签，后通过坐标获取相对应的真值

现在的想法：

1. 给检测结果每个物体打上对应真值的token
2. 根据官方库的方法进行真值标注

10-31讨论结果

- [ ] 不归一化

- [x] 跟踪网络自己的特征提取:无法表示存储

  ![](2021-9-17-3D-Tracking-on-NuScences.assets/image-20211113101736628.png)

- [ ] 不加速度

- [x] sigmoid归一化0-1



更改为新的数据dict输入新的网络



给detection score设置一个阈值

data["coors"]还是有问题多出来的一个维度信息
