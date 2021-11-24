from django.db import models


class Sep(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    photo = models.ImageField(upload_to='media/image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sep'


class Subject(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    photo = models.ImageField(upload_to='media/image')
    deck = models.TextField()
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Subject'


class Student_Life(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    photo = models.ImageField(upload_to='media/image')
    deck = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Student_Life'
