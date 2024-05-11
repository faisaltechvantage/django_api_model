from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import User
from .serializers import *
from base.functions import *
# Create your views here.

# Success response
def success_response(data=None, message="Success", status_code= status.HTTP_200_OK):
    return Response({
        "status": "success",
        "message": message,
        "data": data
    }, status= status_code)

# Error response
def error_response(message="Error", errors=None, status_code=status.HTTP_400_BAD_REQUEST):
    print(99)
    response_data = {
        "status": "error",
        "message": message
    }
    if errors:
        response_data["errors"] = errors
    return Response(response_data, status=status_code)

# user registration view
class UserRegistration(APIView):
    def post(self, request):
        try:
            email = request.data.get("email")
            # Check if email already exists
            emailexist= User.objects.filter(email= email)
            if emailexist:
                return error_response(message= "Email already exist", errors= "Email already exist", status_code= status.HTTP_400_BAD_REQUEST)
            
            serializer = UserSerializer(data=request.data)
            
            # Validate serializer data
            if serializer.is_valid():
                # Save user
                serializer.save()
                return success_response(data= serializer.data, message= "User added successfully", status_code= status.HTTP_201_CREATED)
            else:
                # Return validation errors
                return error_response(message= "error", errors= serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_message = str(e)
            return error_response(message= "error", errors= error_message, status_code= status.HTTP_500_INTERNAL_SERVER_ERROR)

# user details updation view  
class UserDetailsUpdate(APIView):
    def put(self, request):
        try:
            user_instance = User.objects.get(pk=request.data["user_id"])
            serializer = UserDetailsUpdateSerializer(instance= user_instance, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return success_response(data= serializer.data, message= "User details updated", status_code= status.HTTP_200_OK)
            else:
                return error_response(message= "error", errors= serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_message = str(e)
            return error_response(message= "error", errors= error_message, status_code= status.HTTP_500_INTERNAL_SERVER_ERROR)

# user list api
class UserList(APIView):
    def get(self, request):
        try:
            page_number = request.GET.get("page")
            page_size= request.GET.get("page_size")
            if not page_size:
                page_size= 5
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            pagination= Paginator(serializer.data, page_size)
            try:
                page_obj = pagination.get_page(page_number)  # returns the desired page object
            except PageNotAnInteger:
                # if page_number is not an integer then assign the first page
                page_obj = pagination.page(1)
            except EmptyPage:
                # if page is empty then return last page
                page_obj = pagination.page(pagination.num_pages)
            return success_response(data= page_obj.object_list, message= "User details", status_code= status.HTTP_200_OK)
        except Exception as e:
            error_message = str(e)
            return error_response(message="Error retrieving user list", errors=error_message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# user delete api  
class UserDelete(APIView):
    def delete(self, request):
        try:
            user_instance = User.objects.get(pk=request.data["user_id"])
            if user_instance:
                user_instance.delete()
                return success_response(data= None, message= "User deleted", status_code= status.HTTP_200_OK)
            else:
                return error_response(message= "error", errors= user_instance.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_message = str(e)
            return error_response(message= "error", errors= error_message, status_code= status.HTTP_500_INTERNAL_SERVER_ERROR)

# operations
class Operations(APIView):
    def get(self, request):
        try:
            user_instance = User.objects.filter()
            print(user_instance)
            for i in user_instance:
                print(i.name)
            if user_instance:
                return success_response(data= None, message= "Details", status_code= status.HTTP_200_OK)
            else:
                return error_response(message= "error", errors= user_instance.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            error_message = str(e)
            return error_response(message= "error", errors= error_message, status_code= status.HTTP_500_INTERNAL_SERVER_ERROR)