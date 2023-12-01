from django.shortcuts import render
from django.http import HttpResponse





def maqola_royxati(request):
    maqolalar = [
        {'id': 1, 'sarlavha': 'Birinchi maqola', 'muallif': 'Muallif 1'},
        {'id': 2, 'sarlavha': 'Ikkinchi maqola', 'muallif': 'Muallif 2'},
    ]
    context = {'maqolalar': maqolalar}
    return render(request, 'maqola_royxati.html', context)

def maqola_tafsiloti(request, maqola_id):
    maqola = {'id': maqola_id, 'sarlavha': 'Tanlangan maqola', 'muallif': 'Muallif 3', 'tartib': 3, 'matn': 'Bu maqola batafsil matni.'}
    context = {'maqola': maqola}
    return render(request, 'maqola_tafsiloti.html', context)




