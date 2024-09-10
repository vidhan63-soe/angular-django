from rest_framework import serializers
from EmployeeAPP.models import Departments,Employees

class DepartmentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields= ('DepartmentID',
                'DepartmentName')
        
class EmployeeSerialize(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields= ('EmployeeId',
                'EmployeeName',
                'Department',
                'DateofJoining',
                'PhotofileName')