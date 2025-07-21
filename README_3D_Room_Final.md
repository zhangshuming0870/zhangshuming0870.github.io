# 🏠 Jekyll 3D房间项目 - 完整解决方案

这是一个在Jekyll项目中集成Three.js 3D房间的完整解决方案，包含多种加载方式。

## 📁 项目结构

```
├── _layouts/
│   ├── 3d-room.html          # CDN版本布局
│   └── 3d-room-local.html    # 本地文件版本布局
├── assets/js/
│   ├── three.min.js          # Three.js主库（需要下载）
│   └── OrbitControls.js      # 轨道控制器（需要下载）
├── 3d-room.md                # CDN版本页面
├── 3d-room-local.md          # 本地版本页面
├── _3d-room.html             # 独立HTML页面
├── test-simple.html          # 简单测试页面
├── download-threejs.sh       # 自动下载脚本
└── README_3D_Room_Final.md  # 项目说明文档
```

## 🚀 快速开始

### 方法一：使用自动下载脚本（推荐）

```bash
# 1. 给脚本执行权限
chmod +x download-threejs.sh

# 2. 运行下载脚本
./download-threejs.sh

# 3. 启动Jekyll服务器
jekyll serve

# 4. 访问页面
# http://localhost:4000/3d-room-local.html (本地版本)
# http://localhost:4000/3d-room.html (CDN版本)
```

### 方法二：手动下载文件

```bash
# 创建目录
mkdir -p assets/js

# 下载Three.js文件
curl -L -o assets/js/three.min.js https://cdnjs.cloudflare.com/ajax/libs/three.js/0.178.0/three.min.js
curl -L -o assets/js/OrbitControls.js https://cdnjs.cloudflare.com/ajax/libs/three.js/0.178.0/OrbitControls.js
```

### 方法三：使用CDN版本（无需下载）

直接访问：
- `http://localhost:4000/3d-room.html` (CDN版本)
- `http://localhost:4000/_3d-room.html` (独立HTML)

## 🎯 版本说明

### 📦 本地版本 (`3d-room-local`)
- **优点**：加载速度快，不依赖网络
- **缺点**：需要下载文件
- **适用**：生产环境，网络不稳定地区

### 🌐 CDN版本 (`3d-room`)
- **优点**：无需下载文件，自动更新
- **缺点**：依赖网络，可能加载失败
- **适用**：开发环境，网络稳定地区

### 🧪 测试版本 (`test-simple`)
- **用途**：测试Three.js是否正确加载
- **功能**：显示简单的旋转立方体

## ✨ 特色功能

### 🎨 动态加载
- **智能检测**：自动检测Three.js是否已加载
- **错误处理**：自动重试和备用CDN
- **加载提示**：友好的加载状态显示

### 🏠 房间布局
- **基础结构**：地板、墙壁、天花板
- **主要家具**：床、书桌、椅子
- **光照系统**：环境光 + 方向光
- **阴影渲染**：真实的光影效果

### 🎮 交互控制
- **鼠标左键**：旋转视角
- **鼠标滚轮**：缩放场景
- **鼠标右键**：平移视角
- **空格键**：切换自动旋转

## 🔧 技术实现

### 动态加载Three.js
```javascript
function loadThreeJS() {
    return new Promise((resolve, reject) => {
        const threeScript = document.createElement('script');
        threeScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/0.178.0/three.min.js';
        // ... 错误处理和备用CDN
    });
}
```

### 3D场景创建
```javascript
function createRoom() {
    // 地板
    const floorGeometry = new THREE.PlaneGeometry(8, 6);
    const floorMaterial = new THREE.MeshLambertMaterial({ color: 0x8b4513 });
    const floor = new THREE.Mesh(floorGeometry, floorMaterial);
    scene.add(floor);
    
    // 墙壁、家具等...
}
```

## 🎯 自定义修改

### 修改房间颜色
在布局文件中找到材质定义：
```javascript
const wallMaterial = new THREE.MeshLambertMaterial({ color: 0xf5f5f5 });
```

### 添加新家具
在 `createRoom()` 函数中添加：
```javascript
const newFurnitureGeometry = new THREE.BoxGeometry(width, height, depth);
const newFurnitureMaterial = new THREE.MeshLambertMaterial({ color: 0xcolor });
const newFurniture = new THREE.Mesh(newFurnitureGeometry, newFurnitureMaterial);
scene.add(newFurniture);
```

### 调整光照
在 `createLighting()` 函数中修改：
```javascript
const directionalLight = new THREE.DirectionalLight(0xffffff, intensity);
```

## 🌐 CDN配置

项目使用多个CDN确保加载成功：
- **主要CDN**：`https://cdnjs.cloudflare.com/ajax/libs/three.js/0.178.0/`
- **备用CDN**：`https://unpkg.com/three@0.178.0/`

## 📱 响应式设计

- **桌面端**：完整的3D交互体验
- **移动端**：适配触摸操作
- **性能优化**：根据设备性能调整渲染质量

## 🔍 故障排除

### 问题1：Three.js未定义
**解决方案**：
1. 运行下载脚本：`./download-threejs.sh`
2. 检查文件是否存在：`ls -la assets/js/`
3. 查看浏览器控制台错误信息

### 问题2：CDN加载失败
**解决方案**：
1. 使用本地版本：`3d-room-local.html`
2. 检查网络连接
3. 尝试其他CDN源

### 问题3：性能问题
**解决方案**：
1. 降低渲染质量
2. 关闭阴影渲染
3. 减少场景复杂度

### 问题4：Jekyll构建失败
**解决方案**：
1. 检查文件路径是否正确
2. 确保YAML front matter格式正确
3. 查看Jekyll错误日志

## 🎬 灵感来源

这个3D房间的设计灵感来源于韩国短剧《闹钟》，展现了现代年轻人温馨、简约的生活空间。

## 📝 更新日志

### v1.0.0 (2024-01-XX)
- ✅ Jekyll布局集成
- ✅ 动态加载Three.js
- ✅ 本地文件版本
- ✅ 自动下载脚本
- ✅ 基础房间场景
- ✅ 交互控制系统
- ✅ 响应式设计
- ✅ 完整错误处理

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

---

**享受在Jekyll中探索3D房间的乐趣！** 🏠✨ 