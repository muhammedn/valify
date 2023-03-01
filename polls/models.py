from django.db import models
from django.utils import timezone


# Create your models here.

class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Poll(TimeStamps):
    poll_title = models.CharField(max_length=191)
    poll_description = models.CharField(max_length=255)
    expiry_date = models.DateTimeField('expiry date')

    def __str__(self):
        return self.poll_title

    def is_expired(self):
        return self.expiry_date < timezone.now()


class Vote(TimeStamps):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    vote_title = models.CharField(max_length=191)

    def __str__(self):
        return self.vote_title

class PollVote(TimeStamps):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)


