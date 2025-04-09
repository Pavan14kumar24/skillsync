from django.db import models
from django.contrib.auth.models import User

# Skill Model
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Course Model
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    platform = models.CharField(max_length=100)
    url = models.URLField()
    progress = models.IntegerField(default=0)  # New field for progress tracking

    def __str__(self):
        return self.title


class CourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)  # Progress in percentage (0-100)
    badge_awarded = models.BooleanField(default=False)  # New field

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} - {self.course.title}: {self.progress}%"


class SkillProficiency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'skill')

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} on {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"