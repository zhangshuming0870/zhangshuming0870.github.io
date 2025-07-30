#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json
import yaml
from datetime import datetime
from pathlib import Path

def extract_posts_data():
    """从_posts目录提取所有文章数据"""
    posts_dir = Path('_posts')
    posts_data = []
    
    if not posts_dir.exists():
        print(f"错误：{posts_dir} 目录不存在")
        return posts_data
    
    for file_path in posts_dir.glob('*.md'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取front matter
            if not content.startswith('---'):
                print(f"警告：{file_path.name} 没有front matter")
                continue
            
            match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if not match:
                print(f"警告：{file_path.name} front matter格式不正确")
                continue
            
            frontmatter_text = match.group(1)
            
            try:
                frontmatter = yaml.safe_load(frontmatter_text)
            except yaml.YAMLError as e:
                print(f"错误：{file_path.name} YAML解析失败: {e}")
                continue
            
            # 提取文章摘要
            excerpt = content.replace(frontmatter_text, '').replace('---', '').strip()
            excerpt = re.sub(r'<[^>]*>', '', excerpt)  # 移除HTML标签
            excerpt = re.sub(r'#{1,6}\s+', '', excerpt)  # 移除标题标记
            excerpt = excerpt[:150] + '...' if len(excerpt) > 150 else excerpt
            
            # 构建文章数据
            categories = frontmatter.get('categories', ['其他'])
            # 使用第一个分类作为URL路径的一部分
            category_path = categories[0].lower() if categories else '其他'
            post_data = {
                'title': frontmatter.get('title', file_path.stem),
                'excerpt': excerpt,
                'url': f"/{category_path}/{frontmatter.get('date', '2024-01-01').strftime('%Y/%m/%d')}/{file_path.stem}.html",
                'date': frontmatter.get('date', datetime.now()).strftime('%Y-%m-%d'),
                'categories': categories,
                'tags': frontmatter.get('tags', [])
            }
            
            posts_data.append(post_data)
            print(f"已处理：{file_path.name}")
            
        except Exception as e:
            print(f"错误：处理 {file_path.name} 时出错: {e}")
    
    return posts_data

def generate_posts_json(posts_data):
    """生成posts-data.json文件"""
    json_data = {'posts': posts_data}
    
    with open('posts-data.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    print(f"已生成 posts-data.json 文件，包含 {len(posts_data)} 篇文章")

def fix_post_frontmatter():
    """修复文章front matter格式"""
    posts_dir = Path('_posts')
    fixed_count = 0
    
    if not posts_dir.exists():
        print(f"错误：{posts_dir} 目录不存在")
        return
    
    for file_path in posts_dir.glob('*.md'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否有front matter
            if not content.startswith('---'):
                print(f"警告：{file_path.name} 没有front matter")
                continue
            
            # 提取front matter
            match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if not match:
                print(f"警告：{file_path.name} front matter格式不正确")
                continue
            
            frontmatter_text = match.group(1)
            
            try:
                frontmatter = yaml.safe_load(frontmatter_text)
            except yaml.YAMLError as e:
                print(f"错误：{file_path.name} YAML解析失败: {e}")
                continue
            
            # 确保必要的字段存在
            needs_update = False
            
            if 'layout' not in frontmatter:
                frontmatter['layout'] = 'post'
                needs_update = True
            
            if 'title' not in frontmatter:
                title = file_path.stem.replace('-', ' ').title()
                frontmatter['title'] = title
                needs_update = True
            
            if 'date' not in frontmatter:
                # 从文件名提取日期
                date_match = re.match(r'(\d{4}-\d{2}-\d{2})', file_path.name)
                if date_match:
                    frontmatter['date'] = datetime.strptime(date_match.group(1), '%Y-%m-%d')
                else:
                    frontmatter['date'] = datetime.now()
                needs_update = True
            
            if 'categories' not in frontmatter:
                frontmatter['categories'] = ['其他']
                needs_update = True
            
            if 'tags' not in frontmatter:
                frontmatter['tags'] = []
                needs_update = True
            
            if 'author' not in frontmatter:
                frontmatter['author'] = 'zhangshuming'
                needs_update = True
            
            # 如果需要更新，重写文件
            if needs_update:
                # 重新生成front matter
                new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
                
                # 替换front matter
                new_content = re.sub(
                    r'^---\s*\n.*?\n---\s*\n',
                    f'---\n{new_frontmatter}---\n',
                    content,
                    flags=re.DOTALL
                )
                
                # 写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"已修复：{file_path.name}")
                fixed_count += 1
            else:
                print(f"正常：{file_path.name}")
                
        except Exception as e:
            print(f"错误：处理 {file_path.name} 时出错: {e}")
    
    print(f"\n修复完成！共修复了 {fixed_count} 个文件")

def update_layout_file():
    """更新_layouts/post.html文件中的搜索功能"""
    layout_file = Path('_layouts/post.html')
    
    if not layout_file.exists():
        print(f"错误：{layout_file} 文件不存在")
        return
    
    try:
        with open(layout_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找并替换搜索数据部分
        search_pattern = r'// 文章数据.*?const blogPosts = \[.*?\];'
        
        new_search_data = '''// 文章数据 - 从JSON文件加载
        let blogPosts = [];

        // 加载文章数据
        async function loadBlogPosts() {
            try {
                const response = await fetch('/posts-data.json');
                const data = await response.json();
                blogPosts = data.posts;
            } catch (error) {
                console.error('加载文章数据失败:', error);
                // 如果加载失败，使用默认数据
                blogPosts = [
                    {
                        title: "Ubuntu 安装宝塔面板教程",
                        excerpt: "宝塔面板是一款简单好用的服务器运维管理面板，支持一键部署 LNMP/LAMP、网站、数据库、FTP 等，极大简化了服务器管理。",
                        url: "/2024/06/12/ubuntu-bt-panel.html",
                        date: "2024-06-12",
                        categories: ["Linux", "运维"],
                        tags: ["宝塔", "Ubuntu", "面板", "运维"]
                    }
                ];
            }
        }'''
        
        # 替换搜索数据
        new_content = re.sub(search_pattern, new_search_data, content, flags=re.DOTALL)
        
        # 更新搜索函数
        search_func_pattern = r'function performSearch\(\) \{.*?\}'
        new_search_func = '''async function performSearch() {
            const searchInput = document.getElementById('searchInput');
            const searchResults = document.getElementById('searchResults');
            const query = searchInput.value.trim().toLowerCase();

            if (query.length === 0) {
                searchResults.classList.remove('active');
                return;
            }

            // 确保文章数据已加载
            if (blogPosts.length === 0) {
                await loadBlogPosts();
            }

            const results = blogPosts.filter(post => {
                const searchText = `${post.title} ${post.excerpt} ${post.categories.join(' ')} ${post.tags.join(' ')}`.toLowerCase();
                return searchText.includes(query);
            });

            displaySearchResults(results);
        }'''
        
        new_content = re.sub(search_func_pattern, new_search_func, new_content, flags=re.DOTALL)
        
        # 更新初始化代码
        init_pattern = r'document\.addEventListener\(''DOMContentLoaded'', function \(\) \{.*?\}\);'
        new_init_code = '''document.addEventListener('DOMContentLoaded', async function () {
            const savedTheme = localStorage.getItem('theme') || 'light';
            const html = document.documentElement;
            const themeIcon = document.getElementById('theme-icon');

            html.setAttribute('data-theme', savedTheme);

            // Update button state
            if (savedTheme === 'dark') {
                themeIcon.textContent = '☀️';
            } else {
                themeIcon.textContent = '🌙';
            }

            // 加载文章数据
            await loadBlogPosts();
        });'''
        
        new_content = re.sub(init_pattern, new_init_code, new_content, flags=re.DOTALL)
        
        # 写回文件
        with open(layout_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("已更新 _layouts/post.html 文件")
        
    except Exception as e:
        print(f"错误：更新布局文件时出错: {e}")

def main():
    """主函数"""
    print("开始修复文章搜索和标签同步问题...")
    
    # 1. 修复文章front matter
    print("\n1. 修复文章front matter...")
    fix_post_frontmatter()
    
    # 2. 提取文章数据
    print("\n2. 提取文章数据...")
    posts_data = extract_posts_data()
    
    if not posts_data:
        print("没有找到有效的文章数据")
        return
    
    # 3. 生成posts-data.json
    print("\n3. 生成posts-data.json...")
    generate_posts_json(posts_data)
    
    # 4. 更新布局文件
    print("\n4. 更新布局文件...")
    update_layout_file()
    
    print("\n修复完成！")
    print("现在搜索功能应该可以正常工作了，标签也会与文章保持同步。")

if __name__ == '__main__':
    main() 