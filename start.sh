#!/bin/bash

# Betting Payment Manager - Docker Quick Start Script

set -e

echo "🚀 Starting Betting Payment Manager Stack..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from .env.example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "✅ Created .env file. Please review and update if needed."
    else
        echo "❌ .env.example not found. Please create .env manually."
        exit 1
    fi
fi

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker Desktop."
    exit 1
fi

# Build and start services
echo "📦 Building and starting services..."
docker-compose up -d --build

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

# Check service status
echo ""
echo "📊 Service Status:"
docker-compose ps

echo ""
echo "✅ Services are starting!"
echo ""
echo "📍 Access your services:"
echo "   Frontend:  http://localhost:5174"
echo "   API:       http://localhost:3001/api/v1"
echo "   Health:    http://localhost:3001/health"
echo "   Adminer:   http://localhost:8081"
echo ""
echo "📝 To seed the database:"
echo "   docker-compose exec api npm run db:seed"
echo ""
echo "📋 To view logs:"
echo "   docker-compose logs -f"
echo ""
echo "🛑 To stop services:"
echo "   docker-compose down"
echo ""

