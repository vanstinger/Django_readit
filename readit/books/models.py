from django.db import models
from django.utils.timezone import now
# Create your models here.


class Book(models.Model):
    # New things learnt. verbose_name, help_text and ManyToMany
    # Relationship
    # Refer Django Bulk method
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField("Author", related_name='books')
    review = models.TextField(blank=True, null=True)
    date_reviewed = models.DateTimeField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False, verbose_name='Favorite?')

    def __str__(self):
        # string formatting
        return "{} by {}".format(self.title, self.list_authors())

    def list_authors(self):
        # refer list comprehension
        return ", ".join([author.name for author in self.authors.all()])

    def save(self, *args, **kwargs):
        if (self.review and self.date_reviewed is None):
            self.date_reviewed = now()

        # super(Child, self).method()
        super(Book, self).save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(
        max_length=70, help_text='Use a Pen name, not a Real name')

    def __str__(self):
        return self.name
