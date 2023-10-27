from django.db import models


# Create your models here.




class Statistic(models.Model):
    minute_play = models.FloatField(null=True)
    conceled_goals = models.FloatField(null=True)
    xCG = models.FloatField(null=True)
    shots_again =  models.FloatField(null=True)
    with_reflexes = models.FloatField(null=True)
    exits = models.FloatField(null=True)
    long_passes = models.FloatField(null=True)
    accurate_l = models.FloatField(null=True)
    short_passes = models.FloatField(null=True)
    accurate_sh = models.FloatField(null=True)
    goal_kicks = models.FloatField(null=True)
    

