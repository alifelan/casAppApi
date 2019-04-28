from django.db import models

# Create your models here.


class Casa(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=50)
    date = models.DateTimeField()


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    maps = models.TextField()
    photo = models.TextField()


class Teacher(models.Model):
    """Teacher model."""

    teacher_name = models.CharField(max_length=40)

    def __str__(self):
        """Return string."""
        return self.teacher_name


class Class(models.Model):
    """Class model."""

    class_id = models.CharField(max_length=6, primary_key=True)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        """Return string."""
        return "%s %s" % (self.class_id, self.class_name)


class Date(models.Model):
    """Date model."""

    day = models.PositiveSmallIntegerField()
    time = models.TimeField()

    def __str__(self):
        """Return string."""
        day_names = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves',
                     'Viernes', 'Sabado']
        return "%s a las %s" % (day_names[self.day],
                                self.time.strftime("%H:%M"))

    class Meta:
        """Meta."""

        unique_together = (("day", "time"),)


class Group(models.Model):
    """Group model."""

    class_id = models.ForeignKey(Class, related_name='groups',
                                 on_delete=models.CASCADE)
    group_number = models.IntegerField()
    teachers = models.ManyToManyField(Teacher, related_name='groups')
    semester = models.CharField(max_length=6)
    dates = models.ManyToManyField(Date, related_name='groups')

    def __str__(self):
        """Return string."""
        return "%s %s grupo %s" % (self.class_id.class_id,
                                   self.class_id.class_name, self.group_number)

    class Meta:
        """Meta."""

        unique_together = (("group_number", "class_id", "semester"),)


class User(models.Model):
    name = models.CharField(max_length=50)
    mat = models.CharField(max_length=9, primary_key=True)
    password = models.CharField(max_length=50)
    casa = models.ForeignKey(to=Casa, related_name="users", on_delete=models.CASCADE)
    events = models.ManyToManyField(to=Event, related_name="events")
    enrolled_in = models.ManyToManyField(to=Group, related_name='students')
