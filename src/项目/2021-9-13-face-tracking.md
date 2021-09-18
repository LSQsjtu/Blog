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