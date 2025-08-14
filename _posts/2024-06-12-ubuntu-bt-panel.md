---
layout: post
title: "Ubuntu 安装宝塔面板教程"
date: 2024-06-12
categories: [后端]
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

## 宝塔面板常用命令

### 启动宝塔面板

```bash
sudo bt start
```

### 停止宝塔面板

```bash
sudo bt stop
```

### 重启宝塔面板

```bash
sudo bt restart
```

### 查看面板状态

```bash
sudo bt status
```

### 查看面板信息

```bash
sudo bt default
```

### 修改面板端口

```bash
sudo bt 14
```

### 修改面板密码

```bash
sudo bt 5
```

### 卸载宝塔面板

```bash
sudo bt uninstall
```

### 查看面板日志

```bash
sudo bt 22
```

### 修复面板

```bash
sudo bt repair
```

### 更新面板

```bash
sudo bt update
```

## 常见问题
7月28日宝塔无法正常运行，因为误删了配置文件
运行报错缺少配置文件


###解决 强制重新安装
```
if [ -f /usr/bin/curl ];then curl -sSO https://download.bt.cn/install/install_panel.sh;else wget -O install_panel.sh https://download.bt.cn/install/install_panel.sh;fi;bash install_panel.sh
```
