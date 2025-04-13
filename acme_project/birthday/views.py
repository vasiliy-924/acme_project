from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday

class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10

class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list') 

class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list') 

class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list') 

