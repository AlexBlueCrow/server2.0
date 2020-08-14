from django.shortcuts import render
from wxapp.models import Order,Item,Captain,User,Order,Comments,FarmUser,User
from wxapp.serializers import OrderSerializer,ItemSerializer,FarmUserSerializer
from django.http import HttpResponse,HttpResponseNotFound
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt,csrf_protect
from server.settings import MEDIA_ROOT,MEDIA_URL
from .models import AdminUser,VideoFiles,PicFiles,VIMap,Key
import jwt
from rest_framework_jwt.settings import api_settings
import csv as csvreader
from rest_framework.authtoken.models import Token
from wxapp.views import JSONResponse
from .serializers import AdminUserSerializer,VideoFilesSerializer,PicFilesSerializer,VIMapSerializer,KeySerializer
from django.utils import timezone
# Create your views here.




def order(request):
    start=request.GET.get('date1')
    end=request.GET.get('date2')
    farm_name = request.GET.get('farmname')
    try:
        orders = Order.objects.filter(effect_time__range=(start,end),name = farm_name)
        orders_serializer = OrderSerializer(orders,many=True)
        return JSONResponse(orders_serializer.data)
    except:
        return JSONResponse({'code':20000,'data':{'msg':'目标范围无数据'},})

@csrf_exempt
def VIMap_update(request):
    itemid = request.POST.get('itemid')
    farmname = request.POST.get('farmname')
    links = VIMap.objects.filter(item_id=itemid)
    new_ids = []
    old_ids = []
    farm = FarmUser.objects.get(name=farmname)
    item = Item.object.get(id = itemid)
    for link in links:
        old_ids.append(link.video_id)
    i = 0
    while True:
        vid = request.POST.get('videoids['+ str(i) +']')
        if vid:
            new_ids.append(vid)
            i+=1
        else:
            break
    for id in old_ids:
        if id not in new_ids:
            link = VIMap.objects.get(item_id=itemid,video_id=id)
            link.delete()
    for id in new_ids:
        if id not in old_ids:
            link = VIMap.objects.create(
                farm = farm,
                item_id = itemid,
                video_id = id,
                name = item.itme_name+'---'+str(id)
            )
    return JSONResponse({'code':20000,'data':{'msg':'更新成功'},})



@csrf_exempt
def Item_update(request):
    if request.method == 'POST':
        item_id = request.POST.get('id')
        item_name = request.POST.get('itemname')
        category = request.POST.get('class')
        price = request.POST.get('price')
        size = request.POST.get('size')
        farmname = request.POST.get('farmname')
        video_file = request.FILES.get('video')
        pic_file = request.FILES.get('pic')
        is_active = request.POST.get('active')
        mode = request.POST.get('mode')
        
        #stock and mode to be added

        item = Item.objects.get(id=item_id)
        item.name = item_name
        item.category = category
        item.item_price = price
        item.unit = size
        item.status = is_active
        item.save()
        item.mode = mode
        #
        if video_file:
            video_pf=video_file.name.split('.')[-1]
            video_file.name = farmname +'-'+ item_name + str(timezone.localtime()) + '.' + video_pf
            newvideo =  VideoFiles.objects.create(
                itemname = item_name,
                farmname = farmname,
                video = video_file
            )
            item.video_address = video_file.name
            item.save()
        if pic_file:
            pic_pf=pic_file.name.split('.')[-1]
            pic_file.name = farmname +'-'+ item_name + str(timezone.localtime()) + '.' + pic_pf 
            newpic = PicFiles.objects.create(
                itemname = item_name,
                farmname = farmname,
                pic = pic_file
            )
            item.pic_address= pic_file.name
            item.save()
        return JSONResponse({'code':20000,'data':{'msg':'更新成功'},})
    else:
        
        return HttpResponse('error')


