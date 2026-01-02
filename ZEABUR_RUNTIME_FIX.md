# Zeabur 运行时错误解决方案

## 问题分析

根据最新的 `error.log`，问题已经从构建阶段转移到了运行时阶段：

**错误信息：**
```
/bin/sh: 1: rails: not found
Back-off restarting failed container
```

**问题原因：**
1. ✅ 构建阶段已成功（不再有 rake 错误）
2. ❌ 运行时阶段，Zeabur 仍然尝试运行 `rails` 命令
3. Jekyll 是静态站点，不需要 Rails，应该直接服务静态文件

## 解决方案

### 1. 创建了 Procfile
创建了 `Procfile` 文件，明确指定使用静态文件服务器：
```
web: npx serve _site -p $PORT
```

### 2. 更新了 package.json
- 添加了 `serve` 依赖
- 更新了 `start` 脚本，使用 `npx serve` 而不是 `jekyll serve`

### 3. 创建了 start.sh
创建了启动脚本作为备用方案。

### 4. 更新了 zeabur.json
确保配置明确指定为静态站点框架。

## 配置文件

### Procfile
```
web: npx serve _site -p $PORT
```

### package.json
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

## 如果问题仍然存在

如果 Zeabur 仍然尝试运行 `rails`，可以尝试：

1. **在 Zeabur 控制台设置环境变量：**
   - `ZEABUR_FRAMEWORK=static`
   - 或者禁用自动检测

2. **确保项目类型设置为静态站点：**
   - 在 Zeabur 控制台的项目设置中，明确选择"静态站点"

3. **检查是否有其他配置文件触发 Rails 检测：**
   - 检查是否有 `config/application.rb` 或其他 Rails 相关文件
   - 确保 Gemfile 中没有 rails gem


