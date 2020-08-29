from django.core.management.base import BaseCommand
from authapp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser('admin@admin.com', 'Admin', 'admin')
        print('Done')
