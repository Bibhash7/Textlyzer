from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #params = {'name':'Tarbi'}
    return render(request,"index.html")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    #Operations
    removepunc = request.POST.get('removepunc','default')
    fullcaps = request.POST.get('fullcaps','default')
    count = request.POST.get('count','default')
    newlineremover = request.POST.get('newlineremover','default')
    spaceremover = request.POST.get('spaceremover','default')
    #Result text
    analyzed = ""


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed,'input_text': djtext}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = djtext.upper()
        params = {'purpose': 'To Upper Case', 'analyzed_text': analyzed, 'input_text': djtext}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if count == "on":
        cnt = 0
        analyzed = ""
        for x in djtext:
            if(x.isdigit()):
                continue
            analyzed+=x
        params = {'purpose': 'Number Remover', 'analyzed_text': analyzed, 'input_text': djtext}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for x in djtext:
            if x != '\n' and x!='\r':
                analyzed+=x
        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed, 'input_text': djtext}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if spaceremover =="on":
        analyzed =""
        for x in djtext:
            if(x!=' '):
                analyzed+=x
        params = {'purpose': 'Space Remove', 'analyzed_text': analyzed, 'input_text': djtext}
        djtext = analyzed

    if spaceremover !="on" and newlineremover != "on" and count != "on" and fullcaps != "on" and removepunc != "on":
        return HttpResponse("Select any option and try again")
    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

