from django.db import models


class Message(models.Model):
    first_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    doctor = models.CharField(max_length=60)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name}'


class Doctor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    profession = models.CharField(max_length=40)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class News(models.Model):
    image = models.ImageField(upload_to='static/img/')
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Review(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    review = models.CharField(max_length=200)
    data_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, default='static/img/testimonial-2', upload_to='static/img/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
