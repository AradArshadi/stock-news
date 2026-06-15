from django.shortcuts import render


def alert_list(request):
    return render(request, 'alerts/list.html')
