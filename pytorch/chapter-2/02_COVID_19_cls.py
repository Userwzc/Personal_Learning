import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset,DataLoader
import torchvision.transforms as transforms
from PIL import Image

def main():
  # step 1 : 数据模块
  # step 2 : 模型模块
  # step 3 : 优化模块
  # strp 4 : 迭代模块

  # step 1/4 : 数据模块
  class COVID19Dataset(Dataset):
    def __init__(self,root_dir,txt_path,transform=None):
      self.root_dir = root_dir
      self.txt_path = txt_path
      self.transform = transform
      self.img_info = [] #[(path,label), ...]
      self.label_array = None
      self._get_img_info()
      
    def __getitem__(self, index):
      path_img,label = self.img_info[index]
      img = Image.open(path_img).convert('L')
      
      if self.transform is not None:
        img = self.transform(img)
        
      return img,label
      
    def __len__(self):
      if len(self.img_info) == 0:
        raise Exception("\ndata_dir:{} is a empty dir! Please cheakouut your path".format(
          self.root_dir))
      return len(self.img_info)
    
    def _get_img_info(self):
      """读取数据集"""
      #读取txt,解析txt
      with open(self.txt_path, "r") as f:
        txt_data = f.read().strip()
        txt_data = txt_data.split("\n")
        
      self.img_info = [(os.path.join(self.root_dir,i.split()[0]),int(i.split()[2]))
                       for i in txt_data]
      
  root_dir = "/home/wzc/Coding/Python/pytorch/chapter-2/covid-19-demo"
  img_dir = os.path.join(root_dir,"imgs")
  path_txt_train = os.path.join(root_dir, "labels","train.txt")
  path_txt_valid = os.path.join(root_dir,"labels","valid.txt")
  transforms_func = transforms.Compose([
    transforms.Resize((8,8)),
    transforms.ToTensor()
  ]) 
  train_data = COVID19Dataset(root_dir=img_dir,txt_path=path_txt_train,transform=transforms_func)
  valid_data = COVID19Dataset(root_dir=img_dir,txt_path=path_txt_valid,transform=transforms_func)
  train_loader = DataLoader(dataset=train_data,batch_size=2)
  valid_loader = DataLoader(dataset=valid_data,batch_size=2)
  
  #step 2/4 : 模型模块
  class TinyCNN(nn.Module):
    def __init__(self,cls_num=2):
      super(TinyCNN,self).__init__()
      self.conv = nn.Conv2d(1,1,kernel_size=(3,3))
      self.fc = nn.Linear(36,cls_num)
      
    def forward(self,x):
      x = self.conv(x)
      x = x.view(x.size(0),-1)
      out = self.fc(x)
      return out
    
  model = TinyCNN(2)
  
  #step 3/4:优化模块
  loss_f = nn.CrossEntropyLoss()
  optimizer = optim.SGD(model.parameters(),lr = 0.1,momentum=0.9,weight_decay=5e-4)
  scheduler = optim.lr_scheduler.StepLR(optimizer=optimizer,gamma=0.1,step_size = 50)
  
  # step : 迭代模块
  for epoch in range(100):
    # 训练集训练
    model.train()
    for data,labels in train_loader:
      # forward && backward
      outputs = model(data)
      optimizer.zero_grad()
      
      # loss 计算
      loss = loss_f(outputs,labels)
      loss.backward()
      optimizer.step()
      
      #计算分类准确度
      _,predicted  =torch.max(outputs.data,1)
      correct_num = (predicted == labels).sum()
      acc = correct_num / labels.shape[0]
      print("Epoch:{} Train Loss : {:.2f} Acc : {:.0%}".format(epoch,loss,acc))
    
    # 验证集验证
    model.eval()
    for data,label in valid_loader:
      # forward
      outputs = model(data)
      
      # loss 计算
      loss = loss_f(outputs,label)
      
      # 计算分类准确度
      _,predicted =  torch.max(outputs.data,1)
      correct_num = (predicted == label).sum()
      acc_valid = correct_num  / label.shape[0]
      print("Epoch:{} Valid Loss : {:.2f} Acc : {:.0%}".format(epoch,loss,acc_valid))
      
    #添加停止条件
    if(acc_valid == 1):
      break
  
    #学习率调整
    scheduler.step()
    
if __name__ == "__main__":
  main()
        
