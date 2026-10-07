from locust import HttpUser, task, between


class URLShortenerUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def redirect(self):
        self.client.get("/4", allow_redirects=False)