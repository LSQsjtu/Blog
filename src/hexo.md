---
layout: post
title: 5月8日上午小结
slug: conclude
date: 2021-5-8
status: publish
author: 刘胜琪
categories: 
  - 默认分类
tags: 
  - 博客
excerpt: 又急起来了
---

# 事情记录

1. 尝试使用Hexo，使用新的主题fluid
2. 更改GitHub action（失败😥连接出错😖）
3. hexo生成文章的步骤不清楚
4. .ssh生成有问题

## 解决方法

1. 不使用hexo
2. 继续了解GitHub action机制

自己不能太着急，找到自己喜欢的东西，认真记录生活每一天。

![](https://im0-tub-com.yandex.net/i?id=2c27f5792796367ec0725562281747d6&n=13)

## 记录hexo使用方法

1. ```bash
   $ hexo init [folder]
   ```

   新建一个网站。如果没有设置 `folder` ，Hexo 默认在目前的文件夹建立网站。

2. ```bash
   $ hexo new [layout] <title>
   ```

   新建一篇文章。如果没有设置 `layout` 的话，默认使用 [_config.yml](https://hexo.io/zh-cn/docs/configuration) 中的 `default_layout` 参数代替。如果标题包含空格的话，请使用引号括起来。

   | 参数              | 描述                                          |
   | :---------------- | :-------------------------------------------- |
   | `-p`, `--path`    | 自定义新文章的路径                            |
   | `-r`, `--replace` | 如果存在同名文章，将其替换                    |
   | `-s`, `--slug`    | 文章的 Slug，作为新文章的文件名和发布后的 URL |

3. ```bash
   $ hexo generate
   ```

   | 选项                  | 描述                                                         |
   | :-------------------- | :----------------------------------------------------------- |
   | `-d`, `--deploy`      | 文件生成后立即部署网站                                       |
   | `-w`, `--watch`       | 监视文件变动                                                 |
   | `-b`, `--bail`        | 生成过程中如果发生任何未处理的异常则抛出异常                 |
   | `-f`, `--force`       | 强制重新生成文件 Hexo 引入了差分机制，如果 `public` 目录存在，那么 `hexo g` 只会重新生成改动的文件。 使用该参数的效果接近 `hexo clean && hexo generate` |
   | `-c`, `--concurrency` | 最大同时生成文件的数量，默认无限制                           |

   **总结**

   使用hexo生成静态博客，调用命令过多，造成时间浪费，主题自己以后有时间可以尝试更改主题样式，使博客更美观，现在已经够用了

