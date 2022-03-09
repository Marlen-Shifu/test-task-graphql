from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    status_choice = (
        ('later', 'later'),
        ('doing', 'doing'),
        ('done', 'done'),
    )
    status = models.CharField(max_length=255, choices=status_choice)

    def __str__(self):
        return f'{self.title}'