from django.http import JsonResponse
from .models import Poll
from .serializers import PollSerializer


def index(request):
    serialized_polls = PollSerializer(Poll.objects.all(), many=True)
    return JsonResponse({'polls': serialized_polls.data}, safe=False)

