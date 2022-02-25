from audioop import reverse
from platform import release
from turtle import title
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import Tvshow, Network
from datetime import datetime


def redirigir(request):
    return redirect('/shows')


def index(request):
    context = {
        'alltvshows': Tvshow.objects.all(),
        'allnetworks': Network.objects.all(),
    }
    return render(request, 'app/index.html', context)


def newtvshow(request):
    return render(request, 'app/formulario_new.html')


def createtvshow(request):
    if request.method == 'POST':
        if Network.objects.all().filter(name=request.POST['network']):
            print(Network.objects.all().filter(name=request.POST['network']))
            networks_query = Network.objects.all().filter(
                name=request.POST['network'])
            for query in networks_query:
                this_network = Network.objects.get(id=query.id)
                print(this_network.name)
                print(this_network.id)
                tv_show = Tvshow.objects.create(
                    title=request.POST['title'], network=this_network, releasedate=request.POST['releasedate'], description=request.POST['description'])
                print(tv_show.__dict__)
                showid = tv_show.id
            return redirect(f"/shows/{showid}")
        else:
            print(request.POST)
            create = Tvshow.objects.create(title=request.POST['title'], network=Network.objects.create(name=request.POST['network']),
                                           releasedate=request.POST['releasedate'], description=request.POST['description'])
            showid = create.id
            return redirect(f"/shows/{showid}")


def details(request, id):
    detalle = Tvshow.objects.get(id=id)
    context = {
        "detailstvshow": detalle,
    }
    return render(request, 'app/detalle.html', context)


def edit(request, id):
    if request.method == 'GET':
        editar = Tvshow.objects.get(id=id)
        network = editar.network.name
        release_date = editar.releasedate
        release_date = release_date.strftime('%Y-%m-%d')
        print(release_date)
        context = {
            "edit": editar,
            "release_date": release_date,
            "network": network
        }
    return render(request, 'app/formulario_edit.html', context)


def update(request, id):
    print(request.POST)
    update = Tvshow.objects.get(id=id)
    update_network = Network.objects.get(id=update.network.id)
    update.title = request.POST['title']
    update_network.name = request.POST['network']
    update.description = request.POST['description']
    update.releasedate = request.POST['releasedate']
    update_network.save()
    update.save()
    return redirect(f"/shows/{id}")


def destroy(request, id):
    print(request.POST)
    deleteshow = Tvshow.objects.get(id=id)
    deleteshow.delete()
    return redirect("/shows")
