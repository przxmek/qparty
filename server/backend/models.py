from django.contrib.sessions.models import Session
from django.db import models


class Song(models.Model):
    service_id = models.CharField(max_length=50)
    voting_result = models.IntegerField(default=0)


class Party(models.Model):
    tag = models.CharField(max_length=50)
    songs = models.ManyToManyField(Song)

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


class User(models.Model):
    session = models.ForeignKey(Session)
    party = models.ForeignKey(Party, blank=True, null=True)
    upvoted_songs = models.ManyToManyField(Song, related_name='upvoters')
    downvoted_songs = models.ManyToManyField(Song, related_name='downvoters')

    def upvote_song(self, song):
        if song in self.upvoted_songs:
            raise Exception("Already upvoted")
        elif song in self.downvoted_songs:
            self.downvoted_songs.remove(song)
            song.voting_result += 1
        self.upvoted_songs.add(song)
        song.voting_result += 1
        self.save()
        song.save()

    def downvote_song(self, song):
        if song in self.downvoted_songs:
            raise Exception("Already downvoted")
        elif song in self.upvoted_songs:
            self.upvoted_songs.remove(song)
            song.voting_result -= 1
        self.downvoted_songs.add(song)
        song.voting_result -= 1
        self.save()
        song.save()
