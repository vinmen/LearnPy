#Projectile Coordinates

import math

def plot_coordinates():
    for i in range(1, 100):
        t = i * 0.1
        x = 20.0 * t * math.cos(math.radians(70))
        y = (20.0 * t * math.sin(math.radians(70))) - ((9.81 * (t**2))/2)
        print(round(x), round(y), sep=',')
        if y <= 0:
            break

if __name__ == '__main__':
    plot_coordinates()