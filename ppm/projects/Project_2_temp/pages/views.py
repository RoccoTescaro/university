from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from . import models
from . import forms

def homeView(request):
    return render(request, 'home.html', { })


def eventsView(request):
    events = models.Event.objects.all()

    return render(request, 
                  'events.html',
                  {
                      'events': events,                    
                  })

def managedEventsView(request):
    events = models.Event.objects.filter(manager=request.user)

    return render(request,
                  'events.html',
                  {
                      'events': events,
                  })

def attendedEventsView(request):
    events = models.Event.objects.filter(attendees=request.user)

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
            messages.success(request, 'Event added successfully')
            return HttpResponseRedirect('/events')
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

def joinEventView(request, event_id):
    event = models.Event.objects.get(pk=event_id)

    if not request.user.is_authenticated:
        messages.error(request, 'You need to login to join an event')
        return HttpResponseRedirect('/login')

    if request.user in event.attendees.all():
        messages.error(request, 'You are already attending this event')
        return HttpResponseRedirect('/events')
    
    event.attendees.add(request.user)
    event.save()

    return HttpResponseRedirect('/events')

def leaveEventView(request, event_id):
    event = models.Event.objects.get(pk=event_id)

    if not request.user.is_authenticated:
        messages.error(request, 'You need to login to leave an event')
        return HttpResponseRedirect('/login')


    if request.user not in event.attendees.all():
        messages.error(request, 'You are not attending this event')
        return HttpResponseRedirect('/events')
    
    event.attendees.remove(request.user)
    event.save()

    return HttpResponseRedirect('/events')

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

    if not request.user.is_authenticated:
        messages.error(request, 'You need to login to delete an event')
        return HttpResponseRedirect('/login')

    if request.user == event.manager:
        event.delete()
    else:
        messages.error(request, 'You are not authorized to delete this event')

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
                  'home.html', { })


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
            messages.success(request, 'Venue added successfully')
            return HttpResponseRedirect('/venues')
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

    if not request.user.is_authenticated or not request.user.is_staff:
        messages.error(request, 'You need to login to staff member delete a venue')
        return HttpResponseRedirect('/login')

    venue.delete()

    return HttpResponseRedirect('/venues')

def searchVenueView(request):
    if request.method == 'POST':
        searched_venue = request.POST['searched_venue']
        venues = models.Venue.objects.filter(name__contains=searched_venue)
        return render(request,
                    'venues.html',
                    {
                        'venues': venues,
                    })
    else:
        return render(request, 'home.html', { })