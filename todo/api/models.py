from django.db import models
from django.contrib import admin


class Context(models.Model):
    context_choices = (
        ('Lt', 'Laptop'),
        ('Tb', 'Table'),
        ("Ho", "Home"),
        ("He", "High Energy"),
        ("Le", "Low Energy"),
        ("In", "Incremental"),
        ("As", "Assignment/SS"),
        ("Ph", "Phone"),
        ("Gn", "General"),
        ("Md", "Mom/Dad"),
    )

    context_name = {
        'Lt': 'Laptop',
        'Tb': 'Table',
        "Ho": "Home",
        "He": "High Energy",
        "Le": "Low Energy",
        "In": "Incremental",
        "As": "Assignment/SS",
        "Ph": "Phone",
        "Gn": "General",
        "Md": "Mom/Dad",
    }
    name = models.CharField(max_length=2, choices=context_choices)

    def __str__(self):
        return self.context_name[self.name]


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    recurring = models.BooleanField(default=False, blank=True, null=True)
    contexts = models.ManyToManyField(Context, related_name="context")

    def __str__(self):
        return self.title
