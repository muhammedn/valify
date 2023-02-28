from rest_framework import serializers
from .models import Poll, Vote


class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'vote_title']


class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'poll_title']


class PollSerializer(serializers.ModelSerializer):
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ['id', 'poll_title', 'poll_description', 'votes']

    def get_votes(self, key):
        votes = Vote.objects.filter(poll=key)
        serialized_votes = VotesSerializer(votes, many=True)
        return serialized_votes.data
