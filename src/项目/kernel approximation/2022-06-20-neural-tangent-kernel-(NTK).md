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



数学知识：

1. ![image-20220622163321364](2022-06-20-neural-tangent-kernel-(NTK).assets/image-20220622163321364.png)

   其中第一个等式来自第二个性质，第二个等式来自第一个性质，而 ![[公式]](https://www.zhihu.com/equation?tex=%5CTheta_%5Cinfty%28X%2CX%29) 就是那位deterministic的Kerenl。

   于是网络输出函数的动力学方程变为：

   ![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B%5Cpartial+f_t%28%5Ctheta%2C+x%29%7D%7B%5Cpartial+t%7D+%3D++-+%5Ceta+%5CTheta_%5Cinfty%28x%2CX%29+%5Cnabla_%7Bf_t%28%5Ctheta%2CX%29%7D+%5Cmathcal%7BL%7D)

   假设loss function是我们常见的Mean squared loss，那么方程进一步化简为一个线性常微分方程（ODE）：

   ![image-20220622163732369](2022-06-20-neural-tangent-kernel-(NTK).assets/image-20220622163732369.png)
   
   当将函数一阶泰勒展开并保留一阶时，和上面ode等价，所以可以认为是一阶线性模型。