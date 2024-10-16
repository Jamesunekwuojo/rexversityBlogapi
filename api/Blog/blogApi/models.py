from django.db import models

# Create your models here.
class BlogPost(models.Model):  # This gets all of the basic functionality of a database model
    title = models.CharField(max_length=255)

    content = models.TextField()

    published_date = models.DateTimeField(auto_now_add=True) # Don't need to manually set the time. it's going to automatically fill in the publishhed data.


    def __str__(self) : 
        return self.title
    