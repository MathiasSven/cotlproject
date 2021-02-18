import sys

from django.apps import AppConfig


class PnwdataConfig(AppConfig):
    name = 'pnwdata'

    def ready(self):
        super(PnwdataConfig, self).ready()

        if not ('migrate' in sys.argv):
            from .models import Market
            for resource in Market.RESOURCE_TYPE:
                if not Market.objects.filter(pk=resource[0]).exists():
                    Market.objects.create(pk=resource[0])
