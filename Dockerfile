## ------------------------------- Builder Stage ------------------------------ ##
FROM python:3.12-bookworm AS builder

# Install build tools for dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install uv
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod +x /install.sh && /install.sh && rm /install.sh

# Set UV path
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy pyproject.toml and install dependencies into .venv
COPY pyproject.toml .
RUN uv venv && uv pip install -e .  # optional: -e . for editable if needed

## ------------------------------- Production Stage ------------------------------ ##
FROM python:3.12-bookworm AS production

# Set working directory
WORKDIR /app

# Copy app source code
COPY . .

# Copy virtual environment from builder
COPY --from=builder /app/.venv .venv

# Activate venv in PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose FastAPI port (default 8080)
EXPOSE 8080

# Start app with Uvicorn
CMD ["uvicorn", "main:app", "--log-level", "info", "--host", "0.0.0.0", "--port", "8080"]
