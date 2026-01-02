# Dockerfile for Jekyll static site
# This ensures Zeabur doesn't mistake this for a Rails app

FROM ruby:3.2-slim

# Install Node.js (needed for serve)
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Gemfile and Gemfile.lock
COPY Gemfile Gemfile.lock ./

# Install bundler and dependencies
RUN gem install bundler && bundle install

# Copy all files
COPY . .

# Build Jekyll site
RUN bundle exec jekyll build

# Install serve globally
RUN npm install -g serve

# Expose port (Zeabur will set PORT env var)
EXPOSE 3000

# Start static file server (NOT rails!)
CMD ["sh", "-c", "serve _site -p ${PORT:-3000}"]

