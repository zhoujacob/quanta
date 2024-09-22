import click
from app.track import is_app_running

# Quanta CLI tool to track app usage
@click.group()
def cli():
    pass

# default should be how long the OS has been active for in the day
@cli.command()
@click.option('--app', default=None, help='Name of the application to track usage')
def track(app):
    """Track the usage of an application by its name."""
    click.echo(f'Tracking usage for {app}')
    is_app_running(app)
    
if __name__ == '__main__':
    cli()