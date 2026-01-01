# Zeabur 部署配置说明

## 配置文件说明

已为项目添加了以下配置文件以支持 Zeabur 部署：

### 1. `zeabur.json`
Zeabur 的主要配置文件，指定了构建命令和输出目录。

### 2. `package.json`
包含构建脚本和引擎版本要求。

### 3. `.ruby-version`
指定 Ruby 版本为 3.1.0。

### 4. `.nvmrc`
指定 Node.js 版本为 18。

## 部署步骤

1. 在 Zeabur 平台上连接你的 GitHub 仓库
2. Zeabur 会自动检测到 `zeabur.json` 配置文件
3. 构建命令会自动执行：`gem install bundler && bundle install && bundle exec jekyll build`
4. 输出目录设置为 `_site`
5. 部署完成后，静态站点会自动上线

## 常见问题

### 如果部署失败，请检查：

1. **Ruby 版本**：确保 `.ruby-version` 文件中的版本可用
2. **依赖安装**：检查 `Gemfile` 和 `Gemfile.lock` 是否正确
3. **构建输出**：确认 `_site` 目录在构建后包含所有静态文件
4. **环境变量**：如果有需要，在 Zeabur 控制台设置必要的环境变量

## 构建命令

```bash
gem install bundler
bundle install
bundle exec jekyll build
```

## 输出目录

构建后的静态文件位于 `_site` 目录。

