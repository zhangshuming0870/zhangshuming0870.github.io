# Node.js 环境变量配置
export NODE_ENV=production

# Node.js 路径配置 - 请根据实际安装路径调整
# 如果使用 nvm 安装的 Node.js
# export PATH=$PATH:$HOME/.nvm/versions/node/$(nvm current)/bin

# 如果使用官方安装包安装的 Node.js
export PATH=$PATH:/usr/local/bin

# 如果使用 snap 安装的 Node.js
# export PATH=$PATH:/snap/bin

# 如果使用自定义路径安装的 Node.js
# export PATH=$PATH:/opt/node/bin

# npm 全局包路径
export NPM_CONFIG_PREFIX=$HOME/.npm-global
export PATH=$PATH:$HOME/.npm-global/bin