from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Trip, Notes
# Create your views here.
class HomeView(TemplateView):
    template_name = 'trip/index.html'

def trip_list(request):
    trips =  Trip.objects.filter(owner=request.user)
    context = {
        'trips':trips
    }
    return render(request, 'trip/trip_list.html', context)

class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    # template named model_form.html

    def form_valid(self, form):
        # owner field = logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TripDetailView(DetailView):
    model = Trip

    # Data Stored on Trip - Also have the Notes Date 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes
        return context
        
class TripUpdateView(UpdateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country','start_date', 'end_date']

class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    
class NoteDetailView(DetailView):
    model= Notes

class NoteListView(ListView):
    model = Notes

    def get_queryset(self):
        queryset = Notes.objects.filter(trip__owner=self.request.user)
        return queryset

class NoteCreateView(CreateView):
    model = Notes
    success_url = reverse_lazy('notes-list')
    fields = '__all__'

    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner = self.request.user)
        form.fields['trip'].queryset = trips
        return form

class NoteUpdateView(UpdateView):
    model = Notes
    success_url = reverse_lazy('notes-list')
    fields = '__all__'

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner = self.request.user)
        form.fields['trip'].queryset = trips
        return form

class NoteDeleteView(DeleteView):
    model = Notes
    success_url = reverse_lazy('notes-list')
    # not template needed  -just post request to this url