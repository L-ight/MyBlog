from Classification.models import Classification
from Tag.models import Tag

from django.shortcuts import render_to_response

def home(request):

    classifications = Classification.objects.all()
    classifications_card = list()
    for item in classifications:
        tag = Tag.objects.filter(classification=item)
        classifications_card.append({'Classifications':item,'Tags':tag})
    return render_to_response('index.html', {'Classifications': classifications,'Classifications_Card':classifications_card})
