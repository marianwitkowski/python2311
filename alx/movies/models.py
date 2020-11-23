from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

### Klasa z komentarzami
class Comment(models.Model):
    body = models.TextField()
    stars = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.stars} - {self.body}"

    class Meta:
        verbose_name = "komentarz"
        verbose_name_plural = "komentarze"

### Klasa przechowująca informacje o aktorze
class Actor(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "aktor"
        verbose_name_plural = "aktorzy"

### Klasa przechowująca dane o filmie
class Movie(models.Model):
    MPAA = (
        ("-", "Brak"),
        ("G", "Dla wszystkich"),
        ("PG-13", "Za zgodą rodziców"),
        ("NC-17", "Tylko powyżej 17 lat")
    )

    title = models.CharField(max_length=255, verbose_name="tytuł")
    description = models.TextField(default="", verbose_name="opis")
    released = models.DateField(null=True, blank=True, verbose_name="data premiery")
    year = models.IntegerField(null=True, blank=True, editable=False)
    imdb = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name="imdb" )
    poster = models.ImageField(null=True, blank=True, verbose_name="plakat", unique=False, upload_to="%Y%m%d" )
    trailer = models.URLField(null=True, blank=True, verbose_name="trailer")

    created = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    mpaa_rating = models.CharField(choices=MPAA, verbose_name='mpaa', max_length=10, default='-')

    # Relacje
    actors = models.ManyToManyField(Actor, verbose_name="aktorzy", null=True)

    def __str__(self):
        return f"{self.title} - {self.year if self.year else 'BRAK DATY' }"

    def save(self, *args, **kwargs):
        if self.released:
            self.year = self.released.year
        super(Movie, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmy"