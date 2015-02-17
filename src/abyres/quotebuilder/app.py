import morepath
import os
from more.static import StaticApp
from more.chameleon import ChameleonApp

class App(StaticApp, ChameleonApp):

    def __str__(self):
        return u'QuoteBuilder Service'

    def static_path(self):
        return os.path.join(os.path.dirname(__file__), 'static')

@App.setting_section(section='chameleon')
def get_setting_section():
    return {
        'auto_reload': True
    }

class StaticUrl(object):

    def __init__(self, request):
        self.components = request.app.bower_components

    def __call__(self, component):
        return self.components.get_component(component).url()

@App.template_directory()
def get_template_directory():
    return 'templates'

@App.path(path='')
class Root(object):
    pass

@App.html(
    model=Root,
    template='index.pt'
)
def frontpage(self, request):
    request.include('jquery')
    request.include('Materialize')
    request.include('abyres.quotebuilder')
    templates = request.app.registry._template_loaders.get('.pt')
    master_macro = templates['main_template.pt'].macros['master']
    return {
        'static_url': StaticUrl(request),
        'master_macro': master_macro
    }

