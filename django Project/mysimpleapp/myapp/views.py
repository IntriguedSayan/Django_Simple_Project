from django.shortcuts import render
import os;
from django.http import JsonResponse;
from django.views.decorators.csrf import csrf_exempt
import os;
# Create your views here.


@csrf_exempt  
def readGivenFile(request):

    filePath =  r"C:\Users\sayan\OneDrive\Desktop\utils\The key components of an enterprise level application.txt"
    try:
        with open(filePath, 'r') as file:
            file_content = file.read();
        return JsonResponse({"file":file_content});
    except:
        err_msg = "FIle Not found";
        return JsonResponse(request,{"Err_Msg":err_msg});
    
@csrf_exempt
def addDataToFile(request):
    filePath =  r"C:\Users\sayan\OneDrive\Desktop\utils\The key components of an enterprise level application.txt"
    data = "Shawn Frost";
    try:
        with open(filePath,"a") as file:
          
            file.write(data+"\n");
        with open(filePath, 'r') as file:
            file_content = file.read();
        return JsonResponse({"msg":"Addedd data successfully","File":file_content});
    except:
        err_msg = "FIle Not found";
        return JsonResponse(request,{"err_msg":err_msg});   


@csrf_exempt
def delete_Localfile(request):
    filePath =  r"C:\Users\sayan\OneDrive\Desktop\utils\The key components of an enterprise level application.txt"
    try:
        file = os.remove(filePath);
        return JsonResponse({"msg":file});

    except OSError as e:
        return JsonResponse({"msg":f"Error: {e.filename} - {e.strerror}."});
