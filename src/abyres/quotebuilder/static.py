import bowerstatic
import os
from abyres.quotebuilder.app import App

bower = bowerstatic.Bower()
components = bower.components('++bower_static', os.path.join(
                                os.path.dirname(__file__),
                                'bower_components'))

local_components = bower.local_components('++quotebuilder_static', components)
local_components.component(os.path.join(os.path.dirname(__file__),
                            'static'), version=None)

@App.static_components()
def get_static_components():
    return local_components

