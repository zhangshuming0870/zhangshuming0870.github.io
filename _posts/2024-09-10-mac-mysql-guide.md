---
layout: post
title: "Mac 下 MySQL 使用指南"
date: 2024-09-10
categories: [数据库]
tags: [MySQL, Mac]
author: zhangshuming
---

# Mac 下 MySQL 使用指南

## 1. 安装 MySQL

### 方式一：通过 Homebrew 安装
```bash
brew install mysql
```

### 方式二：通过 DMG 安装包
1. 访问 [MySQL 官网](https://dev.mysql.com/downloads/mysql/) 下载适用于 macOS 的 DMG 安装包。
2. 按照安装向导完成安装。

## 2. 启动与停止 MySQL 服务

### 使用 Homebrew 安装的启动方式
```bash
brew services start mysql   # 启动
brew services stop mysql    # 停止
brew services restart mysql # 重启
```

### 使用系统偏好设置启动（DMG 安装）
- 打开“系统偏好设置” > “MySQL”，点击“Start MySQL Server”。

## 3. 配置环境变量

如果终端输入 `mysql` 提示找不到命令，可以将 MySQL 的 bin 目录加入环境变量：

```bash
echo 'export PATH="/usr/local/mysql/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## 4. 常用命令

- 登录 MySQL：
  ```bash
  mysql -u root -p
  ```
- 修改 root 密码：
  ```sql
  ALTER USER 'root'@'localhost' IDENTIFIED BY '新密码';
  ```
- 查看所有数据库：
  ```sql
  SHOW DATABASES;
  ```
- 创建数据库：
  ```sql
  CREATE DATABASE dbname;
  ```
- 退出 MySQL：
  ```sql
  exit;
  ```

## 5. 常见问题

### 5.1 启动报错："Can't connect to local MySQL server"
- 检查 MySQL 服务是否已启动。
- 检查端口是否被占用。

### 5.2 忘记 root 密码
- 参考官方文档重置 root 密码。

### 5.3 卸载 MySQL
```bash
brew uninstall mysql
# 或手动删除 /usr/local/mysql 相关文件
```

## 6. 参考链接
- [MySQL 官方文档](https://dev.mysql.com/doc/)
- [Homebrew 官网](https://brew.sh/) 

## 7. 数据库操作详解

### 7.1 创建数据库
```sql
CREATE DATABASE dbname CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

### 7.2 删除数据库
```sql
DROP DATABASE dbname;
```

### 7.3 创建用户
```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```

### 7.4 删除用户
```sql
DROP USER 'username'@'localhost';
```

### 7.5 用户授权
```sql
GRANT ALL PRIVILEGES ON dbname.* TO 'username'@'localhost';
FLUSH PRIVILEGES;
```

### 7.6 撤销授权
```sql
REVOKE ALL PRIVILEGES ON dbname.* FROM 'username'@'localhost';
FLUSH PRIVILEGES;
```

### 7.7 备份数据库
```bash
mysqldump -u root -p dbname > dbname_backup.sql
```

### 7.8 恢复数据库
```bash
mysql -u root -p dbname < dbname_backup.sql
```

### 7.9 导入数据（如 CSV 文件）
```sql
LOAD DATA INFILE '/path/to/file.csv' INTO TABLE tablename FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
```

### 7.10 导出表为 CSV
```sql
SELECT * FROM tablename INTO OUTFILE '/path/to/file.csv' FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
```

### 7.11 创建表
```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 7.12 删除表
```sql
DROP TABLE tablename;
```

### 7.13 修改表结构（添加字段）
```sql
ALTER TABLE users ADD COLUMN age INT;
```

### 7.14 查询表结构
```sql
DESCRIBE users;
``` 