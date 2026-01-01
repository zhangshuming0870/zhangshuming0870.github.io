#!/bin/bash
set -e

# 静态站点启动脚本
# 使用 serve 来服务静态文件，而不是 rails

PORT=${PORT:-3000}

echo "Starting static site server on port $PORT..."
npx serve _site -p $PORT

