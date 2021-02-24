from django.core.management.base import BaseCommand, CommandError

from apps.main.models import HotelFeature, RoomFeature


class Command(BaseCommand):
    help = 'Creates hotel and room features. args: int of hotel features, int of room features'

    def add_arguments(self, parser):
        parser.add_argument('hotel_feature', nargs='+', type=int)
        parser.add_argument('room_feature', nargs='+', type=int)

    def handle(self, *args, **options):
        for i in range(options['hotel_feature'][0]):
            HotelFeature.objects.create(title='Hotel feature ' + str(i))

        for i in range(options['room_feature'][0]):
            RoomFeature.objects.create(title='Room feature ' + str(i))

        self.stdout.write(
            self.style.SUCCESS(
                f'Created {options["hotel_feature"][0]} hotel features and {options["room_feature"][0]} room feeatures'))
