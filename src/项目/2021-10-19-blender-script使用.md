---
layout: post
title: blender script使用
slug: blender_script
date: 2021-10-19
status: publish
author: 刘胜琪
categories: 
  - 默认分类
tags: 
  - 工具
excerpt: 项目学习
---

**blender script**

将blender中所有的button转换为代码接口，操纵物体

重要学习数据类型：bpy

bpy.data.object：打开的模型物体

Data is added and removed via methods on the collections in [`bpy.data`](https://docs.blender.org/api/current/bpy.data.html#module-bpy.data)

 “poll” function which checks if the cursor is in a valid area or if the object is in the correct mode ：判断是否选择正确的操作方式