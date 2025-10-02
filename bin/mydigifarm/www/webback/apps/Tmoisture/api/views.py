# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250929
# VERSION: 1.0
# FILE: mydigifarm,1.0,views.py
# DESCRIPTION: Sets up view for moisture.
# LASTMODIFIED: 20250929

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## *|*|*|*|* Section 1 *|*|*|*|*

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from apps.Tmoisture.api.serializers import TmoistureSerializer
from apps.Tmoisture.models import Tmoisture

from django.http import JsonResponse

from datetime import date
from datetime import datetime

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions. 
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*

@api_view(['GET', ])
def moisture_cluster_all(request, cluster_no):
    if request.method == 'GET':
        all_cluster_no = cluster_no.split(",")

        try:
            collection = []
            for cluster in all_cluster_no:
                query_results = Tmoisture.objects.filter(
                        tmoisture_cluster_no=cluster).order_by('-tmoisture_ts')
                if query_results:
                    collection.append([cluster, query_results])
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        dataResponse = []
        for item in collection:
            data = {}
            serializer = TmoistureSerializer(
                item[1], many=True)

            data['data'] = serializer.data
            data['cluster_no'] = item[0]
            dataResponse.append(data)

        return JsonResponse(dataResponse, safe=False)

@api_view(['GET', ])
def moisture_cluster_latest(request, cluster_no):
    if request.method == 'GET':
        all_cluster_no = cluster_no.split(",")
        try:
            collection = []
            for cluster in all_cluster_no:
                query_results = Tmoisture.objects.filter(
                    tmoisture_cluster_no=cluster).latest('tmoisture_ts')
                if query_results:
                    collection.append(query_results)
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TmoistureSerializer(
            collection, many=True)
        return Response(serializer.data)
        
@api_view(['GET', ])
def moisture_cluster_latest_count(request, cluster_no, count):
    if request.method == 'GET':
        all_cluster_no = cluster_no.split(",")
        int_count=int(count)
        try:
            collection = []
            for cluster in all_cluster_no:
                query_results = Tmoisture.objects.filter(
                    tmoisture_cluster_no=cluster).order_by('-tmoisture_ts')[:int_count:-1]
                if query_results:
                    collection.append([cluster, query_results])
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        dataResponse = []
        for item in collection:
            data = {}
            serializer = TmoistureSerializer(
               item[1], many=True)

            data['data'] = serializer.data
            data['cluster_no'] =item[0]
            dataResponse.append(data)

        return JsonResponse(dataResponse, safe=False)

@api_view(['GET', ])
def moisture_cluster_date_range(request, cluster_no):
    if request.method == 'GET':
        all_cluster_no = cluster_no.split(",")

        query_start_date=request.query_params.get('start_date').split('-')
        query_end_date=request.query_params.get('end_date').split('-')
        start_date_obj=date(int(query_start_date[0]), int(query_start_date[1]), int(query_start_date[2]))
        end_date_obj=date(int(query_end_date[0]), int(query_end_date[1]), int(query_end_date[2]))

        try:
            collection = []
            for cluster in all_cluster_no:
                query_results = Tmoisture.objects.filter(tmoisture_cluster_no=cluster, tmoisture_ts__range=(start_date_obj, end_date_obj)).order_by('tmoisture_ts')
                if query_results:
                    collection.append([cluster, query_results])
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        dataResponse = []
        for item in collection:
            data = {}
            serializer = TmoistureSerializer(
                item[1], many=True)
            data['data'] = serializer.data
            data['cluster_no'] = item[0]
            dataResponse.append(data)
        return JsonResponse(dataResponse, safe=False)

@api_view(['GET', ])
def moisture_cluster_date_specific(request, cluster_no):
    if request.method == 'GET':
        all_cluster_no = cluster_no.split(",")
        
        query_date=request.query_params.get('date').split('-')

        year=query_date[0]
        month=query_date[1]  
        day=query_date[2]

        query_string = f"{year}.{month}.{day}"

        try:
            collection = []
            for cluster in all_cluster_no:
                query_results = Tmoisture.objects.filter(tmoisture_cluster_no=cluster, tmoisture_ts__startswith=query_string).order_by('tmoisture_ts')
                if query_results:
                    collection.append([cluster, query_results])
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        dataResponse = []
        for item in collection:
            data = {}
            serializer = TmoistureSerializer(
                item[1], many=True)

            data['data'] = serializer.data
            data['cluster_no'] = item[0]
            dataResponse.append(data)
        return JsonResponse(dataResponse, safe=False)

@api_view(['GET', ])
def moisture_cluster_datetime_range(request, cluster_no):
    if request.method == 'GET':
        all_cluster_no = cluster_no.split(",")

        query_start_date=request.query_params.get('start_date').split(' ')[0]
        query_start_time=request.query_params.get('start_date').split(' ')[1]
        query_end_date=request.query_params.get('end_date').split(' ')[0]
        query_end_time=request.query_params.get('end_date').split(' ')[1]

        start_date=query_start_date.split('-')
        start_time=query_start_time.split(":")
        end_date=query_end_date.split('-')
        end_time=query_end_time.split(":")

        start_date_obj=datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]), int(start_time[0]), int(start_time[1]), int(start_time[2]))
        end_date_obj=datetime(int(end_date[0]), int(end_date[1]), int(end_date[2]), int(end_time[0]), int(end_time[1]), int(end_time[2]))

        try:
            collection = []
            for cluster in all_cluster_no:
                query_results = Tmoisture.objects.filter(tmoisture_cluster_no=cluster, tmoisture_ts__range=(start_date_obj, end_date_obj)).order_by('tmoisture_ts')
                if query_results:
                    collection.append([cluster, query_results])
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        dataResponse = []
        for item in collection:
            data = {}
            serializer = TmoistureSerializer(
                item[1], many=True)
            data['data'] = serializer.data
            data['cluster_no'] = item[0]
            dataResponse.append(data)
        return JsonResponse(dataResponse, safe=False)

