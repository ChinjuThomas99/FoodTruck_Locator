import csv
from django.core.management.base import BaseCommand
from trucks.models import FoodTruck

class Command(BaseCommand):
    help = 'Load food trucks from a CSV file'

    def handle(self, *args, **kwargs):
        with open('food-truck-data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                FoodTruck.objects.create(
                    name=row['Applicant'],
                    description=row['FoodItems'],
                    latitude=row['Latitude'],
                    longitude=row['Longitude'],
                    address =row['Address'],
    
                    )
        self.stdout.write(self.style.SUCCESS('Successfully loaded food trucks'))