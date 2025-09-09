import click

import commands.commitmsg as _commitmsg
import commands.suggest as _suggest
import commands.explain as _explain

@click.group()
def main():
    pass

@main.command(name="commitmsg", help="Generates acommit message")
def commitmsg():
    _commitmsg.commitmsg()

@main.command(name="suggest", help="Suggests the next command")
def suggest():
    _suggest.suggest()

@main.command(name="explain", help="Explains a git command")
def explain():
    _explain.explain()

if __name__=="__main__":
    main.add_command(commitmsg)
    main.add_command(suggest)
    main.add_command(explain)
    main()