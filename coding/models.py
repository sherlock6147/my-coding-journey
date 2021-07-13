from django.db import models
from django.db.models.base import Model
from model_utils import Choices
# Create your models here.
class ProblemTag(models.Model):
    value = models.CharField("Tag name",max_length=200)
    bg_color = models.CharField("Background Color",max_length=6)
    def __str__(self):
        return self.value

class TheoryTopic(models.Model):
    name = models.CharField("Topic",max_length=100)
    def __str__(self):
        return self.name

class TheoryNote(models.Model):
    topic= models.ForeignKey(TheoryTopic,on_delete=models.CASCADE)
    note = models.TextField("Note")
    def __str__(self) -> str:
        return self.topic

class Problem(models.Model):
    statement = models.TextField("Problem Statement")
    tags = models.ManyToManyField(ProblemTag,"Problem_Tags")
    date = models.DateField("problem date")
    link = models.CharField("Link to problem",max_length=200)
    solution = models.TextField("Solution to problem")
    num_attempts = models.IntegerField("No. of attempts")
    STATUS = Choices(('todo', ('todo')), ('repeat', ('repeat')),('done',('done')))
    status = models.CharField(choices=STATUS, default=STATUS.todo, max_length=20)
    def __str__(self) -> str:
        return self.statement

class ProblemNote(models.Model):
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    value = models.TextField("Note")
    def __str__(self):
        return self.value

class Attempt(models.Model):
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    time = models.IntegerField("Time taken")
    def __str__(self) -> str:
        return 'Attempt'+str(Problem.objects.get(id=self.problem.id).num_attempts)

class Score(models.Model):
    attempt = models.ForeignKey(Attempt,on_delete=models.CASCADE)
    SCORECHOICES = Choices((0, 'ZERO',('ZERO')), (1,'ONE', ('ONE')),(2,'TWO',('TWO')),(3,'THREE',('THREE')),(4,'FOUR',('FOUR')),(5,'FIVE',('FIVE')))
    under_30 = models.IntegerField(choices=SCORECHOICES,default=SCORECHOICES.ZERO)
    need_hints = models.IntegerField(choices=SCORECHOICES,default=SCORECHOICES.ZERO)
    was_optimal = models.IntegerField(choices=SCORECHOICES,default=SCORECHOICES.ZERO)
    any_bugs = models.IntegerField(choices=SCORECHOICES,default=SCORECHOICES.ZERO)
    score = models.IntegerField(default=0)
    def save(self,*args, **kwargs):
        self.score = self.under_30+self.need_hints+self.was_optimal+self.any_bugs
        super(Score,self).save(*args, **kwargs)
    def __str__(self):
        return str(Attempt.objects.get(id=self.attempt.id))+' Score '+str(self.score)