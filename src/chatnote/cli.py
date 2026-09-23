"""CLI entrypoint for chatnote."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatnote import __version__


@click.group(name="chatnote", invoke_without_command=True, no_args_is_help=True)
@click.version_option(__version__, prog_name="chatnote")
@add_tree_option(renderer_options={"root_name": "chatnote"})
def main() -> None:
    """chatnote command line interface."""
    # Add package-specific commands here. Prefer ChatStyle helpers for
    # interactive input when a command needs recoverable user input.
    pass


if __name__ == "__main__":
    main()
