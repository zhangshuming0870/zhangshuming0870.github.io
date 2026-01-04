# Dockerfile for Jekyll static site
# This ensures Zeabur doesn't mistake this for a Rails app
# Optimized for smaller image size

FROM ruby:3.2-slim

# Install Node.js and build tools (needed for serve and Jekyll)
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy Gemfile and Gemfile.lock first (for better caching)
COPY Gemfile Gemfile.lock ./

# Install bundler and dependencies
RUN gem install bundler && \
    bundle install --deployment --without development test && \
    rm -rf ~/.gem/cache

# Copy source files (excluding files in .dockerignore)
COPY . .

# Build Jekyll site
RUN bundle exec jekyll build

# Clean up build dependencies and cache to reduce image size
RUN apt-get purge -y build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    npm cache clean --force && \
    rm -rf ~/.gem/cache

# Install serve globally
RUN npm install -g serve

# Expose port (Zeabur will set PORT env var)
EXPOSE 3000

# Start static file server (NOT rails!)
CMD ["sh", "-c", "serve _site -p ${PORT:-3000}"]

