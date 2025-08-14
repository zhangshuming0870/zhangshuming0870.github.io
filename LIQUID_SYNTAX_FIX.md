# Liquid语法错误修复指南

## 问题描述

在Jekyll博客中，当Markdown文件包含JavaScript/JSX代码时，可能会出现Liquid语法错误。这是因为Jekyll的Liquid模板引擎会尝试解析所有`{{}}`和`{%%}`语法，即使它们是在代码块中。

## 常见错误

### 1. JavaScript对象语法错误

**错误示例：**
```tsx
// ❌ 这会导致Liquid语法错误
<div style={{ width: '100vw', height: '100vh', position: 'fixed', top: '0', left: '0', zIndex: 1000 }}>
```

**正确示例：**
```tsx
// ✅ 使用CSS字符串语法
<div style="width: 100vw; height: 100vh; position: fixed; top: 0; left: 0; z-index: 1000;">
```

### 2. 模板字符串语法错误

**错误示例：**
```tsx
// ❌ 这会导致Liquid语法错误
const message = `Hello ${name}`;
```

**正确示例：**
```tsx
// ✅ 使用字符串连接
const message = 'Hello ' + name;
```

## 解决方案

### 方案1：使用CSS字符串语法

将JSX中的内联样式从JavaScript对象语法改为CSS字符串语法：

```tsx
// 修改前
<div style={{ width: '100vw', height: '100vh' }}>

// 修改后  
<div style="width: 100vw; height: 100vh;">
```

### 方案2：使用CSS类

避免内联样式，使用CSS类：

```tsx
// 修改前
<div style={{ width: '100vw', height: '100vh', position: 'fixed' }}>

// 修改后
<div class="fullscreen-container">
```

```css
.fullscreen-container {
  width: 100vw;
  height: 100vh;
  position: fixed;
}
```

### 方案3：使用Liquid raw标签

如果必须使用JavaScript对象语法，可以使用Liquid的raw标签：

```liquid
{% raw %}
<div style={{ width: '100vw', height: '100vh' }}>
{% endraw %}
```

## 已修复的文件

以下文件已经修复了Liquid语法错误：

1. `_posts/2025-04-01-nextjs-build-error1.md` - 第43行
2. `_posts/2025-03-19-nextjs-build-errors-analysis.md` - 第144行

## 预防措施

1. **代码审查**：在提交代码前检查是否包含JavaScript对象语法
2. **使用CSS类**：尽量使用CSS类而不是内联样式
3. **测试构建**：定期运行Jekyll构建命令检查语法错误
4. **文档规范**：在团队中建立代码规范，避免使用会导致冲突的语法

## 构建检查

运行以下命令检查是否还有语法错误：

```bash
bundle exec jekyll build
```

或者使用Python服务器测试：

```bash
python3 -m http.server 8000
```

## 注意事项

- Jekyll会处理所有Markdown文件中的Liquid语法
- 代码块中的语法也会被解析
- 使用CSS字符串语法是最安全的解决方案
- 定期检查构建日志中的警告信息
