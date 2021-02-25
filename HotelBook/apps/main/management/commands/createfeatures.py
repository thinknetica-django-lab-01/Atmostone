from django.core.management.base import BaseCommand, CommandError

from apps.main.models import HotelFeature, RoomFeature


class Command(BaseCommand):
    help = 'Creates hotel and room features. args: amount of hotel features[int], amount of room features[int]'

    def add_arguments(self, parser):
        parser.add_argument('hotel_feature', nargs='+', type=int)
        parser.add_argument('room_feature', nargs='+', type=int)

    def handle(self, *args, **options):
        """
        Method for creating hotel and room features like: Feature1, Feature2...
        :param args:
        :param options:
        :return:
        """
        for counter in range(1, options['hotel_feature'][0] + 1):
            HotelFeature.objects.create(title='Hotel feature ' + str(counter))

        for counter in range(1, options['room_feature'][0] + 1):
            RoomFeature.objects.create(title='Room feature ' + str(counter))

        self.stdout.write(
            self.style.SUCCESS(
                f'Created {options["hotel_feature"][0]} hotel features and {options["room_feature"][0]} room feeatures'))
