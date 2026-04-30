from __future__ import annotations

import subprocess
from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Label, Select, Static
from textual.containers import Horizontal, Vertical, ScrollableContainer

from termio_tui import engine
from termio_tui.config import load_aliases

TERMIO_BIN = engine.TERMIO_BIN


class AddEditScreen(Screen):
    """
    Launches termio add / termio edit in the terminal (via suspend).
    The form is handled by termio's own wizard — we just hand off.
    """

    BINDINGS = [
        Binding("escape", "cancel", "Back"),
    ]

    def __init__(self, alias_name: str | None = None):
        super().__init__()
        self._alias = alias_name

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(id="add-edit-body"):
            if self._alias:
                yield Static(
                    f"\n  [bold]Editing alias:[/bold] [cyan]{self._alias}[/cyan]\n\n"
                    f"  This will open the termio edit wizard in your terminal.\n",
                    id="info"
                )
            else:
                yield Static(
                    "\n  [bold]Add new alias[/bold]\n\n"
                    "  This will open the termio add wizard in your terminal.\n",
                    id="info"
                )
            with Horizontal(id="buttons"):
                if self._alias:
                    yield Button("Open Edit Wizard", variant="primary", id="btn-go")
                else:
                    yield Button("Open Add Wizard", variant="primary", id="btn-go")
                yield Button("Cancel", variant="default", id="btn-cancel")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-go":
            args = ["edit", self._alias] if self._alias else ["add"]
            with self.app.suspend():
                subprocess.run([TERMIO_BIN, *args])
            self.dismiss(True)
        elif event.button.id == "btn-cancel":
            self.dismiss(False)

    def action_cancel(self) -> None:
        self.dismiss(False)
