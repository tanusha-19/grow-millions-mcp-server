FROM python:3.11-slim-bookworm AS base
COPY --from=ghcr.io/astral-sh/uv:0.5.11 /uv /bin/uv

WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

COPY --from=public.ecr.aws/awslambda/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter

COPY pyproject.toml uv.lock ./
RUN uv pip install --no-cache -r pyproject.toml

COPY . .

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]