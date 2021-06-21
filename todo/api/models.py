from django.db import models


class Context(models.Model):
    context_choices = (
        ('LT', 'Laptop'),
        ('Tb', 'Table'),
        ("Ho", "Home"),
        ("HE", "High Energy"),
        ("LE", "Low Energy"),
        ("In", "Incremental"),
        ("AS", "Assignment/SS"),
        ("Ph", "Phone"),
        ("Gn", "General"),
        ("MD", "Mom/Dad"),
    )
    name = models.CharField(max_length=2, choices=context_choices)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    recurring = models.BooleanField(default=False, blank=True, null=True)
    contexts = models.ManyToManyField(Context)

    def __str__(self):
        return self.title
