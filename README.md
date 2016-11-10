# Kivy BorderImage Tool
## Kivy BorderImage based widgets made easy

The application is really easy to use: simply open the image that interests you (PNG or JPG) and with the set of sliders you can easily tune the widget BorderImage properties.

![screenshot](https://github.com/rafalo1333/KivyBorderImageTool/blob/master/screenshot.png "Screenshot")

Program supports:

* setting the bottom, right, left and top border value
* setting the auto_scale property for border
* automatic converting the border size in pixels to corresponding display_border expressed in density independent pixels (dp), to make sure your widget scales well with the different screen sizes, DPI and resolutions
* option to scale the border to via scale property, so you can resize the border to acomodate to small size widget
* option to scale thw widget size so you can see how your widget with needed width/height will look like
* ability to show the area to be stretched (just tick the fill stretch area checkbox)
* display of the borders placement in the widget coordinates
* selected image preview with resolution information + widget size information
* **HUGE!** automatic KV Language generation for your custom widget with ability to easily copy it and use in your program

Application is young and may be extended in the future with better UI and more solid I/O, however you should "take it as it is". I think its a nice utility when you must create nice, custom shape widget and you find Kivy BorderImage docs too weak in that area. Manual testing of the code turn-by-turn is not so easy, so why not to use magic of Kivy and be able to see your progress live and working? :)

Application is written upon **Kivy 1.9.2** and requires that version. I am not sure if it will run under 1.9.1 (stable), but it may after removing the *kivy.require()* line.

App idea based on [border-image.com](http://www.border-image.com/) website. Thanks!

Thanks to the Kivy Organization for awesome Kivy framework and Kivy community for help. Special thanks to **@dessant** and **@tshirtman** for help understanding the Kivy BorderImage.
