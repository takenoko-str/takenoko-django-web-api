from django.db import models


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    def __str__(self):
        return '{} {}'.format(self.language_id, self.name)

    class Meta:
        managed = False
        db_table = 'language'


class Film(models.Model):
    film_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.PositiveSmallIntegerField(blank=True, null=True)
    language = models.ForeignKey('Language', models.CASCADE)
    length = models.SmallIntegerField(blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film'



