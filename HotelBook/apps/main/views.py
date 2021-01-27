from django.shortcuts import render


def index(request):
    user = request.user
    if user.status == 'O':
        is_owner = True
    else:
        is_owner = False

    context = {
        'user': user,
        'is_owner': is_owner,
    }
    return render(request, 'main/index.html', context)
