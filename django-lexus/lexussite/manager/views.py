from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponseRedirect


def index(request):
    if 'id_client' not in request.session:
        return HttpResponseRedirect('/')

    Request = apps.get_model('index', 'Request')

    if "_logout" in request.POST:
        del request.session['id_client']
        return HttpResponseRedirect('/')

    if request.POST:
        if '_reject' in request.POST:
            obj = Request.objects.get(id=request.POST.get('_reject'))
            obj.status = 'r'
            obj.save()
        if '_accept' in request.POST:
            obj = Request.objects.get(id=request.POST.get('_accept'))
            obj.status = 'a'
            obj.save()

    all_new = Request.objects.filter(status__exact='u')
    all_accepted = Request.objects.filter(status__exact='a')
    all_rejected = Request.objects.filter(status__exact='r')
    all_orders = Request.objects.all()

    content = {
        "all_new": all_new,
        "all_accepted": all_accepted,
        "all_rejected": all_rejected,
        "all": all_orders
    }

    return render(request, 'manager/manager.html', content)

