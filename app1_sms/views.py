from django.http import HttpResponse , JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import models
from . import forms
from rest_framework.permissions import IsAuthenticated
class smsonattenteListView(generic.ListView):
    permission_classes = (IsAuthenticated,)
    form_class = forms.smsonattenteForm
    model = models.smsonattente


class smsonattenteCreateView(generic.CreateView):
    model = models.smsonattente
    form_class = forms.smsonattenteForm


class smsonattenteDetailView(generic.DetailView):
    model = models.smsonattente
    form_class = forms.smsonattenteForm


class smsonattenteUpdateView(generic.UpdateView):
    model = models.smsonattente
    form_class = forms.smsonattenteForm
    pk_url_kwarg = "pk"


class sys_paramtListView(generic.ListView):
    model = models.sys_paramt
    form_class = forms.sys_paramtForm


class sys_paramtCreateView(generic.CreateView):
    model = models.sys_paramt
    form_class = forms.sys_paramtForm


class sys_paramtDetailView(generic.DetailView):
    model = models.sys_paramt
    form_class = forms.sys_paramtForm


class sys_paramtUpdateView(generic.UpdateView):
    model = models.sys_paramt
    form_class = forms.sys_paramtForm
    pk_url_kwarg = "pk"


class smstosendListView(generic.ListView):
    model = models.smstosend
    form_class = forms.smstosendForm


class smstosendCreateView(generic.CreateView):
    model = models.smstosend
    form_class = forms.smstosendForm


class smstosendDetailView(generic.DetailView):
    model = models.smstosend
    form_class = forms.smstosendForm


class smstosendUpdateView(generic.UpdateView):
    model = models.smstosend
    form_class = forms.smstosendForm
    pk_url_kwarg = "pk"
@api_view(['POST','GET'])
@csrf_exempt
def test(request):
    try:
        data_user=request.data["user"]
        data_password=request.data["password"]
        user = authenticate(username=data_user, password=data_password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({'key': token.key, 'id': token.user_id})
    except:
        pass
    return JsonResponse({'key': False, 'id': False})
