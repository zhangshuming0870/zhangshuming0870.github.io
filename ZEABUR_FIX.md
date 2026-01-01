# Zeabur 部署问题解决方案

## 问题分析

根据 `error.log` 文件，部署失败的原因是：

```
No Rakefile found (looking for: rakefile, Rakefile, rakefile.rb, Rakefile.rb)
ERROR: process "/bin/sh -c bundle exec rake assets:precompile" did not complete successfully
```

**根本原因：**
Zeabur 错误地将 Jekyll 项目识别为 Rails 项目，并尝试运行 `bundle exec rake assets:precompile`，但 Jekyll 项目不需要这个命令。

## 解决方案

### 1. 创建了 Rakefile
创建了 `Rakefile` 文件，提供空的 `assets:precompile` 任务，防止 rake 命令失败。

### 2. 更新了 zeabur.json
明确指定：
- `framework: "static"` - 告诉 Zeabur 这是静态站点
- 明确的构建命令：`bundle exec jekyll build`
- 输出目录：`_site`

### 3. 创建了构建脚本
创建了 `build.sh` 脚本，明确构建流程。

## 配置文件说明

### zeabur.json
```json
{
  "build": {
    "command": "gem install bundler && bundle install && bundle exec jekyll build",
    "outputDirectory": "_site"
  },
  "framework": "static",
  "installCommand": "gem install bundler && bundle install",
  "rootDirectory": "."
}
```

### Rakefile
提供了空的 rake 任务，防止 Zeabur 运行 Rails 相关的 rake 命令时失败。

## 下一步

1. 提交这些更改到 Git
2. 在 Zeabur 平台重新部署
3. 如果仍然失败，检查 Zeabur 控制台的构建日志

## 如果问题仍然存在

如果 Zeabur 仍然尝试运行 `rake assets:precompile`，可以尝试：

1. 在 Zeabur 控制台的环境变量中设置：
   - `ZEABUR_SKIP_RAKE=true`
   - 或者禁用自动检测

2. 联系 Zeabur 支持，说明这是 Jekyll 静态站点，不是 Rails 项目

