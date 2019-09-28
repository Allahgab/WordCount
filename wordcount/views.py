from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,'home.html')

def Count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] =1    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':worddictionary.items()})  