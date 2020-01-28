# -*- coding: utf-8 -*-
#BMI指数计算小程序

height = float(input("请输入您的身高：\n"))
weight = float(input("请输入您的体重： \n"))
bmi = float(weight/(height**2))
type(bmi)
if bmi < 18.5:
    print("您的BMI指数为：",bmi)
    print("您的体重过轻。")
elif 25 >= bmi >= 18.5:
    print("您的BMI指数为：",bmi)
    print("您的体重正常。")
elif 28 >= bmi > 25:
    print("您的BMI指数为：",bmi)
    print("您的体重过重。")
elif 32 >= bmi > 28:
    print("您的BMI指数为：",bmi)
    print("您的体重过于肥胖！")
elif bmi > 32:
    print("您的BMI指数为：",bmi)
    print("您的体重严重肥胖！")
    pass

