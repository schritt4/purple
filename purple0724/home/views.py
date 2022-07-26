from django.shortcuts import get_object_or_404, render
from curation.models import Curation

# Create your views here.
def home(request):
    curation_index = Curation.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'curation_index':curation_index})

def search(request):
    return render(request, 'search.html')

def c_detail(request, curation_id):
    curation = get_object_or_404(Curation, pk=curation_id)
    return render(request, 'c_detail.html', {'curation':curation})