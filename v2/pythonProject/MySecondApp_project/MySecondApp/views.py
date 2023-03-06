from django.shortcuts import render
import  string
import json
import  html
from django.shortcuts import render
from MySecondApp.models import CrashMenu
from django.db.models.expressions import RawSQL
## <!-- Шанин Андрей Владимирович  hedgestandart@gmail.com -->

# Create your views here.
title = 'Менюшка'

def default_page(request,item=''):
#    Форма доля тестов
#"""
#    menu=[
#            ['big1','/item1',0,'ul'],
#            ['item2', '/item2',1,'li'],
#            ['item3', '/item3',2, 'li'],
#            ['big 2', '/item1', 0, 'ul'],
#            ['item4', '/item4', 1, 'li'],
#            ['item5', '/item5', 2, 'li']
#          ]
#"""

## Берем данные из таблицы и сортируем их чтобы они попали в свою менюшку
    table = "MySecondApp_crashmenu"
    all_menu_raw = CrashMenu.objects.raw("SELECT distinct a.id, a. name, a.url, a.parent_id , (a.id = a.parent_id) as caret FROM "+table +"  as a , "+table+"  as b order by  b.parent_id asc, a.id asc")

    #в нормальный список
    all_menu=[]
    for p in all_menu_raw:
        print ("DEBUG: ",p.name, ' ',p.url)
        elem='li'
        if p.parent_id == p.id:
            elem="ul"
        all_menu.append( [p.name,p.url,p.parent_id,elem] )

## Берем переделываем в JSON
    data_menu = html.unescape (  json.dumps(  all_menu, ensure_ascii=False, separators=(',', ':'))  ).replace("&quot;",'\"')
    print (data_menu)

## Сдаем  данные мордашке
    data={
        'title' :str(title),
        'item'  :str("/"+item),
        'menu': html.unescape(data_menu),
        'menu_len': len(  all_menu),
    }

    return (render(request,'default.html',data))