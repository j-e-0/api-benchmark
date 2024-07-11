# locustfile.py
from locust import HttpUser, task

class APIUser(HttpUser):
    
    @task
    def test_endpoint(self):
        self.client.get("/endpoint")