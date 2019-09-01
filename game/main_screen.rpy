screen main():
    modal True
    imagemap:
        add "images/background.png"

        ground "images/idle.png"
        hover "images/hover.png"
        selected_idle "images/selected.png"

        hotspot (363, 50, 350, 93) action Show("button_input")
        hotspot (785, 50, 350, 93) action Show("imagemap_input")
        hotspot (1207, 50, 350, 93) action Show("desktop")

        hbox:
            xalign 0.5
            yalign 1.0
            textbutton "Basic button version" action Show("simple_button_input")
            textbutton "|"
            textbutton "Basic imagemap version" action Show("simple_imagemap_input")
            textbutton "|"
            textbutton "Exit" action Quit()
