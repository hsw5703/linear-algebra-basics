# 수치미분 vs 해석미분
# 수치미분 : 미분 정의를 사용하여 x값 변화량을 최소화하는 극한 개념을 이용한다.
# 해석미분 : 미분 공식을 사용하는 방법

def f(x):
    return 20 * (x - 2) ** 2 + 500


def numerical_diff(f, x):
    h = 1e-4  # 10e-50은 너무 작아서 안 된다. 1e-4가 보통 가장 적절하다.
    return (f(x + h) - f(x)) / h


def analytic_diff(x):
    return 40 * x - 80


print(f'Numerical Diffirentiation Value : {numerical_diff(f, 2)}')  # 함수도 객체이므로 값으로 받을 수 있다.
print(f'Analytic Diffirentiation Value : {analytic_diff(2)}')

# 둘을 비교하면 거의 차이가 없음을 알 수 있다. Python에선 수치미분을 사용하여 함수의 최솟값 등을 구한다.(가중치 등을 고려해)

