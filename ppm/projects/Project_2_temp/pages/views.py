from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from . import forms

# this function is not needed but shows how default values work in python
def __f():
    return "default data to show on base url"

def homeView(request, url_data = __f()):
    data = "test data from view"

    #here we can still do some logic if we want

    return render(request, 
                  'home.html', 
                  {
                    'data': data,
                    'url_data': url_data,
                  })


def eventsView(request):
    events = models.Event.objects.all()

    return render(request, 
                  'events.html',
                  {
                      'events': events,                    
                  })

def eventView(request, event_id):
    event = models.Event.objects.get(pk=event_id)

    return render(request,
                  'event.html',
                  {
                      'event': event,
                  })

def addEventView(request):
    submitted = False

    if request.method == 'POST':
        form = forms.EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = forms.EventForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'add_event.html',
                  {
                      'form': form,
                      'submitted': submitted,
                  })

def updateEventView(request, event_id):
    event = models.Event.objects.get(pk=event_id)

    if request.method == 'POST':
        form = forms.EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/events')
    else:
        form = forms.EventForm(instance=event)

    return render(request,
                  'update_event.html',
                  {
                      'form': form,
                      'event': event,
                  })

def deleteEventView(request, event_id):
    event = models.Event.objects.get(pk=event_id)
    event.delete()

    return HttpResponseRedirect('/events')

def searchEventView(request):
    if request.method == 'POST':
        searched_event = request.POST['searched_event']
        events = models.Event.objects.filter(name__contains=searched_event)
        return render(request,
                    'events.html',
                    {
                        'events': events,
                    })
    else:
        return render(request,
                  'home.html',
                  {
                      'data': '',
                      'url_data': '',                    
                  })


def venuesView(request):
    venues = models.Venue.objects.all()

    return render(request,
                  'venues.html',
                  {
                      'venues': venues,
                  })

def venueView(request, venue_id):
    venue = models.Venue.objects.get(pk=venue_id)

    return render(request,
                  'venue.html',
                  {
                      'venue': venue,
                  })

def addVenueView(request):
    submitted = False

    if request.method == 'POST':
        form = forms.VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = forms.VenueForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 
                  'add_venue.html',
                  {
                        'form': form,
                        'submitted': submitted,
                  })

def updateVenueView(request, venue_id):
    venue = models.Venue.objects.get(pk=venue_id)

    if request.method == 'POST':
        form = forms.VenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/venues')
    else:
        form = forms.VenueForm(instance=venue)

    return render(request,
                  'update_venue.html',
                  {
                      'form': form,
                      'venue': venue,
                  })

def deleteVenueView(request, venue_id):
    venue = models.Venue.objects.get(pk=venue_id)
    venue.delete()

    return HttpResponseRedirect('/venues')