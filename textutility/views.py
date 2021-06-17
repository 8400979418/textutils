# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    upperchar=request.GET.get('upperchar','off')
    spaceremover=request.GET.get('spaceremover','off')
    newlineremover=request.GET.get('newlineremover','off')
    charcounter=request.GET.get('charcounter','off')
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    elif newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif upperchar=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif spaceremover=="on":
        analyzed =""
        for index,char in  enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]=="":
                pass
            else:
                analyzed=analyzed+char
        params = {'purpose': 'Remove Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif  charcounter== "on":
        analyzed = len(djtext)
        params = {'purpose': 'Charecter count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

