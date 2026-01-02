# Zeabur 磁盘空间问题解决方案

## 问题分析

根据最新的错误日志分析：

### ✅ 好消息：Rails 问题已解决！

- **不再出现** `rails: not found` 错误
- Dockerfile 方案成功，Zeabur 正确使用 `serve` 命令
- 项目类型识别问题已解决

### ⚠️ 新问题：节点磁盘空间不足

**错误信息：**
```
Evicted: The node was low on resource: ephemeral-storage
Evicted: The node had condition: [DiskPressure]
```

**原因分析：**
1. 之前的失败部署留下了大量失败的 Pod
2. 镜像大小较大（618MB）
3. Zeabur 节点的临时存储空间不足

## 已实施的优化

### 1. 创建了 .dockerignore
排除不必要的文件，减小构建上下文：
- Git 文件（.git, .gitignore）
- 构建输出（_site，会在 Dockerfile 中重新构建）
- 依赖目录（node_modules, vendor）
- 日志和临时文件
- 文档文件

### 2. 优化了 Dockerfile
- 使用 `--deployment` 模式安装 gems
- 构建后清理构建工具和缓存
- 清理 npm 和 gem 缓存
- 移除不必要的构建依赖

### 3. 镜像大小优化
通过优化，预期镜像大小可以从 618MB 减小到约 200-300MB

## 解决方案

### 方案 1：等待自动清理（推荐）

Zeabur 会自动清理被驱逐的 Pod 和旧的镜像。通常需要：
- 等待 10-30 分钟
- Zeabur 会自动清理资源
- 新的部署应该可以成功

### 方案 2：在 Zeabur 控制台手动清理

1. 登录 Zeabur 控制台
2. 进入项目设置
3. 查找"清理"或"清理资源"选项
4. 手动触发清理操作

### 方案 3：使用多阶段构建（进一步优化）

如果问题持续，可以使用多阶段构建进一步减小镜像大小：

```dockerfile
# 构建阶段
FROM ruby:3.2-slim AS builder
WORKDIR /app
COPY Gemfile Gemfile.lock ./
RUN gem install bundler && bundle install --deployment
COPY . .
RUN bundle exec jekyll build

# 运行阶段
FROM node:18-slim
RUN npm install -g serve
WORKDIR /app
COPY --from=builder /app/_site ./_site
EXPOSE 3000
CMD ["sh", "-c", "serve _site -p ${PORT:-3000}"]
```

## 验证步骤

部署后检查：

1. **构建日志**
   - 应该看到 Jekyll 构建成功
   - 镜像大小应该减小

2. **运行时日志**
   - 应该看到 `serve _site -p 3000`
   - 不应该看到 `rails: not found`
   - 不应该看到 `DiskPressure` 错误

3. **Pod 状态**
   - Pod 应该正常运行
   - 不应该被驱逐（Evicted）

## 当前状态

- ✅ Rails 误判问题已解决
- ✅ Dockerfile 已优化
- ⚠️ 等待磁盘空间问题自动解决

## 下一步

1. **提交优化后的 Dockerfile**
   ```bash
   git add Dockerfile .dockerignore
   git commit -m "优化 Dockerfile，减小镜像大小"
   git push
   ```

2. **等待 Zeabur 重新部署**
   - 使用优化后的 Dockerfile
   - 镜像大小应该减小
   - 磁盘空间问题应该缓解

3. **监控部署状态**
   - 查看构建日志
   - 查看运行时日志
   - 确认 Pod 正常运行

## 如果问题仍然存在

如果磁盘空间问题持续：

1. **联系 Zeabur 支持**
   - 说明节点磁盘空间不足
   - 请求清理资源或分配更多资源

2. **考虑升级计划**
   - 如果免费计划资源有限，考虑升级

3. **使用多阶段构建**
   - 进一步减小镜像大小
   - 只保留运行所需的文件

