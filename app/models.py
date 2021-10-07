from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class EditorModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = RichTextField(blank=True, null=True)
