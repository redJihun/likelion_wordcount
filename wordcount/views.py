from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']
    letter_count = 0
    for letter in full_text:
        if((letter!='\n')&&(letter!='\t')&&(letter!=' ')):
            letter_count += 1

    word_list = full_text.split()
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})
