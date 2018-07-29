from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.count() == 0:
            username = 'admin'
            password = os.getenv('DEFAULT_PWD', 'admin')
            email = ''
            print('Creating account for %s' % (username,))
            admin = User.objects.create_superuser(username=username, email=email, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no users exist')