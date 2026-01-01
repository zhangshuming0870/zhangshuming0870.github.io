#!/bin/bash
set -e

echo "Installing bundler..."
gem install bundler

echo "Installing dependencies..."
bundle install

echo "Building Jekyll site..."
bundle exec jekyll build

echo "Build completed successfully!"

