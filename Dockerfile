# 1. Add AWS Lambda Web Adapter
FROM --platform=$TARGETPLATFORM public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 AS adapter

# 2. Base Python environment matching Python 3.13
FROM python:3.13-slim

WORKDIR /app

# Copy Lambda Adapter extension
COPY --from=adapter /lambda-adapter /opt/extensions/lambda-adapter

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

# Install uv for fast dependency installation
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy configuration files and install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache

# Copy application source code
COPY . .

# Create non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

# Start FastMCP server module
CMD ["uv", "run", "python", "-m", "app.mcp.server"]