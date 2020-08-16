from django.shortcuts import render
#from appThree.models import User
from appThree.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'appThree/index.html')

def users(request):
    # user_list = User.objects.order_by('first_name')
    # user_dict = {'users': user_list}
    # return render(request, 'appThree/users.html',context = user_dict)
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error: Form Invalid")
    return render(request,'appThree/users.html',{'form':form})
