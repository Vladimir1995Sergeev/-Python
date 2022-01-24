from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        el = 0
        while el != 3:
            print(TrafficLight.__color[el])
            if el == 0:
                sleep(7)
            elif el == 1:
                sleep(2)
            elif el == 2:
                sleep(5)

            el += 1


t = TrafficLight()
t.running()