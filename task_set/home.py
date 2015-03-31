from locust import HttpLocust, TaskSet, task

class Tasks(TaskSet):
    @task(10)
    def getHome(self):
        self.client.get("/")

class Locust(HttpLocust):
    task_set = Tasks
    min_wait = 1000
    max_wait = 5000
