from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(default='media/profile_images/default.jpg', upload_to='profile_images/')
    about = models.TextField(max_length=250)
    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions', default=True)
    title = models.CharField(max_length=150, blank=False)
    question = models.TextField(max_length=5000)
    date_asked = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='responses', default=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions', default=True)
    answer = models.TextField(max_length=5000)
    date_answered = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.answer