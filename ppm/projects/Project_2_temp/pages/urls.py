from django.urls import path
from . import views

urlpatterns = [
    #int
    #str
    #path 
    #slug (only letters, numbers, underscores, hyphens)
    #uuid (universally unique identifier)

    # Note: is better to add a slash at the end of the url

    # default page
    path('', views.homeView, name='home'),
    # page with custom data on url
    path('<slug:url_data>/', views.homeView, name='home'),
    # events page
    path('events', views.eventsView, name='events'),
    # event detail page
    path('event/<int:event_id>', views.eventView, name='event'),
    # add event page
    path('add_event', views.addEventView, name='add_event'),
    # update event page
    path('update_event/<int:event_id>', views.updateEventView, name='update_event'),
    # delete event
    path('delete_event/<int:event_id>', views.deleteEventView, name='delete_event'),
    # search event page
    path('search_event', views.searchEventView, name='search_event'),
    # venues page
    path('venues', views.venuesView, name='venues'),
    # add venue page
    path('add_venue', views.addVenueView, name='add_venue'),
    # venue detail page
    path('venue/<int:venue_id>', views.venueView, name='venue'),
    # update venue page
    path('update_venue/<int:venue_id>', views.updateVenueView, name='update_venue'),
    # delete venue
    path('delete_venue/<int:venue_id>', views.deleteVenueView, name='delete_venue'),
]