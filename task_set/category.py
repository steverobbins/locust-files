from locust import HttpLocust, TaskSet, task

categoryPage = "/mens.html"

class Tasks(TaskSet):
    @task(10)
    def getCategory(self):
        self.client.get(categoryPage)

    @task(10)
    def getCategoryParamFilter(self):
        self.client.get(categoryPage + "?size=5158")

    @task(10)
    def getCategoryParamNonFilter(self):
        self.client.get(categoryPage + "?utm_campaign=test_123")

class Locust(HttpLocust):
    task_set = Tasks
    min_wait = 1000
    max_wait = 5000
