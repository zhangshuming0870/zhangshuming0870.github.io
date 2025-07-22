---
layout: post
title: "Ubuntu 安装宝塔面板教程"
date: 2024-06-12
categories: [Linux, 运维]
tags: [宝塔, Ubuntu, 面板, 运维]
author: zhangshuming
---

# Ubuntu 安装宝塔面板教程

## 目录

1. [宝塔面板简介](#宝塔面板简介)
2. [安装前准备](#安装前准备)
3. [安装步骤](#安装步骤)
4. [常见问题](#常见问题)

---

## 宝塔面板简介

宝塔面板是一款简单好用的服务器运维管理面板，支持一键部署 LNMP/LAMP、网站、数据库、FTP 等，极大简化了服务器管理。

## 安装前准备

- 一台已安装 Ubuntu 系统的服务器（建议 Ubuntu 18.04/20.04/22.04）
- 拥有 root 权限
- 保证服务器联网

## 安装步骤

### 1. 更新系统

```
sudo apt update && sudo apt upgrade -y
```

### 2. 安装 curl（如未安装）

```
sudo apt install curl -y
```

### 3. 一键安装宝塔面板

```
curl -sSO http://download.bt.cn/install/install_ubuntu.sh && sudo bash install_ubuntu.sh
```

安装过程中会提示设置面板端口、账号和密码，请根据提示操作。

### 4. 访问面板

安装完成后，终端会输出面板的访问地址、账号和密码。

在浏览器中访问：

```
http://服务器IP:8888
```

用终端输出的账号和密码登录即可。

## 常见问题

- **面板无法访问**：检查服务器安全组/防火墙是否放行 8888 端口。
- **安装失败**：建议重试或更换网络环境。
- **面板安全**：安装后请及时修改默认账号密码，并开启面板安全设置。

---
