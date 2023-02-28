from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Poll, Vote
from .serializers import PollSerializer,PollsSerializer
from rest_framework.decorators import api_view


@api_view(["GET"])
def list_polls(request):
    serialized_polls = PollsSerializer(Poll.objects.all(), many=True)
    return JsonResponse({'polls': serialized_polls.data}, safe=False)


@api_view(["GET"])
def show_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    serialized_poll = PollSerializer(poll)
    return JsonResponse(serialized_poll.data)


