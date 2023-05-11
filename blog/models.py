from django.db import models

class Blog(models.Model):
    date=models.DateField()
    writer=models.CharField(max_length=100)
    IP=models.DecimalField(max_digits=2,decimal_places=1)
    R=models.IntegerField()
    H=models.IntegerField()
    K=models.IntegerField()
    BB=models.IntegerField()
    W=models.IntegerField()
    L=models.IntegerField()
    HLD=models.IntegerField()
    SV=models.IntegerField()

    def __str__(self):
        return str(self.date)
