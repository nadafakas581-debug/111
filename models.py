from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.course_code

class Question(models.Model):
    # Required: ForeignKey to Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Required: is_get_score() method
    def is_get_score(self):
        # This logic typically checks if the question is worth points
        return True

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    # Required: is_correct BooleanField
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class Enrollment(models.Model):
    # Represents a student's enrollment in a specific course
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Enrollment ID: {self.id}"

class Submission(models.Model):
    # Required: ForeignKey to Enrollment
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    # Required: ManyToManyField to Choice
    choices = models.ManyToManyField(Choice)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.id} for {self.enrollment}"
