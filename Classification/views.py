from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

from Article.models import Article
from Classification.models import Classification
from models import Classification

def getArticleListByClassification(request,name):
    classifications = Classification.objects.all()
    articleList = Article.objects.filter(classification__name=name)
    item = Classification.objects.get(name=name)
    return render_to_response('articleList.html',{'Classifications': classifications,"ArticleList":articleList,'Item':item})
