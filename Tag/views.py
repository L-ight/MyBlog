from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from Article.models import Article
from Classification.models import Classification
from models import Tag
# from models import Classification

import MySQLdb

def getArticleListByTag(request,name):
    classifications = Classification.objects.all()
    articleList = Article.objects.filter(tag__name=name)
    item = Tag.objects.get(name=name)
    return render_to_response('articleList.html',{'Classifications': classifications,"ArticleList":articleList,'Item':item})
