import matplotlib.pyplot as plt
import numpy as np

# ex.01

# plt.plot([2, 4, 5, 6], [81, 93, 91, 97])
# plt.show()

# ex.02

# a = [10, 20, 30, 40]  # y축 값만 할당하면 x축 값은 자동으로 0부터 할당된다.
# plt.plot(a)
# plt.show()

# ex.03

# fig = plt.figure()  # figure을 그래프를 그릴 도화지라고 생각하면 된다.
# split1 = fig.add_subplot(1, 1, 1)  # 행을 1개, 열을 1개 생성하고 1번째 플롯을 선택해 반환.
# split1.plot([2, 4, 5, 6], [81, 93, 91, 97])
# plt.show()

# ex.05

# fig = plt.figure()
# split1 = fig.add_subplot(2, 1, 1)  # 행을 2개, 열을 1개 생성하여 1번째 플롯을 선택해 반환.
# split1.plot([2, 4, 5, 6], [81, 93, 91, 97])
# split2 = fig.add_subplot(2, 1, 2)  # 행을 2개, 열을 1개 생성하여 2번째 플롯을 선택해 반환.
# split2.plot([1, 2, 3, 4], [100, 30, 40, 20])
# plt.show()

# ex.06

# fig = plt.figure()  # 선언시 새로운 그래프를 그릴 도화지를 생성.
#
# splt1 = fig.add_subplot(2, 2, 1)
# splt1.plot([2, 4, 5, 6], [81, 93, 91, 97])
#
# sp1 = fig.add_subplot(2, 2, 2)
# sp1.plot(np.random.randn(50).cumsum(), 'r-')
# # r-는 red에 실선을 뜻한다. 여러 표현 방법이 Python word 파일에 적혀있다.
# # cumsum()은 누적 합계를 뜻한다. 50번 째 데이터는 1~50까지 난수의 합이다.
# sp2 = fig.add_subplot(2, 2, 3)
# sp2.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# # x축 값은 0부터 100까지로 기본 설정대로이다. bins는 구간의 수이며 데이터들을 구간별로 나누어
# # 빈도를 출력한다. k는 검은색이며 alpha는 투명도를 나타낸다.
# # hist는 도수분포표를 나타낸다.
# sp3 = fig.add_subplot(2, 2, 4)
# sp3.scatter(np.arange(100), np.arange(100) + 3 * np.random.randn(100))
# plt.show()
# # scatter은 점산도를 뜻한다.


# ex.07

# fig, splts = plt.subplots(2, 2)  # 선언시 도화지(figure)와 그래프를 함께 선언.
#
# splts[0, 0].plot([2, 4, 5, 6], [81, 93, 91, 97])
# splts[0, 1].plot(np.random.randn(50).cumsum(), 'r-')
# splts[1, 0].hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# splts[1, 1].scatter(np.arange(100), np.arange(100) + 3 * np.random.randn(100))
# plt.show()

# ex.09
#
# fig, subplots = plt.subplots(2, 2, sharex=True, sharey=True)
# # sharex=True는 x축 틱을 공유한다. 비교를 위해 sharex=False를 첨부한다.
# for i in range(2):
#     for j in range(2):
#         subplots[i, j].hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
#
# plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
# # plt.tight_layout() tight_layout()을 사용하면 알맞게 위치를 조정해주기 때문에 subplots_adjust의 left
# # bottom, right, top, wspace, hspace를 설정해도 반영되지 않는다.
# # None은 0이 아니라 따로 설정을 하지 않는다는 뜻이다. 기본값을 제공한다.
# # wspace는 가로로 벌려주고, hspace는 세로로 벌려준다. 사진을 첨부.
# plt.show()

# ex.09 - 12

# fig, subplots = plt.subplots(1, 1)
# subplots.plot([10, 20, 30, 40], 'ko--', label='data1')
# # ko--는 '색은 black으로, Data는 점으로 표시, 점선으로 그려라'는 명령이다.
# # 색을 black이나 수로 표현하면 Error.
# subplots.plot([9, 15, 21, 27], color='red', linestyle='', marker='o', label='data2')
# # 하지만 구분하기 쉽게 명시적 방법으로 나타내는 것을 선호한다.
# # color는 red 또는 r 등으로 표현가능하고 linestyle=''은 선 없음을 뜻한다.
# # labeling을 해주지만 plt.legend()를 해주지 않으면 범례는 나오지 않는다.
#
# plt.legend(loc='best') # loc='best'를 생략해도 적절한 위치에 범례를 위치시켜준다.
# plt.show()

# ex.13

# fig, subplots = plt.subplots(1, 1)
# subplots.plot(np.random.randn(50).cumsum(), linestyle='-', marker='o', markersize=2)
# # marker='', marker=None, marker를 따로 설정하지 않는 것까지 세 가지 방식은 모두 같은 결과이다.
# # drawstyle은 'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'가 있다.
# plt.show()

# ex.14
#
# fig, subplots = plt.subplots(2, 1)
#
# subplots[0].plot(np.random.randn(1000).cumsum())
# subplots[1].plot(np.random.randn(1000).cumsum())
# subplots[1].set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# # subplots[0]은 따로 set_xticks를 해주지 않아 자동으로 설정된다.
# # set_xticks()는 x축의 틱 값을 임의로 설정한다.
#
# subplots[1].set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
#                             rotation=30, fontsize='small')
# # set_xticklabels는 set_xticks() 위에 새로이 이름을 설정한다. 단, 사전에 set_xticks()를 설정하지 않았다면 파이썬 임의로
# # 설정한 간격에 label이 입혀지므로 pt0~pt10까지 모든 label이 입혀진다는 보장이 없다. 또한 set_xticks()를 설정했다면
# # 그 틱의 숫자를 맞춰서 xticklabels를 설정해야 한다. rotation은 기울기, fontsize는 틱 이름의 크기를 뜻한다. 숫자도 가능.
#
# plt.show()

# ex.15-16

# fig, subplots = plt.subplots(2, 1)
#
# subplots[0].plot(np.random.randn(1000).cumsum())
# subplots[1].plot(np.random.randn(1000).cumsum())
# subplots[1].set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# subplots[1].set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
#                              rotation=30, fontsize='small')
# subplots[1].set_xlabel('Points')
# subplots[1].set_title('My First Matplotlib Plot')
# subplots[0].set_ylabel('ylabel')
# plt.tight_layout()
# plt.show()

# fig, subplots = plt.subplots(1, 1)
#
# subplots.plot(np.random.randn(1000).cumsum())
# subplots.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# subplots.set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
#                              rotation=30, fontsize='small')
# plt.title('My First Matplotlib Plot')
# plt.xlabel('Points')
# plt.show()