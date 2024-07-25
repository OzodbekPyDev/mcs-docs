# MCS Docs

## Overview
MCS Docs is a document management system built using modern web development frameworks. The project utilizes **FastAPI** for the backend, **SQLAlchemy** for ORM, and **Alembic** for database migrations. The architecture adheres to **Domain-Driven Design (DDD)** and **Clean Architecture (CA)** principles, ensuring a modular and maintainable codebase.

## Features
- **FastAPI:** Efficient backend framework.
- **SQLAlchemy:** ORM for database operations.
- **Alembic:** Handles database migrations.
- **DDD & CA:** Promotes separation of concerns and modularity.

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Python 3.x

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/OzodbekPyDev/mcs-docs.git
   cd mcs-docs
   ```

2. **Set up the environment:**
   - Create a `.env` file for environment variables based on `.env-test`.

3. **Build and run the Docker container:**
   ```bash
   docker-compose up --build
   ```

### Docs of API routers
Access the application at `http://localhost:8000/docs`.

## Contributing
Contributions are welcome! Please open issues or submit pull requests.
