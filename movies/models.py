from django.utils.translation import ugettext_lazy as _
from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from awards.models import Award
from actors.models import Actor

class Movie(models.Model):
    name = models.CharField(_("Movie Name"), max_length=255)
    description = models.TextField(_("Movie Description"))
    release_date = models.DateField(_("Movie Release Date"))

class MovieScreenshot(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="movie_screenshots")
    file = models.ImageField(_("Movie Banner"))
    is_cover_photo = models.TextField(_("Is this movie's cover photo?"))
    launched_date = models.DateField(_("Movie Release Date"))
    priority = models.IntegerField(_("Movie Screenshot Order"))

class MovieVideo(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="movie_trailers")
    file = models.FileField(_("Movie Trailer"))
    launched_date = models.DateField(_("Movie Release Date"))

class MovieAward(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="movie_for_award")
    award_id = models.ForeignKey(Award, related_name="award_for_movie")

class MovieRating(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="mr_movie")
    user_id = models.ForeignKey(User, related_name="mr_user")
    rating = models.CharField(_("Movie Rating"), max_length=3)

class MovieActor(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="mva_movie")
    actor_id = models.ForeignKey(Actor, related_name="mva_actor")
    role = models.CharField(_("Movie Role"), max_length=255)
