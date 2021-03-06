from django.contrib.sessions.models import Session
from django.db import models


class Song(models.Model):
    service_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    voting_result = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " (" + str(self.voting_result) + " votes)"


class Party(models.Model):
    tag = models.CharField(max_length=50)
    songs = models.ManyToManyField(Song)
    admins = models.ManyToManyField('User', related_name='admins')
    password = models.CharField(max_length=50)

    def init_party(self):
        self.save()
        self.tag = self.pk.__str__()
        self.save()

    def add_song(self, song):
        self.songs.add(song)
        self.save()

    def remove_song(self, song):
        self.songs.remove(song)
        self.save()

    def __str__(self):
        return "Party (tag = " + self.tag + ")"


class User(models.Model):
    session = models.ForeignKey(Session)
    party = models.ForeignKey(Party, blank=True, null=True)
    upvoted_songs = models.ManyToManyField(Song, related_name='upvoters')
    downvoted_songs = models.ManyToManyField(Song, related_name='downvoters')

    def upvote_song(self, song):
        if self.upvoted_songs.filter(pk=song.pk).count() > 0:
            return
        elif self.downvoted_songs.filter(pk=song.pk).count() > 0:
            self.downvoted_songs.remove(song)
            song.voting_result += 1
        self.upvoted_songs.add(song)
        song.voting_result += 1
        self.save()
        song.save()

    def downvote_song(self, song):
        if self.downvoted_songs.filter(pk=song.pk).count() > 0:
            return
        elif self.upvoted_songs.filter(pk=song.pk).count() > 0:
            self.upvoted_songs.remove(song)
            song.voting_result -= 1
        self.downvoted_songs.add(song)
        song.voting_result -= 1
        self.save()
        song.save()

    def __str__(self):
        return "User(Session.key = " + self.session.session_key + ", party  = " + str(self.party) + ")"
