from django.shortcuts import render


def rules_list(request):
    return render(request, 'rules/rules_list.html')
