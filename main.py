'''Application used to generate KV code for BorderImages.'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    StringProperty
)
from kivy.clock import mainthread
from plyer import filechooser
import os.path
import threading

__version__ = 1.0


class BorderImageWidget(Widget):
    '''Widget used to help with setup of BorderImage on kivy widgets.'''

    source = StringProperty('data/logo/kivy-icon-512.png')
    '''Source of the image, used as the texture.'''

    auto_scale = BooleanProperty(False)
    '''Indicates if BorderImage should automatically scale when too small.'''

    border = ListProperty([0, 0, 0, 0])
    '''Border of the image taken from source, set by the user.'''

    fill_stretch_area = BooleanProperty(False)
    '''Defines if stretch area should be filled with semitransparent color.'''

class BorderImageTool(BoxLayout):
    '''Main app widget.'''

    KV_STRING = '''
<MyWidget>:
    canvas.before:
        Color:
            rgb: 1, 1, 1
        BorderImage:
            size: self.size
            pos: self.pos
            border: {}
            display_border: {}
            auto_scale: {}
            source: {}
    '''.strip()

    kv_string = StringProperty(KV_STRING)
    '''Code string displayed in the TextInput widget to be copied.'''

    def open_image(self):
        threading.Thread(target=self._open_image).start()

    def _open_image(self):
        images = filechooser.open_file(preview=True, multiple=False)
        if images:
            self._image_opened(images[0])

    @mainthread
    def _image_opened(self, image):
        if image:
            if os.path.exists(image):
                self.ids.bw.source = image

class KivyBorderImageToolApp(App):

    def build(self):
        self.title = 'Kivy BorderImage Tool v.{}'.format(__version__)
        return BorderImageTool()


if __name__ == '__main__':
    KivyBorderImageToolApp().run()
