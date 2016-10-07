from django.shortcuts import render
from django.shortcuts import render_to_response

from models import Article
from Tag.models import Tag
from Classification.models import Classification
# Create your views here.

def getArticle(request,articleID):
    classifications = Classification.objects.all()
    article = Article.objects.get(id=articleID)
    tags = article.tag.all()
    return render_to_response('article.html',{'Classifications': classifications,"article":article,'tags':tags})
