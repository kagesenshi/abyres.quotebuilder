import abyres.quotebuilder 
from abyres.quotebuilder.app import App
import morepath
import more.static
import os
from werkzeug.debug import DebuggedApplication

def run():
    config = morepath.setup()
    config.scan(package=abyres.quotebuilder)
    config.scan(package=more.static)
    config.scan(package=more.chameleon)
    config.commit()
    app = App()
    morepath.run(DebuggedApplication(app), port=9876)

if __name__ == '__main__':
    main()

