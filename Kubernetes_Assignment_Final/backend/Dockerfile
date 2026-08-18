# Line 1: Use lightweight Python 3.11 base image to keep image size small
FROM python:3.11-slim

# Line 2: Set working directory inside the container
WORKDIR /app

# Line 3: Copy requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Line 4: Install Python dependencies without caching pip files
RUN pip install --no-cache-dir -r requirements.txt

# Line 5: Copy application code into container
COPY . .

# Line 6: Expose port 5000 for Flask application
EXPOSE 5000

# Line 7: Start production WSGI server gunicorn binding to all network interfaces
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
