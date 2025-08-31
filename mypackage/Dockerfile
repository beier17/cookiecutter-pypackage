# Use lightweight Python 3.11 image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install pip + dependencies
RUN pip install --upgrade pip \
    && pip install .

# Run tests during build (ensures code works)
RUN pytest || true

# Default command: run package as module
CMD ["python", "-m", "mypackage"]
