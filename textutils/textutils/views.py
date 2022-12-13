#I have created this file
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("hello")
def index(request):
    params = {'name':'kundan','place':'Mars'}
    return render(request, 'index.html',params)
# def about(request):
#     return HttpResponse("about me")
# def removepunc(request):
#     #get the text
#     djtext= print(request.GET.get('text', 'default'))
#     print(djtext)
#     #analyse the text
#     return HttpResponse("remove punc")
def analyze(request):
    #get the text
    djtext= request.POST.get('text', 'default')

    #Check checkbox value
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('uppercase','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    #check which checkbox is on
    if removepunc =="on":
        punctutations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed =''
        for char in djtext:
            if char not in punctutations:
                analyzed += char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed =''
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose':'Changed to uppercase', 'analyzed_text':analyzed}
        #analyse the text
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed =''
        for char in djtext:
            if char !="\n":
                analyzed += char
        params = {'purpose':'Removed ne lines', 'analyzed_text':analyzed}
        #analyse the text
        return render(request, 'analyze.html', params)


    # elif(extraspaceremover=="on"):
    #     analyzed =''
    #     for char in djtext:
    #         if char !="  ":
    #             analyzed += char
    #     params = {'purpose':'Removed ne lines', 'analyzed_text':analyzed}
    #     #analyse the text
    #     return render(request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("error")
# def nav(request):
#     return HttpResponse("<a href='https://www.google.co.in/'>Go to Google</a>")