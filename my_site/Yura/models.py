from django.db import models
# Create your models here.




class Statistic(models.Model):
    minute_play = models.FloatField(null=True)
    total_actions = models.FloatField(null=True)
    successful = models.FloatField(null=True)
    passes = models.FloatField(null=True)
    accurate = models.FloatField(null=True)
    long_passes = models.FloatField(null=True)
    accurate_l = models.FloatField(null=True)
    duels = models.FloatField(null=True)
    won_d = models.FloatField(null=True)
    aeriels_duels = models.FloatField(null=True)
    won_a = models.FloatField(null=True)
    losses = models.FloatField(null=True)
    own_half = models.FloatField(null=True)
    recoviers = models.FloatField(null=True)
    opp_half = models.FloatField(null=True)
    yellow_card = models.FloatField(null=True)
    red_card = models.FloatField(null=True)
    

    




