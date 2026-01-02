# Zeabur 控制台设置指南 - 解决 Rails 误判问题

## 问题说明

当前 Zeabur 错误地将 Jekyll 静态站点识别为 Rails 项目，导致尝试运行 `rails` 命令而失败。

## 解决步骤（必须在 Zeabur 控制台完成）

### 步骤 1：登录 Zeabur 控制台

1. 访问 https://zeabur.com
2. 登录你的账号
3. 进入你的项目（项目名称应该包含 `zhangshuming0870.github.io`）

### 步骤 2：进入项目设置

1. 在项目页面，找到 **"Settings"（设置）** 或 **"配置"** 选项
2. 点击进入设置页面

### 步骤 3：检查并修改项目类型

在设置页面中找到以下选项：

#### 选项 A：Framework / 项目类型 / Project Type

- **当前状态**：可能是 "Rails" 或 "Auto Detect"（自动检测）
- **需要修改为**：**"Static Site"（静态站点）** 或 **"Static"**
- **操作**：从下拉菜单中选择 "Static Site"

#### 选项 B：Build Settings / 构建设置

如果找不到 Framework 选项，查找：
- **Build Command（构建命令）**：应该是 `gem install bundler && bundle install && bundle exec jekyll build`
- **Output Directory（输出目录）**：应该是 `_site`

### 步骤 4：设置启动命令（最关键！）

找到以下任一选项：

- **Start Command（启动命令）**
- **Run Command（运行命令）**
- **Command（命令）**

**必须设置为：**
```
npx serve _site -p $PORT
```

或者：
```
sh -c "npx serve _site -p $PORT"
```

**重要：** 确保这里**不是** `rails` 或 `bundle exec rails`！

### 步骤 5：检查环境变量

在设置页面找到 **"Environment Variables"（环境变量）** 部分：

**添加或检查以下环境变量：**

| 变量名 | 值 | 说明 |
|--------|-----|------|
| `ZEABUR_FRAMEWORK` | `static` | 明确指定为静态站点 |
| `PORT` | `3000` | 端口（Zeabur 通常会自动设置） |

### 步骤 6：保存并重新部署

1. 点击 **"Save"（保存）** 或 **"Update"（更新）** 按钮
2. 返回项目主页面
3. 找到 **"Redeploy"（重新部署）** 或 **"Deploy"（部署）** 按钮
4. 点击触发新的部署

### 步骤 7：验证部署

部署开始后：

1. 进入 **"Logs"（日志）** 页面
2. 查看构建日志，应该看到：
   ```
   bundle exec jekyll build
   Build completed successfully!
   ```
3. 查看运行时日志，应该看到：
   ```
   serve _site -p 3000
   Serving!
   ```
4. **不应该看到**：
   ```
   rails: not found
   ```

## 如果找不到这些选项

如果 Zeabur 控制台的界面不同，尝试以下方法：

### 方法 1：删除并重新创建项目

1. 删除当前项目
2. 重新连接 GitHub 仓库
3. **在创建时明确选择 "Static Site"**

### 方法 2：联系 Zeabur 支持

如果控制台中没有这些设置选项，联系 Zeabur 支持：

**提供以下信息：**
- 项目类型：Jekyll 静态站点
- 问题：Zeabur 错误地尝试运行 `rails` 命令
- 期望行为：应该运行 `npx serve _site -p $PORT`
- 已配置的文件：
  - `zeabur.json` 中设置了 `framework: "static"` 和 `startCommand: "npx serve _site -p $PORT"`
  - `Procfile` 中设置了 `web: npx serve _site -p $PORT`
  - `Dockerfile` 已准备好

## 当前项目配置（供参考）

### zeabur.json
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

## 常见问题

### Q: 找不到 "Framework" 或 "Project Type" 选项？
A: Zeabur 的界面可能不同，尝试查找 "Settings" → "Build" 或 "Deploy" 相关选项。

### Q: 修改后仍然失败？
A: 
1. 确保保存了所有更改
2. 触发完全重新部署（不是增量部署）
3. 清除浏览器缓存后重新登录
4. 如果还是不行，尝试方案 2：删除 zeabur.json，使用 Dockerfile

### Q: 如何确认设置已生效？
A: 查看部署日志，如果看到 `serve _site -p` 而不是 `rails`，说明设置成功。

## 下一步

完成控制台设置后：
1. 等待部署完成
2. 检查日志确认不再有 `rails: not found` 错误
3. 如果问题解决，访问你的网站确认正常运行
4. 如果问题仍然存在，告诉我，我们可以尝试方案 2

