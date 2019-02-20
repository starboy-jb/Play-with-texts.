from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def manipulator(request):
    string = request.POST.get('text', 'default')
    string = string.strip()
    punctuation = request.POST.get('remove punctuation', 'off')
    uppercase = request.POST.get('UPPERCASE', 'off')
    espaces = request.POST.get('remove extra spaces', 'off')
    rlines = request.POST.get('remove lines', 'off')
    ccnt = request.POST.get('character count', 'off')
    mstring = motto = ''
    any = 0
    if punctuation == 'on':
        any = 1
        punctuations = '''\\!()-[]{};:'",<>./?@#$%^&*_~'''
        for c in string:
            if c not in punctuations:
                mstring += c
        motto = 'remove punctuation'
        string = mstring
    if uppercase == 'on':
        any = 1
        mstring = string
        mstring = mstring.upper()
        motto = 'UPPERCASE'
        string = mstring
    if espaces == 'on':
        any = 1
        mstring = ''
        for ind in range(len(string)):
            if not(string[ind] == ' ' and string[ind + 1] == ' '):
                mstring += string[ind]
        motto = 'remove extra spaces'
        string = mstring
    if rlines == 'on':
        mstring = ''
        any = 1
        mstring = string
        mstring = mstring.replace('\n', '')
        mstring = mstring.replace('\r', '')
        motto = 'remove lines'
        string = mstring
    if ccnt == 'on':
        any = 1
        ans = 0
        mstring = ''
        for char in string:
            if char.isalpha():
                ans += 1
        mstring = str(ans)
        motto = 'character count'
        string = mstring
    string = string.split("\n")
    
    if not(any):
        return HttpResponse("<h1> Please select any option to see the magic </h1>")
    para = {'text': string, 'motto': motto}
    return render(request, 'analyzing.html', para)
