from django.urls import path

# Create your urls here.

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json

@login_required()
def userdata(request):
    user = request.user
    return HttpResponse(
        json.dumps({
            'username': user.username
        }),
        content_type='application/json'
    )

urlpatterns = [
    path('userdata', userdata, name='userdata')

]
