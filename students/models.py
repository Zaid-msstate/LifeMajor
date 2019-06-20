from django.db import models


INSTITUTION_LEVELS = [
        ('HS', 'High School'),
        ('CL', 'College'),
        ]


class Institution(models.Model):
    name = models.CharField(max_length=30)
    level = models.CharField(max_length=30, choices=INSTITUTION_LEVELS)

    def __str__(self):
        return str(self.name)


class Department(models.Model):
    name = models.CharField(max_length=30)
    school = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Major(models.Model):
    name = models.CharField(max_length=30)
    host = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class MajorCategory(models.Model):
    name = models.CharField(max_length=30)
    child = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name="child_parent")
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name="parent_child")
