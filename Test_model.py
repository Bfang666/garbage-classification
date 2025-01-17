import sys
import torch
from PIL import Image
from torchvision import transforms
import visdom
from torch import optim , nn
import os
classes=('harmful','kitch','others','recyc')
if torch.cuda.is_available():
	device = torch.device('cuda')
	transform = transforms.Compose([
		transforms.Resize(256),
		transforms.CenterCrops(224),
		transforms.ToTensor(),
		transforms.Normalize(mean=[0.485,0.456,0.406],
				std=[0.229,0.224,0.225])
			])
else:
	device = torch.device('cpu')
	transform=transforms.Compose([
		transforms.Resize(256),
		transforms.CenterCrop(224),
		transforms.ToTensor(),
		transforms.Normalize(mean=[0.485,0.456,0.406],
				std=[0.229,0.224,0.225])
			])
def predict(img_path):
	if torch.cuda.is_available():
		net=torch.load('model.dll',map_location='cuda')
		net=net.to(device)
		torch.no_grad()
		img=Image.open(img_path)
		img=transform(img).unsqueeze(0)
		img_=img.to(device)
		outputs=net(img_)
		_,predicted=torch.max(outputs,1)
	else:
		net=torch.load('model.dll',map_location='cpu')
		net=net.to(device)
		torch.no_grad()
		img=Image.open(img_path)
		img=transform(img).unsqueeze(0)
		img_=img.to(device)
		outputs=net(img_)
		_,predicted=torch.max(outputs,1)
	print(classes[predicted[0]])
	path='connect.dll'
	if os.path.exists(path):
		os.remove(path)
	else:
		print('successfully create the file:connect.dll')
	if classes[predicted[0]]=='harmful':
		#print('1')
		create_file(1)
	if classes[predicted[0]]=='kitch':
		#print('2')
		create_file(2)
	if classes[predicted[0]]=='others':
		#print('3')
		create_file(3)
	if classes[predicted[0]]=='recyc':
		#print('4')
		create_file(4)
def create_file(a):
	if a==1:
		try:
			file=open('connect.dll','r+')
		except FileNotFoundError:
			file=open('connect.dll','a+')
	if a==2:
		try:
			file=open('connect.dll','r+')
		except FileNotFoundError:
			file=open('connect.dll','a+')
	if a==3:
		try:
			file=open('connect.dll','r+')
		except FileNotFoundError:
			file=open('connect.dll','a+')
	if a==4:
		try:
			file=open('connect.dll','r+')
		except FileNotFoundError:
			file=open('connect.dll','a+')
	write_file(a)
def write_file(a):
	if a==1:
		with open('connect.dll','a+',encoding='utf-8') as f:
			text='harmful'
			f.write(text)
	if a==2:
		with open('connect.dll','a+',encoding='utf-8') as f:
			text='kitch'
			f.write(text)
	if a==3:
		with open('connect.dll','a+',encoding='utf-8') as f:
			text='others'
			f.write(text)
	if a==1:
		with open('connect.dll','a+',encoding='utf-8') as f:
			text='recyc'
			f.write(text)

if __name__=='__main__':
	predict('./test/1.jpg')
