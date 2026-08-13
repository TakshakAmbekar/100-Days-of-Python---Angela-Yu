import setup
import time


screen = setup.screen
player = setup.player
cars = setup.cars
car_set = setup.cars.car_set
level = setup.level


def play():
    crashed = False
    while not crashed:
        time.sleep(0.02 * pow(0.9, level.level))
        if player.move(level.level_up):
            time.sleep(0.5)
            cars.reset()
        for car in car_set:
            car.move()
            crashed = player.crash(car.position())
            if crashed:
                time.sleep(1)
                break
        screen.update()
    
    level.game_over()

def main():
    restart = True
    while restart:
        setup.reset()
        play()
        restart = screen.textinput("Want to play again?", "Enter 'y' to play again, 'q' to quit") == 'y'
    
    screen.bye()
        
if __name__ == "__main__":
    main()
    
    
    