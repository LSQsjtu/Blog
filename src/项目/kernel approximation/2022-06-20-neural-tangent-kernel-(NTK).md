---
layout: post
title: neural tangent kernel (NTK)
slug: neural tangent kernel (NTK)
date: 2022-06-20
status: publish
author: 刘胜琪
categories: 
  - 默认分类
tags: 
  - 深度学习
excerpt: 暑期专业实习
---

**neural tangent kernel (NTK)**

观点：

1. NTK在无限宽极限下趋于一个确定的核(Kernel)，在无限宽极限下不随着时间变化，而且在梯度下降的训练过程中保持不变，因此==无限宽网络==的输出层结果的动力学可以用一个常微分方程来表示。
2. 无限宽的神经网络等价于高斯过程
3. Mean field Theory中存在超参数平面中的一条临界线
4. ![image-20220620212719766](2022-06-20-neural-tangent-kernel-(NTK).assets/image-20220620212719766.png)
5. ==引入NTK parameterziation==，是因为LeCun参数化会导致NTK在无限宽极限下发散。



提出的问题困难：

1. NTK在有限宽网络会失效：**有限宽度到无穷的NTK演变问题**