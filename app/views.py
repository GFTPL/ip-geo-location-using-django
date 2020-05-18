from django.shortcuts import render
import requests

def home(request):
 ip = requests.get('http://httpbin.org/ip')
 ip_ex = ip.json()
 ip_f = ip_ex['origin']
 response=requests.get('https://api.ipfind.com/?ip=%s' % ip_f )
 data=response.json()
 return render(request, 'home.html' ,
 {
  'ip':ip_f,
  'city':data['city'],
  'country': data['country'],
  'latitude': data['latitude'],
  'longitude': data['longitude'],
  'timezone': data['timezone']

 }
 )
