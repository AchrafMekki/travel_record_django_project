from django.db import models

# Create your models here.


class SatisfactionLevel(models.Model):
    SATISFACTION_CHOICE = {
                'Very Unsatisfied': 'Very Unsatisfied',
                'Unsatisfied': 'Unsatified',
                'Neutral': 'Neutral',
                'Satisfied': 'Satisfied',
                'Very Satisfied': 'Very Satisfied'
            }
    satisfaction_id = models.AutoField(primary_key=True)
    satisfaction_value = models.CharField(max_length=20, choices=SATISFACTION_CHOICE, default='Neutral')

    def __str__(self):
        return self.satisfaction_value