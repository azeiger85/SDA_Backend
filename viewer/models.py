from django.db import models

class Genre(models.Model):
    """
    with the help of the django ORM this will be translated eto a data table
    """
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Movie(models.Model):
  title = models.CharField(max_length=128)
  genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
  rating = models.IntegerField()
  released = models.DateField()
  description = models.TextField()
  created = models.DateTimeField(auto_now_add=True)


  def __str__(self):
      return self.title