@api_view(['GET', ])
def moisture_clusters_all(request):
    if request.method == 'GET':
        try:
            query_results = Tmoisture.objects.all()
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = TmoistureSerializer(query_results, many=True)
            return Response(serializer.data)

@api_view(['GET', ])
def moisture_clusters_all_latest(request):
    if request.method == 'GET':
        all_cluster_no = Tmoisture.objects.values("tmoisture_cluster_no").distinct()
        try:
            collection = []
            for cluster in all_cluster_no:
                query_results = Tmoisture.objects.filter(
                    tmoisture_cluster_no=cluster['tmoisture_cluster_no']).latest('tmoisture_ts')
                if query_results:
                    collection.append(query_results)
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TmoistureSerializer(
            collection, many=True)
        return Response(serializer.data)

@api_view(['GET', ])
def moisture_clusters_all_latest_count(request, count):
    if request.method == 'GET':
        all_cluster_no = Tmoisture.objects.values("tmoisture_cluster_no").distinct()
        int_count=int(count)
        try:
            collection = []
            for cluster in all_cluster_no:
                query_results = Tmoisture.objects.filter(
                tmoisture_cluster_no=cluster['tmoisture_cluster_no']).order_by('-tmoisture_ts')[:int_count:-1]
                if query_results:
                    collection.append([cluster, query_results])
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        dataResponse = []
        for item in collection:
            data = {}
            serializer = TmoistureSerializer(
                item[1], many=True)

            data['data'] = serializer.data
            data['cluster_no'] = item[0]['tmoisture_cluster_no']
            dataResponse.append(data)

        return JsonResponse(dataResponse, safe=False)
        
@api_view(['GET', ])
def moisture_clusters_all_date_range(request):
    if request.method == 'GET':
        all_cluster_no = Tmoisture.objects.values("tmoisture_cluster_no").distinct()

        query_start_date=request.query_params.get('start_date').split('-')
        query_end_date=request.query_params.get('end_date').split('-')
        start_date_obj=date(int(query_start_date[0]), int(query_start_date[1]), int(query_start_date[2]))
        end_date_obj=date(int(query_end_date[0]), int(query_end_date[1]), int(query_end_date[2]))

        try:
            collection = []
            for cluster in all_cluster_no:
                query_results = Tmoisture.objects.filter(tmoisture_cluster_no=cluster['tmoisture_cluster_no'], tmoisture_ts__range=(start_date_obj, end_date_obj)).order_by('tmoisture_ts')
                if query_results:
                    collection.append([cluster, query_results])
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        dataResponse = []
        for item in collection:
            data = {}
            serializer = TmoistureSerializer(
                item[1], many=True)
            data['data'] = serializer.data
            data['cluster_no'] = item[0]['tmoisture_cluster_no']
            dataResponse.append(data)
        return JsonResponse(dataResponse, safe=False)

@api_view(['GET', ])
def moisture_clusters_all_date_specific(request):
    if request.method == 'GET':
        query_date=request.query_params.get('date').split('-')

        year=query_date[0]
        month=query_date[1]  
        day=query_date[2]

        query_string = f"{year}.{month}.{day}"

        try:
            query_results = Tmoisture.objects.filter(tmoisture_ts__startswith=query_string).order_by('tmoisture_ts')
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TmoistureSerializer(query_results, many=True)
        return Response(serializer.data)

@api_view(['GET', ])
def moisture_clusters_all_datetime_range(request):
    if request.method == 'GET':
        all_cluster_no = Tmoisture.objects.values("tmoisture_cluster_no").distinct()

        query_start_date=request.query_params.get('start_date').split(' ')[0]
        query_start_time=request.query_params.get('start_date').split(' ')[1]
        query_end_date=request.query_params.get('end_date').split(' ')[0]
        query_end_time=request.query_params.get('end_date').split(' ')[1]

        start_date=query_start_date.split('-')
        start_time=query_start_time.split(":")
        end_date=query_end_date.split('-')
        end_time=query_end_time.split(":")

        start_date_obj=datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]), int(start_time[0]), int(start_time[1]), int(start_time[2]))
        end_date_obj=datetime(int(end_date[0]), int(end_date[1]), int(end_date[2]), int(end_time[0]), int(end_time[1]), int(end_time[2]))

        try:
            collection = []
            for cluster in all_cluster_no:
                query_results = Tmoisture.objects.filter(tmoisture_cluster_no=cluster['tmoisture_cluster_no'], tmoisture_ts__range=(start_date_obj, end_date_obj)).order_by('tmoisture_ts')
                if query_results:
                    collection.append([cluster, query_results])
        except Tmoisture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        dataResponse = []
        for item in collection:
            data = {}
            serializer = TmoistureSerializer(
                item[1], many=True)
            data['data'] = serializer.data
            data['cluster_no'] = item[0]['tmoisture_cluster_no']
            dataResponse.append(data)
        return JsonResponse(dataResponse, safe=False)

## *|*|*|*|* End Section 2 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
