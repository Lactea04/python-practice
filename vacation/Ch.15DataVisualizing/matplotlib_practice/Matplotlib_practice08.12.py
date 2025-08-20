import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots() #fig: 그래프 컬렉션 figure, ax: 그래프 이름을 ax로 지정
#ax.plot(input_values, squares, linewidth=3) #함수에 값 입력, 그래프 두께 설정 (그래프를 연속적으로 입력)

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.PuBu, s=10)
#점 지정 x, y, s는 점의 크기, 리스트를 이용하여 여러개의 점을 그릴 수 있음
#color에는 직접 어떤 색을 지정할 수도 있고 튜플 형태로 입력할 수도 있음, 0에 가까울수록 어둡고 1에 가까울수록 밝음
#color=(0.8,0.7,0.5) color='blue'
#colormap을 이용하여 gradation 넣을 수 있음 c=y_values, cmap=plt.cm.Blues #matplotlib사이트에서 가용 색상 확인





#그래프 타이틀을 지정하고 축에 이름표를 붙입니다.
ax.set_title("Square Numbers", fontsize=24) #제목 설정, 폰트크기 설정
ax.set_xlabel("Value", fontsize=14) #x축 이름 설정
ax.set_ylabel("Square of Value", fontsize=14) #y축 이름 설정

#틱 이름표 크기를 지정합니다
ax.tick_params(labelsize=14) #눈금 스타일 지정; 눈금 폰트 크기 지정
ax.ticklabel_format(style='plain') #눈금 이름표 커스텀, 여기선 일반적인 과학 표기법으로


#각 축의 범위를 지정
ax.axis([0, 1100, 0, 1_100_000]) #4가지의 매개변수 입력 x최소, x최대, y최소, y최대 0~1000, 0~1,000,000

#파일 형태로 저장가능 (파일이름 입력 경로를 입력하여 위치도 지정 가능, 필수 X지만 여기선 공백 제거 지정)
#plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show() #함수 출력