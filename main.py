import FreeBodyEngine as engine
import pygame
import moderngl

import sys
import game.game
import os

class colors: # stolen from some nerd on stack overflow
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == "__main__":
    flags = pygame.RESIZABLE  | pygame.DOUBLEBUF
    screen_size = (800, 800)
    profiler = False
    duration = 0
    profiler_length = 20
    fps = 60
    slowdraw = False
    use_SDL = False
    display = 0
    dev_mode = False
    asset_dir = "./assets/"
    production = False

    for arg in sys.argv:
        if arg.startswith("--fps"):
            value = arg.removeprefix("--fps=")
            if len(arg) == 0:
                print(colors.FAIL + "\n FPS Cap was not set because no value was provided.\n" + colors.ENDC)
                continue
            
            if not value.isnumeric():
                print(colors.FAIL + "\nFPS Cap was not set because the provided value was not an integer.\n" + colors.ENDC)
                continue

            fps = int(value)
            print(colors.OKGREEN + f"\nFPS Cap was set to {fps}.\n" + colors.ENDC)

        if arg.startswith("--slowdraw"):
            slowdraw = True

        if arg.startswith("--display"):
            display = int(arg.removeprefix("--display="))
            

        if arg.startswith("--size"):
            string = arg.removeprefix("--size=")
            if arg.find(":") == -1:
                print(colors.FAIL + "\nScreen Size not set because of invalid syntax, please use:" + colors.ENDC + " --size=x:y\n")
                continue

            i = string.index(":")
            x = string[0:i]
            if not x.isnumeric():
                print(colors.FAIL + "\nScreen Size not set because the x value was invalid.\n"+ colors.ENDC)
                continue

            if len(string) == i+1:
                print(colors.FAIL + "\nScreen Size not set because only one value was provided.\n"+ colors.ENDC)
                continue

            y = string[i+1:len(string)]
            if not y.isnumeric():
                print(colors.FAIL + "\nScreen Size not set because the y value was invalid.\n"+ colors.ENDC)
                continue

            screen_size = (int(x), int(y))
            print(colors.OKGREEN + f"\nScreen Size set to {screen_size}.\n" + colors.ENDC)

        if arg == "--fullscreen":
            pygame_flags = pygame_flags | pygame.FULLSCREEN
            screen_size = (0,0)

        if arg == "--profiler":
            profiler = True
            print(colors.OKGREEN + "\nStarted Profiler." + colors.ENDC)

        if arg == ("--SDL"):
            use_SDL = True
        
        if arg == ("--dev"):
            dev_mode = True
            asset_dir = "./dev/assets/"
        if arg == "--production":
            production = True

    if not use_SDL:
        flags = flags| pygame.OPENGL
    
    main = engine.core.Main(use_SDL, window_size=(screen_size), flags=flags, fps=fps, display=display, asset_dir=asset_dir)

    main.add_scene(engine.core.Scene(main), "game")
    
    if dev_mode == False or production == True:
        fb = main.files.load_image('engine/logo/FreeBodyTextLogoWhite.png', moderngl.BLEND)    
        pg = main.files.load_image('engine/logo/pygame_ce_powered.png', moderngl.BLEND)

        pg_scene = engine.core.SplashScreenScene(main, 4000, "fb_splash", pg,"#aaeebb", engine.core.FadeTransition(main, 250))
        fb_scene = engine.core.SplashScreenScene(main, 4000, "game", fb, "#0f0f0f", engine.core.FadeTransition(main, 250))

        main.add_scene(pg_scene, "pg_splash")
        main.add_scene(fb_scene, "fb_splash")
        main.change_scene("pg_splash")
    
    else:
        main.change_scene("game")

    main.run(profiler=profiler)






            