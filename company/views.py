# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
# Create your views here.
from .forms import FormRegister
from .models import RegisterForm

def start(request):
	# import pdb;pdb.set_trace()
	if request.method =="POST":
		form=FormRegister(request.POST or None,request.FILES or None)
		if form.is_valid():
			post=form.save(commit=False)
			post.publish=timezone.now()
			post.save()
			list_data=RegisterForm.objects.all()
			return render(request,'content.html',{'list_data':list_data})
	else:
		form=FormRegister()

	return render(request,'home.html',{'form':form})






def edit(request,pk):
	# import pdb;pdb.set_trace()
	post= get_object_or_404(RegisterForm, pk=pk)
	if request.method == "POST":
		form= FormRegister(request.POST or None,request.FILES or None,instance=post)
		if form.is_valid():
			subject=form.save(commit=False)
			subject.publish=timezone.now()
			subject.save()

			# form1=FormRegister()
			return redirect('start')
	else:
		form = FormRegister(instance=post)
	return render(request,'home.html',{'form':form})



