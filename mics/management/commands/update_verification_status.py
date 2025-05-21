from django.core.management.base import BaseCommand
from mics.models import OpenMicEvent

class Command(BaseCommand):
    help = 'Update verification_status for OpenMicEvent based on last_verified field.'

    def handle(self, *args, **options):
        updated = 0
        for event in OpenMicEvent.objects.all():
            lv = (event.last_verified or '').lower()
            if 'verified tediously' in lv:
                event.verification_status = 'verified tediously'
            elif 'verified' in lv:
                event.verification_status = 'verified'
            else:
                event.verification_status = 'unverified'
            event.save()
            updated += 1
        self.stdout.write(self.style.SUCCESS(f'Updated verification_status for {updated} events.')) 