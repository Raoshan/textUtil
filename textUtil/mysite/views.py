#I have created File:-Raoshanks
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def ex1(request):
    s=  '''<h2>NavigationBar<br></h2>
    <a href=https://www.youtube.com>youtube</a><br>
    <a href='https://www.facebook.com'>facebokk</a><br>
    <a href="https://www.flipkart.com">flipkart</a><br>    
    '''
    return HttpResponse(s)

    
def analyze(request):
    dtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == 'on':
        analyzed = ""
        puncations = '''![]()-{};:'"\,<>'''
        for char in dtext:
            if char not in puncations:
                analyzed = analyzed+char
              
        param ={'purpose':"remove punc", 'analyzed_text':analyzed}
        dtext = analyzed
        # return render(request, 'analyze.html', param)
    # elif (fullcaps == "on"):
    if (fullcaps == "on"):    
        analyzed= ""
        for char in dtext:
            analyzed= analyzed + char.upper()
        param ={'purpose':'fullcapsform', 'analyzed_text':analyzed}  
        dtext = analyzed
        # return render(request, 'analyze.html', param)  

    # elif (newlineremover == "on"):
    if (newlineremover == "on"):      

        analyzed= ""
        for char in dtext:
            if char !="\n" and char !="\r":
                analyzed= analyzed + char
        param ={'purpose':'reomve new line', 'analyzed_text':analyzed}  
        dtext = analyzed
        # return render(request, 'analyze.html', param)    
    # elif (extraspaceremover == "on"):
    if (extraspaceremover == "on"):      
        analyzed= ""
        for index, char in enumerate(dtext):
            if not(dtext[index]==" " and dtext[index+1] == " "):
                analyzed= analyzed + char
        param ={'purpose':'extraspaceromover', 'analyzed_text':analyzed}  
    if (fullcaps !="on" and fullcaps !='on' and newlineremover !='on' and extraspaceremover !='on'):    
        return HttpResponse("<h1>Please select operation and try again</h1>")
   
    return render(request, 'analyze.html', param)
     