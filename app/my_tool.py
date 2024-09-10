import click

# We have a group of commands
@click.group()
def cli():
    pass

# default should be how long the OS has been active for in the day
@cli.command()
@click.option('--app', default=None, help='Name of the application to track usage')
def track(app):
    """Track the usage of an application by its name."""
    click.echo(f'Tracking {app}')
