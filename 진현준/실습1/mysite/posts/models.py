from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length= 50)
  writer = models.CharField(max_length= 50)
  content = models.TextField()

  pub_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
  