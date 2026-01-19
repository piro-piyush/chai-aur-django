from django.shortcuts import render, get_object_or_404
from .models import Chai, ChaiReview, ChaiStore
from .forms import ChaiStoreSearchForm

# Chai list
def chai(request):
    chais = Chai.objects.all()
    return render(request, 'chai/chai.html', {'chais': chais})


# Chai detail + reviews
def chai_description(request, chai_id):
    chai = get_object_or_404(Chai, pk=chai_id)
    reviews = ChaiReview.objects.filter(chai=chai)

    return render(
        request,
        'chai/chai_description.html',
        {
            'chai': chai,
            'reviews': reviews,
        }
    )


# Find chai store
def find_chai_store(request):
    stores = ChaiStore.objects.all()
    form = ChaiStoreSearchForm(request.POST or None)

    if form.is_valid():
        selected_type = form.cleaned_data.get('type')
        selected_size = form.cleaned_data.get('size')

        # Filter ManyToMany related Chai objects
        if selected_type:
            stores = stores.filter(chai_varieties__type=selected_type)
        if selected_size:
            stores = stores.filter(chai_varieties__size=selected_size)

        stores = stores.distinct()

    return render(request, 'chai/find_chai_store.html', {'stores': stores, 'form': form})
