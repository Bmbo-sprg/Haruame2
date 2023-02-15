# init python:
#     import datetime
#     dt = datetime.datetime.today()
#     minute_elapsed = dt.hour * 60 + dt.minute

# image logo_bg:
#     "gui/day_gradient.png"
#     crop (1111, 0, 1, 1080)
#     xsize 1920
#     matrixcolor BrightnessMatrix(0.4)

image logo_bg = "#FFFFFF"

image logo = "menu/logo.png"

label splashscreen:
    scene logo_bg
    with Pause(0.5)

    show logo at truecenter:
        zoom 0.5
    with dissolve
    with Pause(2)

    hide logo
    with dissolve
    with Pause(0.5)

    return
