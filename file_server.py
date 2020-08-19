import os
import click
from app import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    app.config['SQLALCHEMY_ECHO'] = True
    return dict()

@app.cli.command()
@click.option('--length',
              default=25,
              help='Number of functions to include in the profiler report.')
@click.option('--profile-dir',
              default=None,
              help='Directory where profiler data files are saved.')
def profile(length, profile_dir):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app,
                                      restrictions=[length],
                                      profile_dir=profile_dir)
    app.run()


@app.cli.command()
def deploy():
    pass
