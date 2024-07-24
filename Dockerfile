FROM python:3.12-slim

# Install gettext for translations
RUN apt-get update && apt-get install -y gettext postgresql-client && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

# Copy entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create a non-root user and give access to the work directory
RUN useradd -m user
RUN chown -R user:user /code
USER user

ENTRYPOINT ["/entrypoint.sh"]