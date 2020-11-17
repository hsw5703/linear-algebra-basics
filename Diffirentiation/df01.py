# y=20(x-2)^2+500
# 수치미분 : 미분 정의를 사용하여 x값 변화량을 최소화하는 극한 개념을 이용한다.

def f(x) :
    return 20*(x-2)**2+500

def numerical_diff(f, x) :
    h = 1e-4 # 10e-50은 너무 작아서 안 된다. 1e-4가 보통 가장 적절하다.
    return (f(x+h)-f(x))/h

print(f'Diffirentiation Value : {numerical_diff(f, 1)}')
print(f'Diffirentiation Value : {numerical_diff(f, 2)}') # 함수도 객체이므로 값으로 받을 수 있다.
print(f'Diffirentiation Value : {numerical_diff(f, 3)}')