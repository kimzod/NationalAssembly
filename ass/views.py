# coding=utf-8
from pprint import pprint
import json
from django.shortcuts import render, redirect
from urllib.request import urlopen
import urllib.request
import urllib


def index(request):
    if request.method == 'GET':
        hgnm = request.GET.get('hgnm')
        hgnm = urllib.parse.quote("{}".format(hgnm))
        print(hgnm)
        ServiceKey = "iBrqaeMXulVrNt5AYYwEbvMdm244rh7S2P5d13RqayCQCvD%2Fcqeh1IEb%2BS%2B%2FWTWz%2FQTYJMG5SxUdPMBadROD3w%3D%3D"

        url = "http://apis.data.go.kr/9710000/NationalAssemblyInfoService/getMemberNameInfoList?serviceKey=" + ServiceKey +"&hgnm="+hgnm+"&_type=json"

        data = urllib.request.urlopen(url).read().decode('utf-8')

        data_json = json.loads(data)
        ass_data = data_json['response']['body']['items']['item']

        context = {'ass_data': ass_data}
        return render(request, 'ass/index.html', context)

