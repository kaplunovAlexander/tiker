from django.db import models


class RequestLog(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    remote_addr = models.GenericIPAddressField()
    query_params = models.TextField()
    user_agent = models.TextField()
    text_param = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.method} {self.path} at {self.timestamp}"