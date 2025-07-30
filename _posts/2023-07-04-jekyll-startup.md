---
layout: post
title: "Jekyll 本地启动常见问题与解决全记录"
date: 2023-07-04
categories: [其他]
tags: [jekyll, Ruby, rbenv, bundler, 折腾记录, 环境配置]
excerpt: '记录一次在 macOS 上本地启动 Jekyll 博客遇到 Ruby 版本、bundler 依赖等问题的完整排查与解决过程，适合新手参考。'
---

# Jekyll 本地启动常见问题与解决全记录

> 本文记录了在 macOS 上本地启动 Jekyll 博客时遇到的 Ruby 版本、bundler 依赖等问题的完整排查与解决过程，适合新手参考。

## 1. 问题现象

在终端执行 `bundle install` 时，报错如下：

```
Could not find 'bundler' (2.6.9) required by your Gemfile.lock.
To install the missing version, run `gem install bundler:2.6.9`
```

尝试安装 bundler 2.6.9，又遇到如下报错：

```
There are no versions of bundler (= 2.6.9) compatible with your Ruby & RubyGems
bundler requires Ruby version >= 3.1.0. The current ruby version is 2.6.10.210.
```

## 2. 原因分析

macOS 自带的 Ruby 版本较低（2.6.10），而项目依赖的 bundler 2.6.9 需要 Ruby >= 3.1.0。

**直接升级系统 Ruby 可能影响 macOS 系统工具，推荐用 rbenv 管理多版本 Ruby，互不干扰。**

## 3. 解决步骤

### 3.1 安装 rbenv 和 ruby-build

```sh
brew install rbenv ruby-build
```

### 3.2 安装新版本 Ruby（如 3.2.2）

```sh
rbenv install 3.2.2
rbenv global 3.2.2
```

可用 `ruby -v` 验证当前 Ruby 版本：

```
ruby 3.2.2 (2023-03-30 revision e51014f9c0) [arm64-darwin24]
```

### 3.3 安装 bundler 2.6.9

```sh
gem install bundler:2.6.9
```

### 3.4 安装项目依赖

```sh
bundle install
```

### 3.5 启动 Jekyll 本地服务

```sh
bundle exec jekyll serve

```
```sh
bundle exec jekyll serve --host 0.0.0.0 --port 4000
```
终端输出：

```
Server address: http://127.0.0.1:4000
Server running... press ctrl-c to stop.
```

浏览器访问 http://127.0.0.1:4000/ 即可预览。

## 4. 其他常见报错

- `'/favicon.ico' not found.`
- `'/css/style.css' not found.`

这些是因为项目根目录下没有 favicon.ico 或 css/style.css 文件，不影响主要功能，可后续补充。

## 5. 总结

- 不要直接升级/替换系统 Ruby，推荐用 rbenv 管理多版本。
- 安装新 Ruby 后，记得用 `rbenv global` 切换并重启终端。
- 遇到依赖问题，优先检查 Ruby 版本和 bundler 版本。

希望本文对你本地启动 Jekyll 博客有所帮助！ 