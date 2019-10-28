Thank you for downloading and I hope this recipe helps you!

All assets included in this folder were created by LunaLucid (or Namastaii from Lemma Soft forums). https://lunalucid.itch.io

*All images (buttons, backgrounds, etc) are free to use, with or without credit to Lunalucid so feel free to use these in your projects/games. I have included some PSD files in the images folder.*

*Fonts 'Sacramento' and 'Share Tech Mono' were provided by Google Fonts and is under an open source license, meaning you can use their fonts in any non-commercial or commercial project. You can find more fonts from Google at https://fonts.google.com*

###### Basic example:

![example image](https://i.ibb.co/GcMj0nj/1.gif)

* Define a variable you'll use to store the user's input.
* Define a function that stores that input.

```python
init:
    default myinput_1 = ""

init python:
    def change_myinput1(newstring):                                          
        store.myinput_1 = newstring
```

* Create the screen.
* Define a screen variable that decides if the input is active or not.
* Put the input and the text placeholder on the screen and connect it to the function you created. Clicking the input changes **input_on** to **True** and once clicked again, will set it back to **False**.

```python
screen simple_button_input():
    default input_on = False
    modal True


    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "Click to type!"
            button:
                background Frame(Solid("#ffc"))
                xsize 400
                if input_on:                                                  
                    input default myinput_1 changed change_myinput1
                    action SetScreenVariable("input_on", False)      
                else:
                    text myinput_1                                           
                    action SetScreenVariable("input_on", True)             


            textbutton "close" action Hide("simple_button_input")
```
###### Some good things to know:
* **default** - the default value of the input (in this case, the variable itself)
* **length** - maximum amount of characters user is allowed to input
* **pixel_width** - maximum pixels wide for user input
* **allow** - string list of characters that user is allowed to input
* **exclude** - string list of characters that user is not allowed to input
