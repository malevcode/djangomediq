from django.shortcuts import render
from .models import OpenMicEvent
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

def open_mic_list(request):
    events = OpenMicEvent.objects.all()

    # Get filter/search parameters
    search = request.GET.get('search', '').strip()
    mic_name = request.GET.get('mic_name', '').strip()
    venue_name = request.GET.get('venue_name', '').strip()
    neighborhood = request.GET.get('neighborhood', '').strip()
    weekday = request.GET.get('weekday', '').strip()
    borough = request.GET.get('borough', '').strip()
    cost = request.GET.get('cost', '').strip()
    verification_status = request.GET.get('verification_status', '').strip()

    # General search (matches any relevant field)
    if search:
        events = events.filter(
            Q(name__icontains=search) |
            Q(venue__icontains=search) |
            Q(neighborhood__icontains=search) |
            Q(borough__icontains=search) |
            Q(description__icontains=search) |
            Q(signup_instructions__icontains=search)
        )
    if mic_name:
        events = events.filter(name__icontains=mic_name)
    if venue_name:
        events = events.filter(venue__icontains=venue_name)
    if neighborhood:
        events = events.filter(neighborhood__icontains=neighborhood)
    if weekday:
        events = events.filter(day__iexact=weekday)
    if borough:
        events = events.filter(borough__iexact=borough)
    if cost:
        if cost == 'free':
            events = events.filter(cost__icontains='free')
        elif cost == 'paid':
            events = events.exclude(cost__icontains='free')
    if verification_status:
        events = events.filter(verification_status=verification_status)

    events = events.order_by('date', 'time')

    WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    BOROUGHS = ["Manhattan", "Brooklyn", "Queens", "The Bronx", "Staten Island"]

    context = {
        'events': events,
        'search': search,
        'mic_name': mic_name,
        'venue_name': venue_name,
        'neighborhood': neighborhood,
        'weekday': weekday,
        'borough': borough,
        'cost': cost,
        'verification_status': verification_status,
        'weekdays': WEEKDAYS,
        'boroughs': BOROUGHS,
    }
    return render(request, 'mics/open_mic_list.html', context)

@csrf_exempt
def add_mic(request):
    if request.method == 'POST':
        try:
            data = request.POST
            event = OpenMicEvent.objects.create(
                name=data.get('name'),
                venue=data.get('venue'),
                address=data.get('address'),
                date=data.get('date') or None,
                time=data.get('time') or None,
                description=data.get('description'),
                day=data.get('day'),
                start_time=data.get('start_time'),
                latest_end_time=data.get('latest_end_time'),
                borough=data.get('borough'),
                neighborhood=data.get('neighborhood'),
                venue_type=data.get('venue_type'),
                cost=data.get('cost'),
                stage_time=data.get('stage_time'),
                signup_instructions=data.get('signup_instructions'),
                hosts=data.get('hosts'),
                changes_updates=data.get('changes_updates'),
                last_verified=data.get('last_verified'),
                other_rules=data.get('other_rules'),
                reviews=data.get('reviews'),
                unique_identifier=data.get('unique_identifier'),
                verification_status=data.get('verification_status', 'unverified'),
                # sms is not a model field anymore, but you can handle it here if you add it back
            )
            # TODO: Send to Google Sheets here using gspread or Google Sheets API
            # (Placeholder for now)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})
