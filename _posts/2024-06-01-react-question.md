---
layout: post
title: "react问题汇总"
date: 2023-09-12
categories: [其他]
tags: [react,nextjs]
author: zhangshuming
---

# 2024-06-01 手动添加script标签没有被渲染的问题

手动添加google检测工具
```
        {/* Google Analytics 脚本 */}
        <Script
          src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"
          strategy="afterInteractive"
        />
        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-XXXXXXXXXX');
          `}
        </Script>
```
nextjs 的script是服务端动态添加的，没有被渲染也正常