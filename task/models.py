from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'Title : {self.task_title}'