#me and myself
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def manipulator(request):
    string = request.POST.get('text', 'default')
    punctuation = request.POST.get('remove punctuation', 'off')
    uppercase = request.POST.get('UPPERCASE', 'off')
    espaces = request.POST.get('remove extra spaces', 'off')
    rlines = request.POST.get('remove lines', 'off')
    ccnt = request.POST.get('character count', 'off')
    mstring = motto = ''
    any = 0
    if punctuation == 'on':
        any = 1
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
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

    if not(any):
        return HttpResponse("<h1> Please select any option to see the magic </h1>")
    para = {'text': string, 'motto': motto}
    return render(request, 'analyzing.html', para)

# def about(request):
#     s = 'How are you?'
#     s = str(s)
#     return HttpResponse("<h1> %s </h1>" % s)
#
# def test(request):
#     f1 = open("first.txt", "r")
#     return HttpResponse("<h1> %s <h1>" % (f1.read()))
#
# def navigator(request):
#     html = '''<a href = "https://www.youtube.com/"> Youtube </a> <br>
#     <a href = "https://www.gaana.com/"> Gaana </a> <br>
#     <a href = "https://www.codeforces.com/"> Codeforces </a> <br>
#     <a href = "https://www.codechef.com/"> Codechef </a> <br>
#     <a href = "https://www.hackerrank.com/"> hackerrank </a>'''
#     return HttpResponse(html)
#
# def capFirst(request):
#     html = '''
#     <h3> capFirst is here </h3>
#     <form>
#     <button type = "submit" value = "back to home" formaction = "http://127.0.0.1:8000/">
#     back to home
#     </button>
#     </form>
#     '''
#     return HttpResponse(html)
#
# def capitalize(request):
#     string = request.GET.get('text')
#     print(string)
#     html = '''
#     <h3> capitalize is here </h3>
#     <form>
#     <button type = "submit" value = "back to home" formaction = "http://127.0.0.1:8000/">
#     back to home
#     </button>
#     </form>
#     '''
#     return HttpResponse(html)
