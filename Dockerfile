# DragonCrawl Multi-stage Docker Build
# Optimized for AI/ML workloads with production-ready deployment

# Base stage with Python and system dependencies
FROM python:3.12-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd --gid 1001 dragoncrawl && \
    useradd --uid 1001 --gid dragoncrawl --shell /bin/bash --create-home dragoncrawl

# Set working directory
WORKDIR /app

# Development stage
FROM base as development

# Install development dependencies
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

# Install pre-commit
RUN pip install pre-commit

# Copy source code
COPY --chown=dragoncrawl:dragoncrawl . .

# Install package in development mode
RUN pip install -e .

# Switch to non-root user
USER dragoncrawl

# Expose port for FastAPI development server
EXPOSE 8000

# Development command
CMD ["uvicorn", "dragoncrawl.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Production dependencies stage
FROM base as deps

# Copy requirements files
COPY requirements.txt .

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM deps as production

# Copy source code
COPY --chown=dragoncrawl:dragoncrawl src/ ./src/
COPY --chown=dragoncrawl:dragoncrawl setup.py .
COPY --chown=dragoncrawl:dragoncrawl README.md .

# Install package
RUN pip install --no-cache-dir .

# Create directories for models and data
RUN mkdir -p /app/models /app/data /app/logs && \
    chown -R dragoncrawl:dragoncrawl /app

# Switch to non-root user
USER dragoncrawl

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import dragoncrawl; print('Health check passed')" || exit 1

# Production command
CMD ["python", "-m", "dragoncrawl.api.main"]

# Testing stage
FROM development as testing

# Copy test files
COPY --chown=dragoncrawl:dragoncrawl tests/ ./tests/

# Run tests
RUN python -m pytest tests/ -v --cov=src/dragoncrawl --cov-report=term-missing

# GPU-enabled stage (optional)
FROM nvidia/cuda:12.1-runtime-ubuntu22.04 as gpu

# Install Python
RUN apt-get update && apt-get install -y \
    python3.12 \
    python3.12-pip \
    python3.12-dev \
    && rm -rf /var/lib/apt/lists/*

# Set Python as default
RUN ln -s /usr/bin/python3.12 /usr/bin/python

# Copy from production stage
COPY --from=production /app /app
COPY --from=production /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

WORKDIR /app

# Install GPU-specific dependencies
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
RUN pip install faiss-gpu

USER dragoncrawl

CMD ["python", "-m", "dragoncrawl.api.main"]