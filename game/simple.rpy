####Simplified version for easier learning :)
#Some notes:
#default - the default value of the input (in this case, the variable itself)
#length - maximum amount of characters user is allowed to input
#pixel_width - maximum pixels wide for user input
#allow - string list of characters that user is allowed to input
#exclude - string list of characters that user is not allowed to input
################################################################################

default myinput_1 = ""
default myinput_2 = ""

init python:
    def change_myinput1(newstring):                                             #Functions that allow us to store the input
        store.myinput_1 = newstring
    def change_myinput2(newstring):
        store.myinput_2 = newstring
################################################################################
screen simple_button_input():
    default input_on = False                                                    #Screen variable for input
    modal True                                                                  #Prevents user from accidentally clicking out of the screen


    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "Click to type!"
            button:
                background Frame(Solid("#ffc"))
                xsize 400
                if input_on:                                                    #Only activate input after the user has clicked the button
                    input default myinput_1 changed change_myinput1
                    action SetScreenVariable("input_on", False)                 #Pressing enter turns input back off
                else:
                    text myinput_1                                              #If input_on variable is false, display text instead
                    action SetScreenVariable("input_on", True)                  #Activate input


            textbutton "close" action Hide("simple_button_input")
################################################################################
screen simple_imagemap_input():
    default input_on = False
    modal True

    imagemap:
        ground "images/post-it.png"
        hover "images/post-it_hovered.png"

        hotspot(785, 390, 350, 300) action ToggleScreenVariable("input_on", True)

        if input_on:
            input default myinput_2 changed change_myinput2 pos(830,480) xsize 300 length 50
        else:
            text myinput_2 area(830,480, 300,250)


        textbutton "close" pos(785, 735) action Hide("simple_imagemap_input")
