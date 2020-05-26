from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
import pyodbc
from .models import smsonattente ,smstosend ,sys_paramt
import datetime
@api_view(['GET'])
@csrf_exempt
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def get_sms(request):
    rs=get_new_pv()
    updat_sms1(rs)
    updat_sms2()
    list_sms=get_sms_to()

    return JsonResponse({'data': list_sms})
def get_new_pv():
    d=sys_paramt.objects.all().filter(name="last_id_pv")
    if len(d)==0:
        d=sys_paramt(pr_value=0,name="last_id_pv")
        d.save()
    last_id_pv=sys_paramt.objects.all().filter(name="last_id_pv")[0]

    last_id_pv.save()

    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=SYSCTA100_01_2020;UID=sa;PWD=sa')
    cursor = conn.cursor()  # Cursor Establishment
    cursor.execute("""select NPV_AUTO,IMMAT, D_carte,   DATE_CONTR, NOM_PROPR, prenom_propr, ADR_PROPR, CODE_PROPR,  PROCH_CONTR,  tel_propr, portable_propr, z_id
                    from pv WHERE z_id > {} order by z_id """.format(last_id_pv.pr_value))  # Execute Query
    rs = [dict((cursor.description[i][0], value) \
        for i, value in enumerate(row)) for row in cursor.fetchall()]
    cursor.connection.close()
    rs2=[]
    if(len(rs)):
        last_id_pv.pr_value=str(rs[-1]['z_id'])
        last_id_pv.save()
        for i in rs:
            try :
                num_phone=False
                if i["tel_propr"]!="":
                    num_phone=i["tel_propr"]
                elif i["portable_propr"]!="":
                    num_phone=i["portable_propr"]
                if num_phone:
                    num_phone=is_phone(num_phone)
                if num_phone:
                    i["tel_propr"]=num_phone
                    del i['portable_propr']
                    rs2.append(i)
            except :
                pass
        update_smsonattente(rs2)
    return rs2
def update_smsonattente(rs):
    for i in rs:
        try:
            date=i["PROCH_CONTR"][21:31]
            date_p=datetime.datetime.strptime(date, '%d/%m/%Y')
            ns=smsonattente()
            ns.data=str(i)
            ns.name=i["NPV_AUTO"]
            ns.next_date_send=date_p
            ns.id_pv=i["z_id"]
            ns.save()
        except :
            pass
def is_phone(phone):
    try:
        l=[" ",".","-","_",";"]
        for i in l:
            phone=phone.replace(i,"")
        if phone[0] == "0" and phone[1] in ["6","7","5"] and len(phone)==10:
            return phone
        return False

    except :
        return False
def updat_sms1(rs):
    for i in rs:
        try :
            body_sms="المرسل : مزكز التقني لسيرات الرويني  \
            مرحبا بك السيد :{} {}  \
            نشكرك على الثقة بنا و نتمنى لك السلامة وسندكرك ان شاء الله \
            قبل حلول معد الصيانة القادم عن طريق sms ".format(i["NOM_PROPR"],i["prenom_propr"])
            nsts=smstosend()
            nsts.body_sms=body_sms
            nsts.num_phone =i["tel_propr"]
            nsts.id_pv=i["z_id"]
            nsts.save()
        except:
            pass
def updat_sms2():
    all_sms_t=smsonattente.objects.all().filter(status=False)
    date_n = datetime.date.today()
    for i in all_sms_t:
        date2 = i.next_date_send
        delt = date2 - date_n
        if delt.days<30:
            ii=eval(i.data)
            body_sms="المرسل : مزكز التقني لسيرات الرويني  \
            مرحبا بك السيد :{} {}  \
            نشكرك على الثقة بنا و نتمنى لك السلامة وسندكرك ان شاء الله \
            قبل حلول معد الصيانة القادم عن طريق sms ".format(ii["NOM_PROPR"],ii["prenom_propr"])
            nsts=smstosend()
            nsts.body_sms=body_sms
            nsts.num_phone =ii["tel_propr"]
            nsts.id_pv=ii["z_id"]
            nsts.save()
            i.status=True
            i.save()

@api_view(['POST','GET'])
@csrf_exempt
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def del_sms_to(request):
    list_z_ids=eval(request.data["list"].replace('"',''))
    all_sms=smstosend.objects.all()
    for i in list_z_ids:
        try:
            sms=all_sms.filter(id_pv=i)[0]
            sms.status=True
            sms.save()
        except:
            pass
    return JsonResponse({'data': False})


def get_sms_to():
    all_sms=smstosend.objects.all().filter(status=False)
    # smstosend.id_pv
    list_sms=[]
    for i in all_sms:
        d = {}
        d["body_sms"]=i.body_sms
        d["num_phone"]=i.num_phone
        d["id"]=i.id_pv
        list_sms.append(d)
    return list_sms
