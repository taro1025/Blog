from django.urls import reverse_lazy
from django.views import generic
from .forms import ReviewCreateForm
from .models import Review


class ReviewList(generic.ListView):
    model = Review


class ReviewDetail(generic.DetailView):
    model = Review


class ReviewCreate(generic.CreateView):
    model = Review
    form_class = ReviewCreateForm
    success_url = reverse_lazy('reviews:review_list')


class ReviewUpdate(generic.UpdateView):
    model = Review
    form_class = ReviewCreateForm
    success_url = reverse_lazy('reviews:review_list')


class ReviewDelete(generic.DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')
