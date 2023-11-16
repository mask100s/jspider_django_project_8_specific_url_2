from django.shortcuts import render

# Create your views here.
def idli(request):
  data='This data is assumed from database'
  d={'assumption':data}
  return render(request,'idli.html',context=d)