@csrf_exempt
def Item_API(request):
    if request.method == 'POST':

        video_file = request.FILES.get('video')
        pic_file = request.FILES.get('pic')
        contact = request.POST
        item_name = request.POST.get('itemname')
        name = request.POST.get('name')
        category = request.POST.get('class')
        price = request.POST.get('price')
        size = request.POST.get('size')
        farmname = request.POST.get('farmname')
        mode  = request.POST.get('mode')
        status = request.POST.get('active')
        print(mode,status)
        try:
            farmuser = FarmUser.objects.get(name=farmname)
        except:
            return HttpResponse('该农场不在系统中，请先创建农场')
        ##rename files with farm_name and item_name
        pic_pf=pic_file.name.split('.')[-1]
        video_pf=video_file.name.split('.')[-1]
        identifier= farmuser.name+'--'+item_name
        timestamp = str(timezone.now()).replace(':', '').replace(' ','_')
        pic_file.name= identifier+timestamp+'.'+pic_pf
        video_file.name= identifier+timestamp+'.'+video_pf
        new_video = VideoFiles.objects.create(
            name = video_file.name,
            itemname = item_name,
            farmid = farmuser.id,
            video = video_file
        )
        new_pic = PicFiles.objects.create(
            name = pic_file.name,
            itemname = item_name,
            farmid = farmuser.id,
            pic = pic_file
        )
        created = Item.objects.create(
            name=item_name,
            owner = farmuser,
            category = category,
            price = price,
            unit = size,
            video_address = video_file.name,
            pic_address= pic_file.name,
            mode = mode,
            status = status
        )
        created.save()
        return HttpResponse('success')

    if request.method == 'GET':
        farmname = request.GET.get('farmname')
        try:
            farmuser = FarmUser.objects.get(name=farmname)
            items = Item.objects.filter(owner = farmuser)
            items_ser = ItemSerializer(items,many=True)
            return JSONResponse({'code':20000,'data':items_ser.data})
        except:
            return HttpResponse('农场未创建')
    


    if request.method == 'PUT':
        
        data = JSONParser().parse(request)
    
        video_file = request.FILES.get('video')
        pic_file = request.FILES.get('pic')
        
        item_id = request.POST.get('id')
        item_name = request.POST.get('itemname')
        category = request.POST.get('class')
        price = request.POST.get('price')
        size = request.POST.get('size')
        farmname = request.POST.get('farmname')
        video_file = request.FILES.get('video')
        pic_file = request.FILES.get('pic')
        
        
        item = Item.objects.get(id=item_id)
        item.name = item_name
        item.category = category
        item.price = price
        item.unit = size
        item.save()
        if video_file:
            video_pf=video_file.name.split('.')[-1]
            video_file.name = farmname +'-'+ item_name + str(timezone.localtime()) + '.' + video_pf
            newvideo =  VideoFiles.objects.create(
                itemname = item_name,
                farmname = farmname,
                video = video_file
            )
            item.video_address = video_file.name
            item.save()
        if pic_file:
            pic_pf=pic_file.name.split('.')[-1]
            pic_file.name = farmname +'-'+ item_name + str(timezone.localtime()) + '.' + pic_pf 
            newpic = PicFiles.objects.create(
                itemname = item_name,
                farmname = farmname,
                pic = pic_file
            )
            item.pic_address= pic_file.name
            item.save()
        return JSONResponse({'code':20000,'data':{'msg':'更新成功'},})


         

    if request.method == 'DELETE':
        item_id = request.GET.get('id') 
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            return JSONResponse({'code':20000,'data':{'msg':'已删除'},})
        except:
            return JSONResponse({'code':20000,'data':{'msg':'删除失败'},})

    return JSONResponse({'code':20000,'data':{'msg':'error'},})
        
        
        
    

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({})


    
@csrf_exempt
def csv(request):
    if request.method == 'POST':
        csvfile = request.FILES.get('csvfile')
        name = csvfile.name
        csv_reader=csvreader.reader(open('homepage/csv/'+name,encoding='utf-8'))
        num=0
        titles=[]
        i=0
        for row in csv_reader:
            if num==0:
                for item in row:
                    titles.append(item)
                for item in titles:
                    i+=1
                num+=1
            else:
              pass
                #new = FarmUser.objects.create(
                #)
                #print(new)
                #new.save()
        return HttpResponse('good')
  
        
        
@csrf_exempt    
def Farm_API(request):
    if request.method=='GET':
        farmname = request.GET.get('farmname')
        farm_obj = FarmUser.objects.get(name = farmname)
        farm_serializer = FarmUserSerializer(farm_obj,many=False)
        return JSONResponse({'code':20000,'data':farm_serializer.data})
    if request.method == 'POST':
        farmname = request.POST.get('farmname')
        address = request.POST.get('address')
        description = request.POST.get('description')
        phonenumber = request.POST.get('phonenumber')
        contact = request.POST.get('contact')
        farm_type = request.POST.get('type')
        fuser = FarmUser.objects.get(name=farmname)
        fuser.address = address
        fuser.description = description
        fuser.phonenumber = phonenumber
        fuser.contact = contact
        fuser.type = farm_type
        fuser.save()
        msg1='info_update_success'
        logo = request.FILES.get('logo')
        msg = 'no_new_logo'
        if logo:
            logo_pf= logo.name.split('.')[-1]
            logo_fname = farmname+'-logo'+'.'+logo_pf
            logo.name = logo_fname
            identifier = farmname+'-logo'
            try:
                static= PicFiles.objects.create(
                    name = identifier,
                    pic = logo,
                )
                msg = '头像创建成功'
                fuser.logo=logo_fname
                fuser.save()
            except:
                static = PicFiles.objects.get(name = identifier)
                static.pic = logo
                static.save()
                msg = '头像更新成功'
                fuser.logo=logo.name
                fuser.save()    
        return JSONResponse({'code':20000,'data':{'res':msg1,'msg':msg},})

@csrf_exempt
def video_API(request):
    if request.method == 'GET':
        farmname = request.GET.get('farmname')
        farm_obj = FarmUser.objects.get(name = farmname)
        try:
            videos = VideoFiles.objects.filter(farmid = farm_obj.id)
            videos_serializer = VideoFilesSerializer(videos,many = True)
            return JSONResponse({'code':20000,'msg':'请求成功','data':videos_serializer.data})
        except:
            return JSONResponse({'code':20000,'msg':'无视频','data':''})

    if request.method == 'POST':
        farmname = request.POST.get('farmname')
        farm_obj = FarmUser.objects.get(name = farmname)
        desc = request.POST.get('desc')
        video = request.FILES.get('video')
        cover = request.FILES.get('cover')
        name = request.POST.get('name')
        
        try:
            new  = VideoFiles.objects.create(
                name = name,
                description = desc,
                farmid = farm_obj.id,
                video = video,
                cover = cover,
            )
            new.save()
            return JSONResponse({'code':20000,'msg':'上传成功'})
        except:

            return JSONResponse({'code':20000,'msg':'上传失败，请尝试重命名视频文件'})



