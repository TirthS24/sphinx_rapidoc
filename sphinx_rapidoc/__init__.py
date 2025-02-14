from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.fileutil import copy_asset
import os

class RapiDocDirective(Directive):
    has_content: bool = False
    option_spec: dict = {
        'spec-url': str,
        'theme': str,
        'render-style': str,
    }

    def run(self) -> list:
        spec_url: str = self.options.get('spec-url', '')
        theme: str = self.options.get('theme', 'dark')
        render_style: str = self.options.get('render-style', 'view')

        # Generate HTML node
        html: str = (
            f'<rapi-doc '
            f'spec-url="{spec_url}" '
            f'theme="{theme}" '
            f'render-style="{render_style}">'
            'primary-color = "#f54c47"'
            'bg-color = "#2e3746"'
            'text-color = "#bacdee"'
            'show-header = "false"'
            f'</rapi-doc>'
        )
        return [nodes.raw('', html, format='html')]

def setup(app) -> dict:
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
