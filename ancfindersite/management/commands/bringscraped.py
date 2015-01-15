import json
from django.core.management.base import BaseCommand#, CommandError
from ancfindersite.models import CommissionerInfo
# from polls.models import Poll

class Command(BaseCommand):
    # args = '<poll_id poll_id ...>'
    # help = 'Closes the specified poll for voting'

    def handle(self, path_to_json, *args, **options):
        with open(path_to_json) as source_file:
            scraped_data = json.load(source_file)

        for ID, fields in scraped_data.items():
            anc, smd = ID[:2], ID[2:]

            for field_name, field_value in fields.items():
                ci = CommissionerInfo()
                ci.anc, ci.smd = anc, smd
                ci.field_name = field_name
                ci.field_value = field_value
                ci.save()

        for c in CommisssionerInfo.objects.all():
            print c.superceded_by