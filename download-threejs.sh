#!/bin/bash

# Three.js 文件下载脚本
echo "🚀 开始下载 Three.js 文件..."

# 创建目录
mkdir -p assets/js

# 下载 Three.js 主库
echo "📥 下载 three.min.js..."
curl -L -o assets/js/three.min.js https://cdnjs.cloudflare.com/ajax/libs/three.js/0.178.0/three.min.js

if [ $? -eq 0 ]; then
    echo "✅ three.min.js 下载成功"
else
    echo "❌ three.min.js 下载失败，尝试备用源..."
    curl -L -o assets/js/three.min.js https://unpkg.com/three@0.178.0/build/three.min.js
    if [ $? -eq 0 ]; then
        echo "✅ three.min.js 从备用源下载成功"
    else
        echo "❌ three.min.js 下载失败"
        exit 1
    fi
fi

# 下载 OrbitControls
echo "📥 下载 OrbitControls.js..."
curl -L -o assets/js/OrbitControls.js https://cdnjs.cloudflare.com/ajax/libs/three.js/0.178.0/OrbitControls.js

if [ $? -eq 0 ]; then
    echo "✅ OrbitControls.js 下载成功"
else
    echo "❌ OrbitControls.js 下载失败，尝试备用源..."
    curl -L -o assets/js/OrbitControls.js https://unpkg.com/three@0.178.0/examples/js/controls/OrbitControls.js
    if [ $? -eq 0 ]; then
        echo "✅ OrbitControls.js 从备用源下载成功"
    else
        echo "❌ OrbitControls.js 下载失败"
        exit 1
    fi
fi

# 检查文件大小
echo "📊 检查文件大小..."
ls -lh assets/js/

echo "🎉 所有文件下载完成！"
echo "现在可以访问以下页面："
echo "- http://localhost:4000/3d-room-local.html (本地版本)"
echo "- http://localhost:4000/3d-room.html (CDN版本)" 