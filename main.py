import FreeBodyEngine as engine
import pygame
import sys
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

    for arg in sys.argv:
        if arg.startswith("--fps"):
            value = arg.removeprefix("--fps=")
            if len(arg) == 0:
                print(colors.Fail + "\n FPS Cap was not set because no value was provided.\n" + colors.ENDC)
                continue
            
            if not value.isnumeric():
                print(colors.Fail + "\nFPS Cap was not set because the provided value was not an integer.\n" + colors.ENDC)
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

    if not use_SDL:
        flags = flags| pygame.OPENGL
    
    main = engine.core.Main(use_SDL, window_size=(screen_size), flags=flags, fps=fps, display=display)
    main.add_scene(engine.core.Scene(main), "main")
    main.set_scene("main")
    main.run(profiler=profiler)






            