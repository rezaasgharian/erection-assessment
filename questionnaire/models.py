from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Questionnaire(models.Model):
    CONFIDENCE_CHOICES = (
        (1, 'Very low'),
        (2, 'Low'),
        (3, 'Moderate'),
        (4, 'High'),
        (5, 'Very high'),
    )
    PENETRATION_CHOICES = (
        (1, 'Almost never or never'),
        (2, 'A few times'),
        (3, 'Sometimes'),
        (4, 'Most times'),
        (5, 'Almost always or always'),
    )
    INTERCOURSE_CHOICES = (
        (1, 'Almost never or never'),
        (2, 'A few times'),
        (3, 'Sometimes'),
        (4, 'Most times'),
        (5, 'Almost always or always'),
    )
    COMPLETION_CHOICES = (
        (1, 'Extremely difficult'),
        (2, 'Very difficult'),
        (3, 'Difficult'),
        (4, 'Slightly difficult'),
        (5, 'Not difficult'),
    )
    SATISFACTION_CHOICES = (
        (1, 'Almost never or never'),
        (2, 'A few times'),
        (3, 'Sometimes'),
        (4, 'Most times'),
        (5, 'Almost always or always'),
    )
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, blank=False, null=False)
    confidence = models.PositiveSmallIntegerField(choices=CONFIDENCE_CHOICES)
    penetration = models.PositiveSmallIntegerField(choices=PENETRATION_CHOICES)
    intercourse = models.PositiveSmallIntegerField(choices=INTERCOURSE_CHOICES)
    completion = models.PositiveSmallIntegerField(choices=COMPLETION_CHOICES)
    satisfaction = models.PositiveSmallIntegerField(choices=SATISFACTION_CHOICES)
    score = models.IntegerField(validators=[MaxValueValidator(25), MinValueValidator(5)], null=False, blank=False)
    average = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


