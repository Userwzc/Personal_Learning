import torch

w = torch.tensor([1.],requires_grad = True)
x = torch.tensor([2.],requires_grad = True)

a = torch.add(w,x)
b = torch.add(w,1)
y = torch.mul(a,b)

y.backward()
print(w.grad)

# 查看叶子节点
print("is_leaf:\n",w.is_leaf,x.is_leaf,a.is_leaf,b.is_leaf,y.is_leaf)

# 查看梯度    
print("gradient:\n",w.grad,x.grad,a.grad,b.grad,y.grad)

# 查看 grad_fn  grad_fn是用来记录创建张量时所用到的运算
print("grad_fn:\n",w.grad_fn,x.grad_fn,a.grad_fn,b.grad_fn,y.grad_fn)


# pytorch是典型的动态图，TensorFlow是静态图（TF 2.x 也支持动态图模式）

# 第一种判断：这就要看运算，是在计算图搭建之后，还是两者同步进行
# 先搭建计算图，再运算，这就是静态图机制
# 而在运算的同时去搭建计算图，这就是动态图机制

# 第二种判断: 也可以通过判断运算过程中，计算图是否可变动来区分静态图与动态图
# 在运算过程中，计算图可变动的是动态图；计算图不可变，是静止的，就是静态图