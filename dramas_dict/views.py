import pandas as pd
import os

from django.shortcuts import render
from django.http import HttpResponse

def drama_table(request):
    dramas_csv = pd.read_csv('dramas.csv')
    dramas = [list(dramas_csv.loc[i]) for i in range(len(dramas_csv))]
    # print(dramas)
    return render(request, 'base.html', {'dramas': dramas})
    