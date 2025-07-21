# 🏠 Jekyll 3D房间项目

这是一个在Jekyll项目中集成Three.js 3D房间的完整解决方案。

## 📁 项目结构

```
├── _layouts/
│   └── 3d-room.html          # 3D房间布局文件
├── 3d-room.md                # 3D房间页面
├── _3d-room.html             # 独立HTML页面
└── README_3D_Room_Jekyll.md # 项目说明文档
```

## 🚀 使用方法

### 方法一：使用Jekyll布局（推荐）

1. **创建页面**：
   ```markdown
   ---
   layout: 3d-room
   title: 我的3D房间
   ---
   
   这里是页面内容...
   ```

2. **访问页面**：
   - 启动Jekyll服务器：`jekyll serve`
   - 访问：`http://localhost:4000/3d-room.html`

### 方法二：直接访问HTML文件

- 访问：`http://localhost:4000/_3d-room.html`

## ✨ 特色功能

### 🎨 动态加载
- **Three.js库**：通过CDN动态加载
- **OrbitControls**：鼠标交互控制
- **错误处理**：自动重试和备用CDN

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
        threeScript.src = 'https://cdn.jsdelivr.net/npm/three@0.178.0/build/three.min.js';
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
在 `_layouts/3d-room.html` 中找到材质定义：
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
- **主要CDN**：`https://cdn.jsdelivr.net/npm/three@0.178.0/`
- **备用CDN**：`https://unpkg.com/three@0.178.0/`

## 📱 响应式设计

- **桌面端**：完整的3D交互体验
- **移动端**：适配触摸操作
- **性能优化**：根据设备性能调整渲染质量

## 🔍 故障排除

### 问题1：Three.js未定义
- 检查网络连接
- 查看浏览器控制台错误信息
- 尝试使用本地服务器

### 问题2：性能问题
- 降低渲染质量
- 关闭阴影渲染
- 减少场景复杂度

### 问题3：CDN访问失败
- 使用本地Three.js文件
- 配置代理服务器
- 使用其他CDN源

## 🎬 灵感来源

这个3D房间的设计灵感来源于韩国短剧《闹钟》，展现了现代年轻人温馨、简约的生活空间。

## 📝 更新日志

### v1.0.0 (2024-01-XX)
- ✅ Jekyll布局集成
- ✅ 动态加载Three.js
- ✅ 基础房间场景
- ✅ 交互控制系统
- ✅ 响应式设计

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

---

**享受在Jekyll中探索3D房间的乐趣！** 🏠✨ 