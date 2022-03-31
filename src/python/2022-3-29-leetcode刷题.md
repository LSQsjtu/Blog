---
layout: post
title: leetcode刷题
slug: leetcode
date: 2022-3-29
status: publish
author: 刘胜琪
categories: 
  - 默认分类
tags: 
  - 刷题
excerpt: 犯过的错误
---

**Python**

1. list.extend返回null，直接修改原list，append是将list整个放在末尾



**Python数据结构学习**

==堆== import ==heapq==

heappush(heap, item): 将 *item* 的值加入 *heap* 中，保持堆的不变性。

heappop(heap): 弹出并返回 *heap* 的最小的元素，保持堆的不变性。如果堆为空，抛出 [`IndexError`](https://docs.python.org/zh-cn/3/library/exceptions.html#IndexError) 。使用 `heap[0]` ，可以只访问最小的元素而不弹出它。

优先队列（SortedList）