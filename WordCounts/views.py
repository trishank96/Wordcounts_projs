from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):
    text_entered = request.GET['fulltext']
    words_list = text_entered.split()
    words_list_imp = []
    num_list = []
    for words in words_list:
        if words.isdigit():
            num_list.append(words.strip('.,'))
        words_list_imp.append(words.strip("',.:"))
        
    counts_words = {}
    for words in words_list_imp:
        if words in counts_words:
            counts_words[words]+=1
        else:
            counts_words[words]=1
        
    sorted_words = sorted(counts_words.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'text': text_entered, 'counts': len(words_list), 'each_counts':sorted_words})


def about(request):
    return render(request, 'about.html')

