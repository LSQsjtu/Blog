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