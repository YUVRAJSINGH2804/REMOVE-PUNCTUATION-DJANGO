from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request,'index.html')
    # return HttpResponse('HOme')

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc= request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    # analyzed= djtext
    punctuations='''
    !()-[];:'"\,<>.?/@#$%^&*_~
    '''
    analyzed=""

    for char in djtext:
        if char not in punctuations:
            analyzed= analyzed+char

    params={'purpose':'remove punctuations','analyzed_text':analyzed}
   

    return render(request,'analyze.html',params)

# def capfirst(request):
#     return HttpResponse("capatilize first")

# def  newlineremove(request):
#     return HttpResponse("newline remove")

# def  spaceremove(request):
#     return HttpResponse("space remover")

# def  charcount(request):
#     return HttpResponse("char count")