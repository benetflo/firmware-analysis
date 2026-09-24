from rich.console import Console
from rich import inspect
from rich.panel import Panel
from rich.table import Table
from rich import box

#console.print("Hello", style="bold red")


class UI:

    def __init__(self):

        self.console = Console()

    def show_main_info():
        table = Table(show_header=False)

        table.add_row("")

    def show_info(self, file, architecture, file_size, file_type, endian):

        table = Table(show_header=False)
        table.add_row("Architecture", architecture)
        table.add_row("File size", file_size)
        table.add_row("File type", file_type)
        table.add_row("Endian", endian)

        self.console.print(
            Panel(
                table,
                title=f"Analysis of {file}",
                title_align="center",
                border_style="cyan",
                box=box.ROUNDED,
                padding=(1, 2),
                )
        )

    
