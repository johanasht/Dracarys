import csv
import json
from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Imports data after migrations.'

    def handle(self, *args, **kwargs):
        import_data()
        self.stdout.write(self.style.SUCCESS('Data import completed successfully.'))

def import_data():
    foods = []
    drinks = []
    count  = 0
    drink_values = ['Signature', 'Coffee', 'Non Coffee', 'Minuman']
    with open('reviews/data/gofood_dataset.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if count >= 100:
                break
            if row['display'] in drink_values:
                drinks.append({
                    'model': 'drinks.Drink',
                    'fields': {
                        'product': row['product'],
                        'merchant_area': row['merchant_area'],
                        'merchant_name': row['merchant_name'],
                        'category': row['category'],
                        'description': row['description']
                    }
                })
            else:
                foods.append({
                    'model': 'foods.Food',
                    'fields': {
                        'product': row['product'],
                        'merchant_area': row['merchant_area'],
                        'merchant_name': row['merchant_name'],
                        'category': row['category'],
                        'description': row['description']
                    }
                })
            count+=1

    with open('reviews/fixtures/foods.json', 'w') as foods_file:
        foods_file.write(json.dumps(foods, indent=2))

    with open('reviews/fixtures/drinks.json', 'w') as drinks_file:
        drinks_file.write(json.dumps(drinks, indent=2))

    call_command('loaddata', 'foods.json')
    call_command('loaddata', 'drinks.json')

if __name__ == '__main__':
    import_data()
