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

blender文件夹下scripts/startup/中有python的环境

When a script is imported as a module, its class instances will remain inside the module and can be accessed later on by importing that module again.

run the script：

> blender --python /home/me/my_script.py

While `__init__()` and `__del__()` will be called if defined, the class instances lifetime only spans the execution. 

数据保存为blender.data的格式，下次开启不会丢失

The register/unregister calls are used so it’s possible to toggle add-ons and reload scripts while Blender runs

每次重新跑，估计得重新加载选项