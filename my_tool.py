import click

# We have a group of commands
@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("Hello World")