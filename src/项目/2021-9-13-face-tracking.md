---
layout: post
title: face tracking
slug: face tracking
date: 2021-9-13
status: publish
author: 刘胜琪
categories: 
  - 默认分类
tags: 
  - 深度学习
excerpt: 项目学习
---

**face tracking**

模型生成的tensor要去除求导属性，.detach()之后再用于可视化



2D动漫脸的关键点手工标记，不用标记嘴巴和鼻子，用3D模型的2D投影去fitting，刚好取脸颊和眼睛的点去fitting



设计两个网络，前面一个叫encoder，生成latent code再进入decoder，生成output



开会讨论时接触了许多新的一些知识，但都没有自己插手的地方，自己目前还是没有能力独立承担工程中的任何任务，讨论创新点时更多的是以写论文讲故事的方面去讨论，工程能力上的实现多半是因为网络模型本身结构的能力和泛化训练的效果有关，无法做到突破性进展，更多的是工程上的效果。



从landmark的标记数据集，训练方法，学习id、exp和最后的texture，保存文件的格式和方法，最后便是渲染的一些基本知识，二次元作画的风格。



texture指的是纹理（颜色形状之类的），材质指的是反射吸收光线的强弱之类的