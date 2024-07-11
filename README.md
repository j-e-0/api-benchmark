# API Benchmarking Project

This project contains four simple APIs implemented in different programming languages and frameworks: FastAPI (Python), Express (Node.js), Spring Boot (Java), and Gin (Go). The objective is to compare the performance of these APIs in terms of Requests Per Minute (RPM), brute force on the endpoint, memory usage, and response time.

## Project Structure

```
/api-benchmark
    /fastapi
        app.py
        Dockerfile
    /express
        app.js
        package.json
        Dockerfile
    /springboot
        src
        pom.xml
        Dockerfile
    /gin
        main.go
        go.mod
        Dockerfile
    locustfile.py
    docker-compose.yml
    README.md
```

## Prerequisites

- Docker
- Docker Compose
- Python 3.9 or higher (to run Locust)
- Pip (to install Locust)

## Setup

### Step 1: Build and Run the Containers

1. Navigate to the project's root directory `/api-benchmark`.

2. Run the following commands to build and start the Docker containers:

```bash
docker-compose build
docker-compose up
```

### Step 2: Install Locust

Install Locust using pip:

```bash
pip install locust
```

### Step 3: Run Tests with Locust

1. Run Locust:

```bash
locust -f locustfile.py
```

2. Access the Locust web interface at `http://localhost:8089`.

3. Fill in the test details (number of users and spawn rate) and click "Start".

## API Endpoints

Each API has an `/endpoint` that returns a JSON message:

- FastAPI (Python): `http://localhost:8000/endpoint`
- Express (Node.js): `http://localhost:3000/endpoint`
- Spring Boot (Java): `http://localhost:8080/endpoint`
- Gin (Go): `http://localhost:8081/endpoint`

## Resources and Limitations

The Docker containers are configured with the same resource limits to ensure a fair comparison:

```yaml
deploy:
  resources:
    limits:
      cpus: '0.50'
      memory: 512M
```

## Contribution

Feel free to open issues and pull requests for improvements and fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.