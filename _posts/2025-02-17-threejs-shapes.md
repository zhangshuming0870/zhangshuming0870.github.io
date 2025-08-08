---
layout: post
title: "threejs 各种形状的添加"
date: 2025-02-17
categories: [前端]
tags: [前端,threejs]
author: zhangshuming
---

# Three.js 形状创建指南

本文档详细介绍Three.js中各种几何体的创建方法和参数含义，帮助开发者快速掌握3D形状的创建技巧。

## 目录

- [基础几何体](#基础几何体)
- [复杂几何体](#复杂几何体)
- [自定义几何体](#自定义几何体)
- [材质和渲染](#材质和渲染)
- [实用技巧](#实用技巧)

## 基础几何体

### 1. 立方体 (BoxGeometry)

```javascript
const geometry = new THREE.BoxGeometry(width, height, depth, widthSegments, heightSegments, depthSegments);
```

**参数说明：**
- `width`: 宽度（X轴）
- `height`: 高度（Y轴）
- `depth`: 深度（Z轴）
- `widthSegments`: 宽度分段数（可选）
- `heightSegments`: 高度分段数（可选）
- `depthSegments`: 深度分段数（可选）

**示例：**
```javascript
// 创建一个1x1x1的立方体
const cube = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshLambertMaterial({ color: 0x00ff00 })
);
```

### 2. 球体 (SphereGeometry)

```javascript
const geometry = new THREE.SphereGeometry(radius, widthSegments, heightSegments, phiStart, phiLength, thetaStart, thetaLength);
```

**参数说明：**
- `radius`: 球体半径
- `widthSegments`: 水平分段数（经度）
- `heightSegments`: 垂直分段数（纬度）
- `phiStart`: 水平起始角度（默认0）
- `phiLength`: 水平角度范围（默认2π）
- `thetaStart`: 垂直起始角度（默认0）
- `thetaLength`: 垂直角度范围（默认π）

**示例：**
```javascript
// 创建完整球体
const sphere = new THREE.Mesh(
  new THREE.SphereGeometry(0.5, 32, 16),
  new THREE.MeshLambertMaterial({ color: 0xff0000 })
);

// 创建半球体（鼠标形状）
const hemisphere = new THREE.Mesh(
  new THREE.SphereGeometry(0.06, 16, 8, 0, Math.PI * 2, 0, Math.PI / 2),
  new THREE.MeshLambertMaterial({ color: 0x333333 })
);
```

### 3. 圆柱体 (CylinderGeometry)

```javascript
const geometry = new THREE.CylinderGeometry(radiusTop, radiusBottom, height, radialSegments, heightSegments, openEnded, thetaStart, thetaLength);
```

**参数说明：**
- `radiusTop`: 顶部半径
- `radiusBottom`: 底部半径
- `height`: 高度
- `radialSegments`: 径向分段数
- `heightSegments`: 高度分段数
- `openEnded`: 是否开放两端（默认false）
- `thetaStart`: 起始角度（默认0）
- `thetaLength`: 角度范围（默认2π）

**示例：**
```javascript
// 创建圆柱体
const cylinder = new THREE.Mesh(
  new THREE.CylinderGeometry(0.5, 0.5, 2, 16),
  new THREE.MeshLambertMaterial({ color: 0x0000ff })
);

// 创建圆锥体
const cone = new THREE.Mesh(
  new THREE.CylinderGeometry(0, 0.5, 2, 16),
  new THREE.MeshLambertMaterial({ color: 0xffff00 })
);
```

### 4. 平面 (PlaneGeometry)

```javascript
const geometry = new THREE.PlaneGeometry(width, height, widthSegments, heightSegments);
```

**参数说明：**
- `width`: 宽度
- `height`: 高度
- `widthSegments`: 宽度分段数（可选）
- `heightSegments`: 高度分段数（可选）

**示例：**
```javascript
// 创建地板
const floor = new THREE.Mesh(
  new THREE.PlaneGeometry(10, 10),
  new THREE.MeshLambertMaterial({ color: 0x8B4513 })
);
floor.rotation.x = -Math.PI / 2; // 水平放置
```

## 复杂几何体

### 1. 圆环 (TorusGeometry)

```javascript
const geometry = new THREE.TorusGeometry(radius, tube, radialSegments, tubularSegments, arc);
```

**参数说明：**
- `radius`: 圆环半径
- `tube`: 管道半径
- `radialSegments`: 径向分段数
- `tubularSegments`: 管道分段数
- `arc`: 圆环弧度（默认2π）

**示例：**
```javascript
const torus = new THREE.Mesh(
  new THREE.TorusGeometry(1, 0.3, 16, 100),
  new THREE.MeshLambertMaterial({ color: 0x00ffff })
);
```

### 2. 八面体 (OctahedronGeometry)

```javascript
const geometry = new THREE.OctahedronGeometry(radius, detail);
```

**参数说明：**
- `radius`: 半径
- `detail`: 细分级别（默认0）

**示例：**
```javascript
const octahedron = new THREE.Mesh(
  new THREE.OctahedronGeometry(0.5),
  new THREE.MeshLambertMaterial({ color: 0xff00ff })
);
```

### 3. 十二面体 (DodecahedronGeometry)

```javascript
const geometry = new THREE.DodecahedronGeometry(radius, detail);
```

**参数说明：**
- `radius`: 半径
- `detail`: 细分级别（默认0）

**示例：**
```javascript
const dodecahedron = new THREE.Mesh(
  new THREE.DodecahedronGeometry(0.5),
  new THREE.MeshLambertMaterial({ color: 0x00ff00 })
);
```

## 自定义几何体

### 1. 使用BufferGeometry

```javascript
const geometry = new THREE.BufferGeometry();

// 定义顶点位置
const vertices = new Float32Array([
  -1.0, -1.0,  1.0,
   1.0, -1.0,  1.0,
   1.0,  1.0,  1.0,
  -1.0,  1.0,  1.0
]);

// 定义面索引
const indices = new Uint16Array([
  0, 1, 2,
  0, 2, 3
]);

geometry.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
geometry.setIndex(new THREE.BufferAttribute(indices, 1));
geometry.computeVertexNormals();

const mesh = new THREE.Mesh(geometry, material);
```

### 2. 使用ShapeGeometry

```javascript
const shape = new THREE.Shape();
shape.moveTo(0, 0);
shape.lineTo(0, 1);
shape.lineTo(1, 1);
shape.lineTo(1, 0);
shape.lineTo(0, 0);

const geometry = new THREE.ShapeGeometry(shape);
const mesh = new THREE.Mesh(geometry, material);
```

## 材质和渲染

### 1. 基础材质

```javascript
// Lambert材质（漫反射）
const lambertMaterial = new THREE.MeshLambertMaterial({ 
  color: 0xff0000,
  transparent: true,
  opacity: 0.8
});

// Phong材质（高光反射）
const phongMaterial = new THREE.MeshPhongMaterial({ 
  color: 0x00ff00,
  shininess: 100
});

// 基础材质（无光照）
const basicMaterial = new THREE.MeshBasicMaterial({ 
  color: 0x0000ff,
  wireframe: true
});
```

### 2. 纹理材质

```javascript
const textureLoader = new THREE.TextureLoader();
const texture = textureLoader.load('/path/to/texture.jpg');

const material = new THREE.MeshLambertMaterial({ 
  map: texture,
  transparent: true,
  opacity: 0.9
});
```

## 实用技巧

### 1. 形状变换

```javascript
// 缩放
mesh.scale.set(1.5, 1, 1); // X轴拉伸1.5倍

// 旋转
mesh.rotation.set(0, Math.PI / 2, 0); // 绕Y轴旋转90度

// 位移
mesh.position.set(1, 0, 2);
```

### 2. 阴影设置

```javascript
mesh.castShadow = true;      // 投射阴影
mesh.receiveShadow = true;   // 接收阴影
```

### 3. 用户数据

```javascript
mesh.userData = {
  name: '鼠标',
  nameEn: 'mouse',
  isInteractive: true
};
```

### 4. 性能优化

```javascript
// 合并几何体
const mergedGeometry = BufferGeometryUtils.mergeBufferGeometries([
  geometry1,
  geometry2,
  geometry3
]);

// 实例化渲染
const instancedMesh = new THREE.InstancedMesh(
  geometry,
  material,
  count
);
```

## 常见应用场景

### 1. 鼠标模型
```javascript
// 椭圆形鼠标
const mouseGeometry = new THREE.SphereGeometry(0.06, 16, 8, 0, Math.PI * 2, 0, Math.PI / 2);
const mouse = new THREE.Mesh(mouseGeometry, material);
mouse.scale.set(1.8, 1, 1); // 拉伸成椭圆形
```

### 2. 键盘模型
```javascript
// 扁平键盘
const keyboardGeometry = new THREE.BoxGeometry(0.35, 0.02, 0.12);
const keyboard = new THREE.Mesh(keyboardGeometry, material);
```

### 3. 桌子模型
```javascript
// 圆形桌子
const tableGeometry = new THREE.CylinderGeometry(0.8, 0.8, 0.05, 16);
const table = new THREE.Mesh(tableGeometry, material);
```

## 总结

Three.js提供了丰富的几何体类型，从简单的立方体到复杂的自定义形状。通过合理选择几何体类型和参数，可以创建出各种逼真的3D模型。记住以下几点：

1. **选择合适的几何体**：根据需求选择最接近的几何体类型
2. **合理设置分段数**：平衡视觉效果和性能
3. **使用变换**：通过缩放、旋转、位移调整形状
4. **优化性能**：合理使用材质和阴影设置

通过掌握这些技巧，您就能创建出各种精美的3D形状了！ 