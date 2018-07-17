from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import block
#from .serializers import blockSerializer
from tablib import Dataset
import pandas as pd
import json


def completion(block):
    filename = "C:/Users/hp/Desktop/json.txt"
    json_data = open(filename, encoding='utf-8').read()
    block = json.loads(json_data)
    ################

    l=[]
    for key in block['blocks']:
        #print(key)
        a=[]
        
        a.append(block['blocks'][key]['block_id']) 
        a.append(block['blocks'][key]['type']) 
        a.append(block['blocks'][key]['id'])
        a.append(block['blocks'][key]['display_name'])
        try:
            a.append(block['blocks'][key]['descendants'])
        except:
            a.append([])
        l.append(a)


    block =pd.DataFrame(l )

    block = pd.DataFrame(l,columns=['|__block_id','|__type','|__id','|__display_name', 'descendants'])


    l=[]
    chp=[]
    seq=[]
    ver=[]
    prob=[]                             
    rank1=0
    rank2=0
    rank3=0
    rank4=0
    rank5=0
    block1 = block[block["|__type"]=="course"]
    for item in range(len(block1)):
        #print(block1.iloc[item])
        rank1 += 1
        temp=[ block1['|__block_id'].iloc[item], block1['|__type'].iloc[item], block1['descendants'].iloc[item], block1['|__id'].iloc[item], block1['|__display_name'].iloc[item] ,rank1]
        #print(temp)
        l.append(temp)
        if block1['|__id'].iloc[item] not in chp:
            chp.append(block1['|__id'].iloc[item])
 

    for item2 in chp:
        #print(item2)
        block9 = block[block["|__id"]==item2]
        for item in range(len(block9)):
            #print(block1.iloc[item]['descendants'])

            for  des in block9.iloc[item]['descendants']:
                block8 = block[block["|__id"]==des]

                for j in range(len(block8)):
                    rank2 += 1
                    temp=[ block8['|__block_id'].iloc[j], block8['|__type'].iloc[j], block8['descendants'].iloc[j], block8['|__id'].iloc[j],block8['|__display_name'].iloc[j], rank2]
                    l.append(temp)
                #print(block['ID'])
                    if block8['|__id'].iloc[j] not in seq:
                        seq.append(block8['|__id'].iloc[j]) 


    for item3 in seq:
        #print(item3)
        block7 = block[block["|__id"]==item3]
        print(item)
        for item in range(len(block7)):
            #print(block1.iloc[item]['descendants'])
            #print(item)
            for  des in block7.iloc[item]['descendants']:
                block6 = block[block["|__id"]==des]
                #print(des)
                for j in range(len(block6)):
                    rank3 += 1
                    temp=[ block6['|__block_id'].iloc[j], block6['|__type'].iloc[j], block6['descendants'].iloc[j], block6['|__id'].iloc[j], block6['|__display_name'].iloc[j], rank3]
                    l.append(temp)
                    #print(temp)
                    #print(block['ID'])
                    if block6['|__id'].iloc[j] not in seq:
                        ver.append(block6['|__id'].iloc[j])

                        
                        
    for item1 in ver:
        #print(item2)
        block5 = block[block["|__id"]==item1]
        for item in range(len(block5)):
            #print(block1.iloc[item]['descendants'])

            for  des in block5.iloc[item]['descendants']:
                block4 = block[block["|__id"]==des]

                for j in range(len(block4)):
                    rank4 += 1
                    temp=[ block4['|__block_id'].iloc[j], block4['|__type'].iloc[j], block4['descendants'].iloc[j], block4['|__id'].iloc[j], block4['|__display_name'].iloc[j], rank4]
                    l.append(temp)
                #print(block['ID'])
                    if block4['|__id'].iloc[j] not in seq:
                        prob.append(block4['|__id'].iloc[j])
                        
                        
                        
    for item1 in prob:
        #print(item2)
        block3 = block[block["|__id"]==item1]
        for item in range(len(block3)):
            #print(block1.iloc[item]['descendants'])

            for  des in block3.iloc[item]['descendants']:
                block2 = block[block["|__id"]==des]

                for j in range(len(block2)):
                    rank5 += 1
                    temp=[ block2['|__block_id'].iloc[j], block2['|__type'].iloc[j], block2['descendants'].iloc[j], block2['|__id'].iloc[j], block2['|__display_name'].iloc[j], rank5]
                    l.append(temp)





    return HttpResponse(l)
################


class courseList(APIView):
    

    def get(self, request, course):
        block1 =block.objects.filter(Type="chapter")
        serializer=blockSerializer(course1, many=True)
        return Response(serializer.data)
    

    def post(self):
        pass


