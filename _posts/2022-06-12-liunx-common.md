---
layout: post
title: "liunx 常见问题"
date: 2022-01-03
categories: [其他]
tags: [liunx, 常见问题]
author: zhangshuming
---

# liunx 常见问题记录

## 目录

1. [端口占用](#端口占用)
2. [docker](#docker)

---

## 端口占用

### 查看某个端口占用
   ```
ps lf -80
   ```

### 解决端口占用
   ```
kill -9 pid
   ```

## docker
### docker 查看docker容器
```
docker ps
```
![端口占用查看示例](/assets/liunx-common/Snipaste_2025-07-11_10-43-04.png)

### 进入某个容器
