from django.shortcuts import render,redirect
from .models import Employee,Department
from django.contrib import messages
# Create your views here.
def landing(req):
    return render(req,'landing.html')

def register(req):
    if req.method == 'POST':
        n = req.POST.get('name')
        i = req.FILES.get('profile')
        a = req.FILES.get('audio')
        v = req.FILES.get('video')
        r = req.FILES.get('resume')
        e = req.POST.get('email')
        p = req.POST.get('password')
        cp = req.POST.get('cpassword')
        g = req.POST.get('gender')
        s = req.POST.get('state')
        q = req.POST.get('qualification')

        user = Employee.objects.filter(Email=e)
        if user:
            msg = "Email Id is Already Exits!"
            return render(req, 'register.html', {'msg': msg})

        print(n, i, a, v, r, e, p, cp, g, s, q)

        if p == cp:
            Employee.objects.create(
                Name=n,
                Profile=i,
                Audio=a,
                Video=v,
                Resume=r,
                Email=e,
                Password=p,
                Cpassword=cp,
                Gender=g,
                State=s,
                Qualification=q
            )
            return redirect('login')
        else:
            userdata = {'name': n, 'email': e, 'gender': g}
            msg = "Password & Confirm_Password not matched"
            return render(req, 'register.html', {'pmsg': msg, 'data': userdata})
    return render(req, 'register.html')


def login(req):
    if req.method == "POST":
        e=req.POST.get('email')
        p=req.POST.get('password')
        if e=='ap5766709@gmail.com' and p=='pandey':
            a_data={
                'name':'Aman',
                'email':'ap5766709@gmail.com',
                'contact':'9934869719',
                'password':'pandey'}
            req.session['user_id']=a_data
            return redirect('admindashboard')
        else:
            user = Employee.objects.filter(Email=e)
            if not user:
                msg="Register First"
                return redirect('register')
            else:
                userdata=Employee.objects.get(Email=e)
                if p == userdata.Password:
                    req.session['user_id']=userdata.id
                    return redirect('userdashboard')
                else:
                    msg='Email & password not Match'
                    return render(req,'login.html',{'x':msg})
    return render(req,'login.html')

def userdashboard(req):
    if 'user_id' in req.session:
        x = req.session.get('user_id')
        userdata=Employee.objects.get(id=x)
        return render (req,'userdashboard.html',{'data':userdata})
    return redirect ('login')

def admindashboard(req):
    if 'user_id' in req.session:
        a_data = req.session.get('user_id')
        return render (req, 'admindashboard.html',{'data':a_data})
    else:
        return redirect('login')
    
def add_dept(req):
    if 'user_id' in req.session:
        a_data = req.session.get('user_id')
        return render (req, 'admindashboard.html',{'data':a_data,'add_dept':True})
    else:
        return redirect('login')
    
def save_data(req):
    if 'user_id' in req.session:
        if req.method=='POST':
            d_n=req.POST.get('name') 
            d_c=req.POST.get('code') 
            d_h=req.POST.get('head') 
            d_d=req.POST.get('description')
            dept=Department.objects.filter(Dep_name=d_n)
            if dept:
                messages.warning(req,'Department already exists')
                a_data=req.session.get('a_data')
                return render(req,'admindashboard.html',{'data':a_data,'add_dep':True})
            else:
                Department.objects.create(Dep_name=d_n,Dep_code=d_c,Dep_head=d_h,Dep_description=d_d)
                messages.success(req,"Department created")
                a_data=req.session.get('a_data')
                return render(req,'admindashboard.html',{'data':a_data,'add_dep':True})
    else:
        return redirect('login')
def show_dept(req):
    if 'user_id' in req.session:
        a_data = req.session.get('user_id')
        all_dept = Department.objects.all()  # <-- department list
        return render(req, 'admindashboard.html',
                      {'data': a_data,
                       'show_dept': True,
                       'all_dept': all_dept})
    else:
        return redirect('login')


# def reply(req,pk):
#     if 'user_id' in req.session:
#         q_data=Query.object.get(id=pk)
#         emp_all_query=Query.objects.all()
#         return render(req,{'data':a_data,'q_data':q_data,'emp_all_query':emp_all_query})

# def a_reply(req):
#     if 'user_id' in req.session:
#         q_old_data=Query.objects.get(id=pk)
#         if req.method=='POST':
#             ar=req.POST.get('a_reply')

def logout(req):
    if req.session.get('user_id',None):
        req.session.flush()
    return redirect('login')