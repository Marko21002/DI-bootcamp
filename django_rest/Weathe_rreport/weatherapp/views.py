from django.shortcuts import render
from .models import Report
from django.views.decorators.csrf import csrf_exempt
from .serializers import ReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import(IsAdminUser,IsAuthenticated,AllowAny)
from rest_framework import generics

# Create your views here.

# class ReportView(APIView):
#     permission_classes = (IsAdminUser,)
    
#     def get(self, request,*args,**kwargs):
#         queryset = Report.objects.all()
#         serializer = ReportSerializer(queryset,many =True)
#         return Response(serializer.data)

# Create your views here.
class PostListView(generics.ListAPIView):
   queryset = Report.objects.all()
   serializer_class = ReportSerializer
#    def get_queryset(self):
#        report_title = self.request.query_params.get('title',None)
#        if report_title is not None:
#            queryset = Report.objects.filter(title = report_title)
#        else:
#            queryset = Report.objects.all()
       
   
class PostDeleteView(generics.DestroyAPIView):
   queryset = Report.objects.all()
   serializer_class = ReportSerializer
   
   
class PostDetailView(generics.RetrieveAPIView):
   queryset = Report.objects.all()
   serializer_class = ReportSerializer

class ForecasterDetailView(generics.RetrieveAPIView):
   queryset = Report.objects.all()
   serializer_class = ReportSerializer

