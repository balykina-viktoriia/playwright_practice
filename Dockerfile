# Use the official Playwright image with Python support
FROM mcr.microsoft.com/playwright/python:v1.60.0-jammy

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first 
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Default command: run the tests
CMD ["pytest", "--html=reports/report.html", "--self-contained-html"]