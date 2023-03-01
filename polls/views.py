from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Poll, Vote
from .serializers import PollSerializer, PollsSerializer
from rest_framework.decorators import api_view
from rest_framework import filters


@api_view(["GET"])
def list_polls(request):
    polls = Poll.objects.all().order_by('expiry_date')
    # if request.query_params.get("search"):
    #     filter_param = request.query_params.get("search")
    #     titles = Poll.objects.filter(poll_title__contains=filter_param)
    #     descriptions = Poll.objects.filter(poll_description__contains=filter_param)
    #     titles.update(descriptions)
    #     poll = titles
    serialized_polls = PollsSerializer(polls, many=True)
    return JsonResponse({'polls': serialized_polls.data}, safe=False)


@api_view(["GET"])
def show_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    serialized_poll = PollSerializer(poll)
    return JsonResponse(serialized_poll.data)


