from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.fileutil import copy_asset
import os

class RapiDocDirective(Directive):
    has_content = False
    option_spec = {
        'spec-url': str,
        'theme': str,
        'render-style': str,
    }

    def run(self):
        spec_url = self.options.get('spec-url', '')
        theme = self.options.get('theme', 'light')
        render_style = self.options.get('render-style', 'read')

        # Generate HTML node
        html = (
            f'<rapi-doc '
            f'spec-url="{spec_url}" '
            f'theme="{theme}" '
            f'render-style="{render_style}">'
            f'</rapi-doc>'
        )
        return [nodes.raw('', html, format='html')]

def setup(app):
    # Register the directive
    app.add_directive('rapidoc', RapiDocDirective)

    # Add RapiDoc static JS file
    app.connect('builder-inited', lambda app: copy_asset(
        os.path.join(os.path.dirname(__file__), 'static', 'rapidoc.min.js'),
        os.path.join(app.outdir, '_static')
    ))

    # Add RapiDoc JS to the HTML output
    app.add_js_file('rapidoc.min.js')

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
