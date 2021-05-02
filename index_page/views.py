from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import PackageDetail
from django.db.models import Q



def index_view(request):
    return render(request, 'index/index.html')

def about_us(request):
    return render(request, 'index/about.html')


def contact_us(request):
    return render(request, 'index/contact.html')

#def factoryFunc(request, template_name):
    #return render(request, template_name)


class Home(ListView):
    model = PackageDetail
    template_name = 'index/index.html'
    context_object_name = 'details'

    def get_queryset(self):
        quary = self.request.GET.get('q')
        if quary:
            object_list = PackageDetail.objects.filter(Q(tracking_number__icontains=quary))
            return object_list
        else:
            object_list = PackageDetail.objects.all()


class Package(ListView):
    model = PackageDetail
    template_name = 'index/tracker.html'
    context_object_name = 'item'


    def page(request):
        current_url = request.get_full_path()
        return render(request, 'index/tracker.html', locals())


class PostDetailView(DetailView):
    model = PackageDetail
    #context_object_name = 'posts'


"""class SearchResultView(ListView):
    model = PackageDetail
    template_name = 'index/result.html'
    #queryset = Tracker.objects.filter(order_id__icontains='rrt')
    def get_queryset(self):
        quary = self.request.GET.get('q')
        object_list = PackageDetail.objects.filter(Q(tracking_number__icontains=quary))

        return object_list
        #return HttpResponseRedirect(reverse('index_view', args=[str(quary)]))"""
    