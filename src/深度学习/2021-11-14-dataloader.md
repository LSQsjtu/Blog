---
layout: post
title: dataloader
slug: model.train
date: 2021-11-14
status: publish
author: 刘胜琪
categories: 
  - 默认分类
tags: 
  - 深度学习
excerpt: 自己需要提升基础代码知识
---

**dataloader**

# 参数含义

1、dataset：（数据类型 dataset）

输入的数据类型。看名字感觉就像是数据库，C#里面也有dataset类，理论上应该还有下一级的datatable。这应当是原始数据的输入。PyTorch内也有这种数据结构。这里先不管，估计和C#的类似，这里只需要知道是输入数据类型是dataset就可以了。

2、batch_size：（数据类型 int）

每次输入数据的行数，默认为1。PyTorch训练模型时调用数据不是一行一行进行的（这样太没效率），而是一捆一捆来的。这里就是定义每次喂给神经网络多少行数据，如果设置成1，那就是一行一行进行（个人偏好，PyTorch默认设置是1）。

3、shuffle：（数据类型 bool）

洗牌。默认设置为False。在每次迭代训练时是否将数据洗牌，默认设置是False。将输入数据的顺序打乱，是为了使数据更有独立性，但如果数据是有序列特征的，就不要设置成True了。

4、collate_fn：（数据类型 callable，没见过的类型）

将一小段数据合并成数据列表，默认设置是False。如果设置成True，系统会在返回前会将张量数据（Tensors）复制到CUDA内存中。（不太明白作用是什么，就暂时默认False）

5、batch_sampler：（数据类型 Sampler）

批量采样，默认设置为None。但每次返回的是一批数据的索引（注意：不是数据）。其和batch_size、shuffle 、sampler and drop_last参数是不兼容的。我想，应该是每次输入网络的数据是随机采样模式，这样能使数据更具有独立性质。所以，它和一捆一捆按顺序输入，数据洗牌，数据采样，等模式是不兼容的。

6、sampler：（数据类型 Sampler）

采样，默认设置为None。根据定义的策略从数据集中采样输入。如果定义采样规则，则洗牌（shuffle）设置必须为False。

7、num_workers：（数据类型 Int）

工作者数量，默认是0。使用多少个子进程来导入数据。设置为0，就是使用主进程来导入数据。注意：这个数字必须是大于等于0的，负数估计会出错。

8、pin_memory：（数据类型 bool）

内存寄存，默认为False。在数据返回前，是否将数据复制到CUDA内存中。

9、drop_last：（数据类型 bool）

丢弃最后数据，默认为False。设置了 batch_size 的数目后，最后一批数据未必是设置的数目，有可能会小些。这时你是否需要丢弃这批数据。

10、timeout：（数据类型 numeric）

超时，默认为0。是用来设置数据读取的超时时间的，但超过这个时间还没读取到数据的话就会报错。 所以，数值必须大于等于0。

11、worker_init_fn（数据类型 callable，没见过的类型）

子进程导入模式，默认为Noun。在数据导入前和步长结束后，根据工作子进程的ID逐个按顺序导入数据。

