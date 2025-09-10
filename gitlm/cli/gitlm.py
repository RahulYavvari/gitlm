import click

from gitlm.cli.commands import commitmsg as _commitmsg
from gitlm.cli.commands import suggest as _suggest
from gitlm.cli.commands import explain as _explain

from gitlm.utils import config

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f"GitLM, version {config.__VERSION__}")
    ctx.exit()

@click.group()
@click.option(
    "--version",
    "-v",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Show the version and exit."
)
def main():
    pass

@main.command(name="commitmsg", help="Generates acommit message")
def commitmsg():
    _commitmsg.commitmsg()

@main.command(name="suggest", help="Suggests the next command")
def suggest():
    _suggest.suggest()

@main.command(name="explain", help="Explains a git command")
@click.option("--cmd", "-c", required=True)
def explain(cmd):
    _explain.explain(cmd)   