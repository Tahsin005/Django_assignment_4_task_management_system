from django.db import models
from category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(CategoryModel)
    def __str__(self) -> str:
        return f'Title : {self.task_title}'