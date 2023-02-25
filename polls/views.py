from django.http import JsonResponse
from .models import Poll
from .serializers import PollSerializer
from rest_framework.decorators import api_view


@api_view(["GET"])
def list_polls(request):
    serialized_polls = PollSerializer(Poll.objects.all(), many=True)
    return JsonResponse({'polls': serialized_polls.data}, safe=False)
