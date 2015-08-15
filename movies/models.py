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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('updated',)
    def __unicode__(self):
        return '%d' % (self.name)


class MovieScreenshot(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="movie_screenshots")
    file = models.ImageField(_("Movie Banner"), upload_to='movie/banner/')
    is_cover_photo = models.TextField(_("Is this movie's cover photo?"))
    launched_date = models.DateField(_("Movie Release Date"))
    priority = models.IntegerField(_("Movie Screenshot Order"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('updated',)
    def __unicode__(self):
        return '%d' % (self.id)

class MovieVideo(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="movie_trailers")
    file = models.FileField(_("Movie Trailer"), upload_to='movie/trailer/')
    launched_date = models.DateField(_("Movie Release Date"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('updated',)
    def __unicode__(self):
        return '%d' % (self.id)

class MovieAward(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="movie_for_award")
    award_id = models.ForeignKey(Award, related_name="award_for_movie")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('updated',)
    def __unicode__(self):
        return '%d' % (self.id)

class MovieRating(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="mr_movie")
    user_id = models.ForeignKey(User, related_name="mr_user")
    rating = models.CharField(_("Movie Rating"), max_length=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('updated',)
    def __unicode__(self):
        return '%d' % (self.id)

class MovieActor(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="movie_actors")
    actor_id = models.ForeignKey(Actor, related_name="actor_object")
    role = models.CharField(_("Movie Role"), max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('updated',)
    def __unicode__(self):
        return '%d' % (self.id)
