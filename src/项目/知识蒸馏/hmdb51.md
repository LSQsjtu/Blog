---
layout: post
title: HMDB数据集
slug: HMDB51处理
date: 2021-7-28
status: publish
author: 刘胜琪
categories: 
  - 默认分类
tags: 
  -数据集
excerpt: HMDB51数据集
---

**HMDB51数据集**

- orgin HMDB51-About 2GB for a total of 7,000 clips distributed in 51 action classes。
- [Stabilized HMDB51](http://serre-lab.clps.brown.edu/wp-content/uploads/2013/10/hmdb51_sta.rar) – the number of clips and classes are the same as HMDB51, but there is a mask in [video_name].form associated with each clip. The mask file is readable in matlab.

除了动作标签，还有meta-label（元标签）表征片段的属性

各个方向的，前面，后面，左右方向的视频

There should be 70 videos with id 1 , 30 videos with id 2 in each txt file.

mask:ice_cream:：只有为1的才表征人

stabilized：还有matrxi表征数据集对原始图像的转换

accimage: accelerate image对PIL库的部分功能实现

hog，hof特征为处理后的光流信息特征

[PyTorch载入图片后ToTensor解读（含PIL和OpenCV读取图片对比） - 木易修 - 博客园 (cnblogs.com)](https://www.cnblogs.com/ocean1100/p/9494640.html)

totensor对于Opencv（不会除以255）和PIL.image的处理不一样

尝试[GitHub - sebastiantiesmeyer/deeplabchop3d: inflated labchop kinetic net](https://github.com/sebastiantiesmeyer/deeplabchop3d)

直接复现最高精度的结果

