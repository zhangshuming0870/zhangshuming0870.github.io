---
layout: 3d-room-local
title: 韩国短剧《闹钟》风格3D房间 - 本地版本
---

这是一个使用本地Three.js文件的3D房间场景，灵感来源于韩国短剧《闹钟》中主人公的房间布局。

## 房间特色

- 🏠 温馨的小房间布局
- 🛏️ 舒适的床铺和枕头  
- 💻 学习工作区域
- 📚 书架和装饰品
- 🌱 绿色植物点缀
- ⏰ 动态闹钟显示
- 📱 手机通知闪烁
- 💡 温暖的台灯光照

## 控制说明

- 🖱️ 鼠标左键：旋转视角
- 🔍 鼠标滚轮：缩放
- 📱 鼠标右键：平移
- 🔄 自动旋转：按空格键

## 技术特点

- **本地文件**：使用本地Three.js文件，避免CDN问题
- **响应式设计**：适配不同屏幕尺寸
- **真实光照**：包含环境光和方向光
- **阴影渲染**：所有物体都有真实的阴影效果
- **交互控制**：完整的鼠标和键盘控制

## 文件要求

请确保以下文件存在于 `assets/js/` 目录：
- `three.min.js` - Three.js主库文件
- `OrbitControls.js` - 轨道控制器文件

## 下载文件

如果文件不存在，请使用以下命令下载：

```bash
# 下载Three.js
curl -o assets/js/three.min.js https://cdnjs.cloudflare.com/ajax/libs/three.js/0.178.0/three.min.js

# 下载OrbitControls
curl -o assets/js/OrbitControls.js https://cdnjs.cloudflare.com/ajax/libs/three.js/0.178.0/OrbitControls.js
``` 