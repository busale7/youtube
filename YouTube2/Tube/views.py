from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Channel , Video
from django.contrib.auth import authenticate , login ,logout
from .forms import ChannelForm, VideoForm, SignupForm , LoginForm

# Create your views here.
def clip(request) :
	clips=Video.objects.all()
	context ={
		"clips" : clips

	}
	return render(request,"list.html", context)

def channels(request) :
	context = {
		"channelss" : Channel.objects.all(),

	}
	return render(request, "channels.html", context)

def videoDetail(request, video_id): 
	context ={
		"clips": Video.objects.get(id=video_id),

	}
	return render(request, "video_detail.html", context)


def channelDetail(request, channel_id): 
	context ={
		"channelss": Channel.objects.get(id=channel_id),

	}
	return render(request, "channel_detail.html", context)
 
def update_channel(request, channel_id):
 	channel_obj =Channel.objects.get(id=channel_id)
 	form =ChannelForm(instance=channel_obj)
 	if request.method=="POST":
 		form=ChannelForm(request.POST, instance=channel_obj)
 		if form.is_valid():
 			form.save()
 			return redirect('detail', channel_id=channel_obj.id)
 	context ={
 		"form":form,
 		"channel": channel_obj,
 	}
 	return render(request, 'update_channel.html', context)

def update_video(request, video_id):
 	video_obj =Video.objects.get(id=video_id)
 	form =VideoForm(instance=video_obj)
 	if request.method=="POST":
 		form=VideoForm(request.POST, instance=video_obj)
 		if form.is_valid():
 			form.save()
 			return redirect('vdetail', video_id=video_obj.id)
 	context ={
 		"form":form,
 		"video": video_obj,
 	}
 	return render(request, 'video_update.html', context)


def delete_channel(request, channel_id):
	Channel.objects.get(id=channel_id).delete()
	return redirect('channel_list')

def delete_video(request, video_id):
	Video.objects.get(id=video_id).delete()
	return redirect('list')

def create_channel(request):
	form =ChannelForm()
	if request.method=="POST":
		form =ChannelForm(request.POST)
		if form.is_valid():
			channel=form.save(commit=False)
			channel.creator =request.user
			channel.save()
			return redirect('channel_list')
	context ={
		'form':form

	}
	return render(request,'create_channel.html',context)


def create_video(request):
	form =VideoForm()
	if request.method=="POST":
		form = VideoForm(request.POST)
		if form.is_valid():
			video=form.save(commit=False)
			video.name =request.user
			video.save()
			return redirect('list')
	context ={
		'form':form

	}
	return render(request,'create_video.html',context)
