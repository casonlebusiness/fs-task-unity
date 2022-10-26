from django.db import models

class Email(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default="subscribed")

    def __str__(self) -> str:
        return self.email
