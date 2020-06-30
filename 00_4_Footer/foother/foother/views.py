from django.shortcuts import render

def foother_index(reqeust):
    return render(reqeust, '_see_all.html')