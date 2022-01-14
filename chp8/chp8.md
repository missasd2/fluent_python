
# chp8 对象引用、可变性和垃圾回收

python中变量不是盒子，而是对对象的引用

python中的赋值语句，应始终先读右边

```python
class Gizmo():
    def __int__(self):
        print("the id is : %(d)" % id(self))

        
x = Gizmo()
y = Gizmo()
```

is运算符：比较两个对象的标识（内存地址）
id（）函数：返回对象标识（内存地址）的整数形式表示；


### 8.2.1 在==和is之间选择

