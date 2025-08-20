import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    #make RandomWalk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #draw RandomWalk's points
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    points_numbers = range(rw.num_points)
    #ax.plot(rw.x_values, rw.y_values, c='pink')
    ax.scatter(rw.x_values, rw.y_values, c=points_numbers, cmap=plt.cm.Blues,
              edgecolors='none', s=1)
    ax.set_aspect('equal') #두 축의 비율을 같게 설정

    #highlight the initial point & end point
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False) #x축 제거
    ax.get_yaxis().set_visible(False) #y축 제거

    plt.show()

    #flag
    keep_running = input("Make another walk? (y/n):")
    if keep_running.strip().lower() == 'n':
        break