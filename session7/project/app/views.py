from django.shortcuts import render

# Create your views here.

def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text'] #html 태그랑 똑같이!
    total_len = len(text)
    print('1', text)
    stripped_text = text.replace(" ", "")
    print('2', text)
    stripped_len = len(stripped_text)
    count_word = len(text.split())
    return render(request, 'result.html', {
        'total_len' : total_len,
        'text' : text,
        'stripped_len' : stripped_len,
        'count_word' : count_word,
    })

