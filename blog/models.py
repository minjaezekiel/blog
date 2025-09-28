from django.db import models

# By Ezekiel Minja
# M Enterprises

#blog model
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.title}"
