from rqt_gui_py.plugin import Plugin
from .spatz_display_widget import DisplayWidget


class Display(Plugin):

    def __init__(self, context):
        super(Plugin, self).__init__(context)
        self.setObjectName("SpatzDisplay")
        self._widget = DisplayWidget()
        context.add_widget(self._widget)
