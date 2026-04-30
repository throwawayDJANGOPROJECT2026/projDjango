#!/bin/bash

# Django development server runner for macOS/Linux
cd "$(dirname "$0")"

if [ ! -f "venv/bin/python" ]; then
    echo "❌ Virtual environment not found!"
    echo ""
    echo "Please run setup first:"
    echo "  python setup.py"
    exit 1
fi

echo ""
echo "============================================================"
echo "🚀 Starting Django Development Server"
echo "============================================================"
echo ""
echo "✅ Server starting on http://localhost:8000"
echo "📝 Press Ctrl+C to stop the server"
echo "============================================================"
echo ""

venv/bin/python manage.py runserver
