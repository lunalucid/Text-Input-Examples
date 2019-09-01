##There is a lot going on on this page, mostly so you can see some additional things you can do with these screens
##Included in this folder is also the simplified version of this so you can see the functionality alone.
##Simplified version found in simple.rpy (includes a basic version of a button input and an imagemap input)

init python:
    import random
#Screen 1 functions#############################################################
    def change_input1(newstring):                                               #Functions that allow us to store the input
        store.input_1 = newstring
#Screen 2 functions#############################################################
    def change_input2(newstring):                                               #This one I've added a pencil sound effect for fun
        store.input_2 = newstring
        if renpy.display.interface.last_event.__dict__.get("key",None) == 8:    #This is checking if the player hits the backspace button
            renpy.music.play(renpy.random.choice(['sounds/erase1.ogg','sounds/erase2.ogg','sounds/erase3.ogg']), channel="audio")
        else:
            renpy.music.play(renpy.random.choice(['sounds/writing2.ogg','sounds/writing3.ogg','sounds/writing4.ogg']), channel="audio")
#Screen 3 functions#############################################################
    def change_username(newstring):
        store.username = newstring
    def change_hobby(newstring):
        store.hobby = newstring
    def change_gender(newstring):
        store.gender = newstring
    def suggest_username():
        addition = random.randint(0,1000)
        store.username = "{}{}".format(username,addition)
#Screen 1 styles################################################################
image my_caret:                                                                 #This is for that flashing line thingy next to your input :>
    Text("|", size=60)
    ypos -5
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat
style my_button:                                                                #Some styles..
    background Frame("images/button.png")
    xsize 400

style my_text:
    size 60
    hover_color "#b4b8f4"

style my_input:
    size 60
    caret "my_caret"
#Screen 1#######################################################################
screen button_input():
    default input_on = False                                                    #Screen variable for input
    add "images/overlay.png"                                                    #I like it, okay?
    modal True                                                                  #Prevents user from accidentally clicking out of the screen

    drag: #just for fun
        pos(720, 300)
        frame:
            background Frame("images/frame.png")
            xpadding 30
            has vbox:
                xalign 0.5
                text "Click to type!"
                button style_prefix "my":
                    if input_on:                                                #Only activate input after the user has clicked the button
                        input default input_1 changed change_input1
                        action SetScreenVariable("input_on", False)             #Pressing enter turns input back off
                    else:
                        if input_1 == "":
                            text "Click me"
                        else:
                            text input_1
                        action SetScreenVariable("input_on", True)              #Activate input


                    xalign 0.5
                textbutton "close" action Hide("button_input")
#Screen 2 styles################################################################
image my_caret2:
    Text("|", size=35, font="fonts/Sacramento/Sacramento-Regular.ttf")
    ypos -5
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat
style another_input:
    size 35
    caret "my_caret2"
    font "fonts/Sacramento/Sacramento-Regular.ttf"
    color "#000"
#Screen 2#######################################################################
screen imagemap_input():
    default input_on = False
    add "images/overlay.png"
    modal True

    imagemap:
        ground "images/post-it.png"
        hover "images/post-it_hovered.png"

        hotspot(785, 390, 350, 300) action ToggleScreenVariable("input_on", True)

        if input_on:
            input default input_2 changed change_input2 pos(830,480) xsize 300 length 80 style "another_input"
        else:
            text input_2 area(830,480, 300,250) style "another_input"

        if len(input_2) > 2:
            textbutton "close" pos(785, 735) action Hide("imagemap_input")
#Screen 3 styles################################################################
image retro_caret:
    xpos -4
    Text("|", font="fonts/Share_Tech_Mono/ShareTechMono-Regular.ttf", size=25)
    linear 0.3 alpha 0.0
    linear 0.3 alpha 1.0
    repeat
style retro_text:
    font "fonts/Share_Tech_Mono/ShareTechMono-Regular.ttf"
    caret "retro_caret"
    size 25
    adjust_spacing False
style error_msg:
    size 18
    color "#FF0000"
style confirmation_msg:
    size 18
    color "#008000"
#Screen 3#######################################################################
screen desktop():
    modal True
    imagemap:
        ground "images/desktop_background.png"
        hover "images/desktop_background_hovered.png"

        hotspot (7, 30, 141, 110) action Show("browser")
        hotspot (0, 1009, 138, 71) action [Hide("desktop"), Hide("browser")]

screen browser():
    default current_input = ""
    default confirmation = ""
    drag:
        pos(400,50)
        imagemap:
            ground "images/browser_background.png"
            hover "images/browser_background_hovered.png"
            selected_idle "images/browser_background_selected.png"

            hotspot (1231, 0, 40, 60) action Hide("browser")
            hotspot (445, 412, 349, 40) action SetScreenVariable("current_input", "username_input")
            hotspot (445, 469, 349, 40) action SetScreenVariable("current_input", "hobby_input")

            hotspot(444, 541, 18, 18) action SetVariable("gender", "female")
            hotspot(518, 541, 18, 18) action SetVariable("gender", "male")
            hotspot(591, 541, 18, 18) action SetVariable("gender", "N/A")

            if username !="":
                hotspot(570, 646, 100, 50) clicked [SetScreenVariable("current_input", ""), If(username=="lunalucid", [SetScreenVariable("confirmation", "That username is already taken!"), Function(suggest_username)], SetScreenVariable("confirmation", "Registration submitted!"))]

            if current_input == "username_input":
                input default username changed change_username exclude " " length 15 pos(450, 418) xsize 1280 style "retro_text"
            if current_input == "hobby_input":
                input default hobby changed change_hobby pos(450, 475) pixel_width 350 exclude "1234567890" style "retro_text"

            if current_input != "username_input":
                text username pos(450, 418) style "retro_text"
            if current_input != "hobby_input":
                text hobby pos(450, 475) style "retro_text"


            hbox:
                xalign 0.5
                yalign 0.9
                if "already taken" in confirmation:
                    text confirmation style "error_msg"
                else:
                    text confirmation style "confirmation_msg"
