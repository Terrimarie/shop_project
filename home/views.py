from django.shortcuts import render

# Create your views here.
# code from boutique abo
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
