import csv
from django.core.management.base import BaseCommand
from mics.models import OpenMicEvent
from datetime import datetime

FIELD_MAP = {
    'Open Mic': 'name',
    'Day': 'day',
    'Start Time': 'start_time',
    'Latest End Time': 'latest_end_time',
    'Venue Name': 'venue',
    'Borough': 'borough',
    'Neighborhood': 'neighborhood',
    'Location': 'address',
    'Venue type': 'venue_type',
    'Cost': 'cost',
    'Stage time': 'stage_time',
    'Sign-Up Instructions': 'signup_instructions',
    'Host(s) / Organizer': 'hosts',
    'Changes/updates': 'changes_updates',
    'Last verified': 'last_verified',
    'Other Rules': 'other_rules',
    'Help other comics! Leave reviews': 'reviews',
    'unique identifier': 'unique_identifier',
    # description, date, and time will be handled below
}

class Command(BaseCommand):
    help = 'Import open mic events from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Path to the CSV file to import.')

    def handle(self, *args, **options):
        csv_path = options['csv_path']
        created = 0
        updated = 0
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = {}
                for csv_col, model_field in FIELD_MAP.items():
                    data[model_field] = row.get(csv_col, '').strip() or None

                # Skip rows with no mic name
                if not data.get('name'):
                    continue

                # Try to parse date and time from Start Time and Day
                data['date'] = None
                data['time'] = None

                # Description: combine changes/updates, other rules, and reviews for now
                desc_parts = []
                for key in ['changes_updates', 'other_rules', 'reviews']:
                    if data.get(key):
                        desc_parts.append(f"{key.replace('_',' ').capitalize()}: {data[key]}")
                data['description'] = '\n'.join(desc_parts) if desc_parts else None

                # Set verification_status based on last_verified
                lv = (data.get('last_verified') or '').lower()
                if 'verified tediously' in lv:
                    data['verification_status'] = 'verified tediously'
                elif 'verified' in lv:
                    data['verification_status'] = 'verified'
                else:
                    data['verification_status'] = 'unverified'

                # Update if unique_identifier exists, else create
                unique_id = data.get('unique_identifier')
                if unique_id:
                    # Handle duplicates: update the first, delete extras
                    matches = list(OpenMicEvent.objects.filter(unique_identifier=unique_id))
                    if matches:
                        event = matches[0]
                        for key, value in data.items():
                            setattr(event, key, value)
                        event.save()
                        # Delete any extras
                        for extra in matches[1:]:
                            extra.delete()
                        updated += 1
                    else:
                        OpenMicEvent.objects.create(**data)
                        created += 1
                else:
                    # If no unique_identifier, create new
                    OpenMicEvent.objects.create(**data)
                    created += 1
        self.stdout.write(self.style.SUCCESS(f'Imported {created} new and updated {updated} open mic events.')) 