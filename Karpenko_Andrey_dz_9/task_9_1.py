import itertools
import time


class TrafficLight:
    __color = [['красный', [7, 31]], ['жёльый', [2, 33]], ['зелёный', [7, 32]], ['жёлтый', [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end='')
            time.sleep(light[1][0])


t_l = TrafficLight()
t_l.running()
