import click
import time
import multiprocessing
import signal
import sys
from app.track import track_app_usage

# Quanta CLI tool to track app usage
@click.group()
def cli():
    pass

# Track the usage of an application by its name.
@cli.command()
@click.option('--app', default=None, help='Name of the application to track usage')
def track(app):
    click.echo(f'Starting to track usage for {app}...')
    
    # Run the app tracking in a background process
    process = multiprocessing.Process(target=track_app_usage, args=(app,))
    process.daemon = True  # Run as a daemon process
    process.start()

    # Handle shutdown signals to cleanly exit
    def handle_shutdown(signal_received, frame):
        click.echo("Shutting down tracking...")
        process.terminate()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, handle_shutdown)  # Ctrl+C
    signal.signal(signal.SIGTERM, handle_shutdown) # Handle system termination

    # Keep the main process alive indefinitely
    while True:
        time.sleep(60)  # Sleep the main process, while the background runs

    
if __name__ == '__main__':
    cli()