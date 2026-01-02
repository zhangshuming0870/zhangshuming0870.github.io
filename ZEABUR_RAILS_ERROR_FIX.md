# Zeabur 部署失败 - Rails 命令错误解决方案

## 问题分析

根据最新的 `error.log`，部署失败的根本原因是：

**错误信息：**
```
/bin/sh: 1: rails: not found
Back-off restarting failed container
```

**问题原因：**
1. ✅ 构建阶段已成功（Jekyll 构建完成）
2. ❌ 运行时阶段，Zeabur 错误地尝试运行 `rails` 命令
3. 这是一个 Jekyll 静态站点，不是 Rails 应用，应该使用静态文件服务器

**为什么 Zeabur 会尝试运行 rails？**
- Zeabur 可能因为 `Rakefile` 的存在而错误地识别项目为 Rails 应用
- 或者 Zeabur 的自动检测机制误判了项目类型

## 解决方案

### 方案 1：确保配置文件正确（推荐）

已完成的配置：

1. **zeabur.json** - 明确指定为静态站点：
```json
{
  "build": {
    "command": "gem install bundler && bundle install && bundle exec jekyll build",
    "outputDirectory": "_site"
  },
  "framework": "static",
  "installCommand": "gem install bundler && bundle install",
  "rootDirectory": ".",
  "startCommand": "npx serve _site -p $PORT"
}
```

2. **Procfile** - 指定启动命令：
```
web: npx serve _site -p $PORT
```

3. **package.json** - 包含启动脚本和依赖：
```json
{
  "scripts": {
    "start": "npx serve _site -p $PORT"
  },
  "dependencies": {
    "serve": "^14.2.1"
  }
}
```

### 方案 2：在 Zeabur 控制台手动配置

如果配置文件仍然不起作用，请在 Zeabur 控制台进行以下操作：

1. **设置环境变量：**
   - `ZEABUR_FRAMEWORK=static`
   - `PORT=3000`（或 Zeabur 分配的端口）

2. **明确设置项目类型：**
   - 在项目设置中，选择"静态站点"而不是"自动检测"
   - 禁用 Rails 自动检测

3. **手动设置启动命令：**
   - 在 Zeabur 控制台的"启动命令"设置中，明确输入：`npx serve _site -p $PORT`

### 方案 3：移除 Rakefile（如果构建不再需要）

如果构建阶段不再需要 Rakefile，可以尝试重命名或删除它：

```bash
# 重命名 Rakefile（保留备份）
mv Rakefile Rakefile.backup
```

**注意：** 只有在确认构建阶段不再需要 Rakefile 时才这样做。

### 方案 4：创建 .zeaburignore（如果支持）

如果 Zeabur 支持，可以创建 `.zeaburignore` 文件来排除可能触发 Rails 检测的文件。

## 验证步骤

1. 提交所有更改到 Git
2. 在 Zeabur 控制台重新部署
3. 检查构建日志，确认：
   - ✅ 构建阶段成功（Jekyll build 完成）
   - ✅ 运行时使用正确的启动命令（`npx serve` 而不是 `rails`）
4. 如果仍然失败，查看 Zeabur 控制台的详细日志

## 如果问题仍然存在

1. **联系 Zeabur 支持**，说明：
   - 这是 Jekyll 静态站点，不是 Rails 应用
   - 已经配置了 `framework: "static"` 和 `startCommand`
   - 但 Zeabur 仍然尝试运行 `rails` 命令

2. **检查 Zeabur 控制台的项目设置**：
   - 确认项目类型设置为"静态站点"
   - 确认没有启用 Rails 自动检测
   - 确认启动命令正确设置

3. **尝试使用 Dockerfile**（最后手段）：
   如果 Zeabur 的自动检测一直有问题，可以考虑创建 Dockerfile 来完全控制构建和运行过程。

## 当前配置文件状态

- ✅ `zeabur.json` - 已配置为静态站点
- ✅ `Procfile` - 已设置正确的启动命令
- ✅ `package.json` - 已包含 serve 依赖和启动脚本
- ✅ `start.sh` - 启动脚本已创建
- ⚠️ `Rakefile` - 可能存在，可能触发 Rails 检测

