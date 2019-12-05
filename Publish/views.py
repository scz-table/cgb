from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.http import require_GET,require_http_methods,require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import *
from .models import *
from django.core.paginator import Paginator
from Universalscript.get_paginator import get_pagination_data
import json

def Publish(request):
    pass

@require_GET
def TitleView(request):
    publish_list=PublishArticle.objects.all()
    return render(request, "Publish/list/Title.html", {"publish_list":publish_list})

@require_GET
def ArticleView(request,article_id):
    publish=PublishArticle.objects.get(id=article_id)
    return render(request,"Publish/Article.html",{"publish":publish})

@login_required
@csrf_exempt
def Article_Column(request):
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(author=request.user.extension)
        around_count = 5
        paginator = Paginator(columns, around_count)
        page = request.GET.get('page')
        # column_form = ArticleColumnForm()
        return render(request, "Publish/column/article_column.html", get_pagination_data(page,'columns', paginator, around_count))

    if request.method == "POST":
        column_name = request.POST.get('column')
        notes_name = request.POST.get('notes')
        print(notes_name)
        columns = ArticleColumn.objects.filter(author=request.user.extension, column=column_name)
        try:
            if columns:
                return HttpResponse('2')
            else:
                ArticleColumn.objects.create(author=request.user.extension, column=column_name,notes=notes_name)
                return HttpResponse("1")
        except:
            return HttpResponse("0")


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def rename_article_column(request):
    article_column=ArticleColumnForm(request.POST)
    if article_column.is_valid():
        cd=article_column.cleaned_data
        column_name = cd.get("column")
        notes_name = cd.get("notes")
        column_id = request.POST.get('column_id')
        try:
            columns = ArticleColumn.objects.filter(author=request.user.extension, column=column_name).exclude(pk=column_id)
            if columns:
                return HttpResponse('2') # 重复操作
            else:
                line = ArticleColumn.objects.get(pk=column_id)
                line.column = column_name
                line.notes = notes_name
                line.save()
                return HttpResponse("1") #验证成功
        except:
            return HttpResponse("0")#保存错误
    return HttpResponse("3")#验证错误


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST.get('column_id')
    print(column_id)
    try:
        line = ArticleColumn.objects.get(pk=column_id)
        print(line)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

@login_required()
@csrf_exempt
def article_post(request):
    if request.method=="POST":
        article_post_form = PublishArticleForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user.extension
                new_article.publish_department_position = list(request.user.extension.position.values_list('position',flat=True))
                position_list=request.user.extension.position.all()
                tmp_list_value=set()
                for tmp_list in position_list:
                    if tmp_list:
                        tmp_list_value.add(tmp_list.department.departmentName)
                new_article.publish_department =list(tmp_list_value)
                # new_article.contains_department.clear()
                # new_article.excude_department.clear()
                # new_article.contains_department = Department
                # new_article.excude_department = request.user.extension.excude_department.get(id=request.POST.get('column_id'))
                new_article.column = ArticleColumn.objects.get(pk=request.POST.get('column_id'),author=request.user.extension)
                print(new_article.publish_department_position,new_article.publish_department)
                new_article.save()
            # tags = request.POST['tags']
            # if tags:
            #     for atag in json.loads(tags):
            #         tag = request.user.tag.get(tag=atag)
            #         new_article.article_tag.add(tag)
                return HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")
    else:
        article_post_form = PublishArticleForm()
        article_columns = request.user.extension.article_column.all()
        # article_tags = request.user.tag.all()
        # return render(request, "article/column/article_post.html",{"article_post_form":article_post_form, "article_columns":article_columns, "article_tags":article_tags})
        return render(request, "Publish/column/article_post.html",{"article_post_form":article_post_form, "article_columns":article_columns})

@login_required()
@require_GET
def article_list(request):
    articles_list = PublishArticle.objects.filter(author=request.user.extension)
    around_count = 5
    paginator = Paginator(articles_list, around_count)
    page = request.GET.get('page')
    return render(request, "Publish/column/article_list.html",get_pagination_data(page,'articles', paginator, around_count))


@login_required(login_url='/account/login')
def article_detail(request, id, slug):
    article = get_object_or_404(PublishArticle, id=id, slug=slug)
    return render(request, "Publish/column/article_detail.html", {"article":article})


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article(request):
    article_id = request.POST['article_id']
    try:
        article = PublishArticle.objects.get(id=article_id)
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

@login_required()
@csrf_exempt
def redit_article(request, article_id):
    if request.method == "GET":
        article_columns = request.user.extension.article_column.all()
        article = PublishArticle.objects.get(id=article_id)
        this_article_form = PublishArticleForm(initial={"title":article.title})
        this_article_column = article.column
        print('1')
        return render(request, "Publish/column/redit_article.html", {"article":article, "article_columns":article_columns, "this_article_column":this_article_column, "this_article_form":this_article_form})
    else:
        redit_article = PublishArticle.objects.get(id=article_id)
        try:
            redit_article.column = request.user.extension.article_column.get(id=request.POST['column_id'])
            redit_article.title = request.POST['title']
            redit_article.body = request.POST['body']
            redit_article.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")

