from django.core.management.base import BaseCommand, CommandError
from core.models import CustomUser


class Command(BaseCommand):
    help = "Get user token by given id"

    def add_arguments(self, parser):
        parser.add_argument("user_id", type=int)

    def handle(self, *args, **options):
        pass
        # user_id = options["user_id"]

        # try:
        #     user = CustomUser.objects.get(id=user_id)
        # except CustomUser.DoesNotExist:
        #     raise CommandError('User "%s" does not exist' % user_id)

        # # (token, _) = Token.objects.get_or_create(user=user)

        # self.stdout.write(
        #     self.style.SUCCESS(f'User "{user_id}" token: "{token.key}"')
        # )