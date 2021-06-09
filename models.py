from django.db import models

class Grade(models.Model):
    grade =models.IntegerField()
    test_id = models.IntegerField()

    


class Test(models.Model):
    name = models.CharField(max_length=200)
    question = models.IntegerField()

    def __str__(self):
        return self.name


class Questions(model.Models):
    title = models.TextField()
    right_answer = models.IntegerField()
    answers = models.JSONField()

    def __str__(self):
        return self.title


class Answers(model.Models):
    content = models.TextField()

    

