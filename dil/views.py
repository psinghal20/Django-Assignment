from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import User,UserDetail,Message,RoseRecord,YellowRoseRecord
from django.contrib.auth import authenticate, login,logout
from .forms import Login,SendMessage,Register
from django.urls import reverse
from itertools import chain

def index(request):
    if request.user.is_authenticated:
    	if hasattr(request.user,'userdetail'):
    		return HttpResponseRedirect(reverse('dil:dashboard',args=(request.user.username,)))
    register = Register()
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
           if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('dil:dashboard'))
            else :
            	form = Login()
                return render(request,'dil/index.html',{'form':form,'error_message':"Invalid Username/Password",'register':register})
    else:
        form = Login()
    return render(request, 'dil/index.html',{'form':form,'register':register})

def dashboard(request):
    if request.user.is_authenticated:
    	if request.user.is_staff:
    		logout(request)
    		return HttpResponseRedirect(reverse('dil:index'))
    	user_details = get_object_or_404(UserDetail,user=request.user)
    	ranked_list = UserDetail.objects.all().order_by('-red_rose')
    	listed = []
    	for x in ranked_list:
        	temp_user = x.user
        	listed.append(temp_user.username)
    	message_list = request.user.to_user_profile.all()
    	return render(request, 'dil/dashboard.html', {'user_details':user_details,'ranked_list':listed,'user_name':request.user.username,"message_list":message_list})
    else:
    	return HttpResponseRedirect(reverse('dil:index'))

def red_rose_inc(request,profile):
    if request.user.is_authenticated:
        user = get_object_or_404(User,username=profile)
    	user_details = get_object_or_404(UserDetail,user=user)
    	user_record = RoseRecord.objects.all()
    	x = 1
    	for record in user_record:
    		if user== record.to:
    			if request.user== record.frm:
    				x = 0
    	if x == 1:
    		user_details.red_rose=user_details.red_rose+1
    		user_details.save()
    		record = RoseRecord(to=user,frm=request.user)
    		record.save()
    	return HttpResponseRedirect(reverse('dil:visit_profile', args=(profile)))
    else:
    	return HttpResponseRedirect(reverse('dil:index'))

def yellow_rose_inc(request,profile):
    if request.user.is_authenticated:
        user = get_object_or_404(User,username=profile)
    	user_details = get_object_or_404(UserDetail,user=user)
    	frm_user= get_object_or_404(User,username=username)
    	user_record = YellowRoseRecord.objects.all()
    	x = 1
    	for record in user_record:
    		if user== record.to:
    			if request.user== record.frm:
    				x = 0
    	if x == 1:
    		user_details.yellow_rose=user_details.yellow_rose+1
    		user_details.save()
    		record = YellowRoseRecord(to=user,frm=request.user)
    		record.save()
    	return HttpResponseRedirect(reverse('dil:visit_profile', args=(profile,)))
    else:
    	return HttpResponseRedirect(reverse('dil:index'))

def visit_profile(request,profile):
    if request.user.is_authenticated:
        user_details = get_object_or_404(UserDetail,user=request.user)
    	visiting_user = get_object_or_404(User,username=profile)
    	visiting_user_details = get_object_or_404(UserDetail,user=visiting_user)
    	if visiting_user==request.user:
    		return HttpResponseRedirect(reverse('dil:dashboard',))
    	else:
    		ranked_list = UserDetail.objects.all().order_by('-red_rose')
    		if request.method == 'POST':
        		form = SendMessage(request.POST)
        		if form.is_valid():
        			sent_message = Message(to=visiting_user, frm=request.user ,message=request.POST["message"])
        			sent_message.save()
        			return HttpResponseRedirect(reverse('dil:visit_profile', args=(profile)))
    		else:
        		form = SendMessage()
    		listed = []
    		for x in ranked_list:
        		temp_user = x.user
        		listed.append(temp_user.username)
        	sent_message_list = Message.objects.filter(to=visiting_user,frm=request.user)
    		received_message_list = Message.objects.filter(frm=visiting_user,to=request.user)
    		result_list = list(chain(sent_message_list,received_message_list))
    		result_list = sorted(result_list)
    		return render(request, 'dil/VisitProfile.html', {'visiting_user_details':visiting_user_details,'user_details':user_details,'ranked_list':listed,'user_name':request.user.username,'profile_user':profile,'form':form,'result_list':result_list})
    else:
    	return HttpResponseRedirect(reverse('dil:index'))

def register(request):
	if request.method == 'POST':
		form = Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            branch = form.cleaned_data['branch']
            year = form.cleaned_data['year']
            dob = form.cleaned_data['dob']
            #user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user_details = UserDetail(user=user,dob=dob,branch=branch,year=year)
            user_details.save()
            login(request,user)
            return HttpResponseRedirect(reverse('dil:dashboard',))
	return HttpResponseRedirect(reverse('dil:index'))

def Logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('dil:index'))
