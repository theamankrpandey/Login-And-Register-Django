from django.shortcuts import render,redirect
from .models import Employee
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
    return render(req,'login.html')