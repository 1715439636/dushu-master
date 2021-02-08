from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world ! ")

# def runoob(request):
#     context          = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'runoob.html', context)



def runoob(request):
    views_list = ["菜鸟教程","菜鸟教程1","菜鸟教程2","菜鸟教程3",]
    return render(request, "runoob.html", {"views_list": views_list})


    # views_unm = 1999
    # return render(request,"runoob.html",{"num":views_unm})
    # # views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    # #
    # return  render(request,"runoob.html", {"views_list":views_list})