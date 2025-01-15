from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from.models import StudentFeesModel,StudentsDataModel,FeeCategoriesModel

# Create your views here.

def adminlogin(request):
    if request.method=='POST':
        name = request.POST['adminname']
        psw = request.POST['password']
        user = authenticate(request, username=name,password=psw)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid name/password...!"
            return render(request,"adminloginpage.html",{"error" : error})
    else:
         return render(request,"adminloginpage.html")
    


@login_required
def adminhome(request):
    obj = StudentFeesModel.objects.all()
    obb = StudentsDataModel.objects.count()
    sum = 0
    for i in obj:
        sum = sum + i.amount_paid
    
    rest = 0
    for j in obj:
        rest = rest + j.fee_category.amount - j.amount_paid

    print(obb)
    print(sum)
    print(rest)
    if obj and obb:
        return render(request,"adminhomepage.html",{"datas" : obj ,"count" : obb ,"total" : sum , "remaining" : rest})
    else:
        msg = "Currently no students with fees due..."
        return render(request,"adminhomepage.html",{"msg" : msg })



@login_required
def studentstable(request):
    data = StudentsDataModel.objects.all()
    obb = StudentsDataModel.objects.count()
    obt = StudentFeesModel.objects.all()
    sum = 0
    for i in obt:
        sum = sum + i.amount_paid
    
    rest = 0
    for j in obt:
        rest = rest + j.fee_category.amount - j.amount_paid

    if request.method=="POST":
        name = request.POST.get("studentname")
        data = StudentsDataModel.objects.filter(first_name__icontains=name)
        

    return render(request,"studentspage.html",{"datas" : data , "count" : obb ,"total" : sum , "remaining" : rest })




@login_required
def feescategorytable(request):
    obj = FeeCategoriesModel.objects.all()
    obb = StudentsDataModel.objects.count()
    obt = StudentFeesModel.objects.all()
    sum = 0
    for i in obt:
        sum = sum + i.amount_paid
    
    rest = 0
    for j in obt:
        rest = rest + j.fee_category.amount - j.amount_paid
    return render(request,"feescategorypage.html",{"datas" : obj , "count" : obb ,"total" : sum , "remaining" : rest})



@login_required
def delete_student(request,delete_id):
    obj = StudentsDataModel.objects.get(student_id=delete_id)
    print(obj)
    obj.delete()
    return redirect('/students')



@login_required
def edit_student(request,edit_id):
    obj = StudentsDataModel.objects.filter(student_id=edit_id)
    print(obj)
    if obj:
        return render(request,"updatestudent.html",{"editdata" : obj})
    else:
        return render(request,"studentspage.html")
    


@login_required
def update_student(request):
    if request.method=="POST":
        idno = request.POST.get('id')
        obj = StudentsDataModel.objects.get(student_id=idno)
        obj.first_name = request.POST.get('firstname')
        obj.second_name = request.POST.get('secondname')
        obj.class_name = request.POST.get('classname')
        obj.roll_number = request.POST.get('rollnumber')
        obj.email = request.POST.get('email')
        obj.save()
        print(obj)
        return redirect('/students')
    

@login_required
def view_student(request,view_id):
    student_viewdata = StudentsDataModel.objects.get(student_id=view_id)
    student_fee_data = StudentFeesModel.objects.filter(student=student_viewdata)
    return render(request,"viewstudent.html",{"data" : student_viewdata,"feesdata" : student_fee_data})


@login_required
def fees_update(request):
    students_fee_data = StudentFeesModel.objects.all()
    return render(request,"studentfeesupdate.html",{"datas" : students_fee_data})




@login_required
def student_fee_edit(request,fee_id):
    students_fee_obj = StudentFeesModel.objects.get(id=fee_id)
    if request.method == "POST":
        fee_amount = int(request.POST.get('fee'))

        if fee_amount >= students_fee_obj.remaining_amount() :
            students_fee_obj.status = "PAID"

        students_fee_obj.amount_paid = students_fee_obj.amount_paid+fee_amount
        students_fee_obj.save()
        return redirect('/feesupdate')


    return render(request,"feesedit.html",{"data" : students_fee_obj})





@login_required
def adminlogout(request):
    logout(request)
    return redirect('/')