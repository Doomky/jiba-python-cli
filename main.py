from enum import Enum
from typing import List
from command_context import CommandContext
import typer

from tokens import TokenParser, RpnTransformer, RpnCalculator


class Notation(str, Enum):
    infix = "infix"
    rpn = "rpn"


app = typer.Typer()
notationOption: Notation = typer.Option(Notation.infix, "--notation", "-n", help="Calculation notation")
baseOption: int = typer.Option(10, "--base", "-b", help="Base for the calculation", min=2)


@app.command()
def compute(calculation: List[str],
            notation: Notation = notationOption,
            base: int = baseOption):
    typer.echo(f"Selected Notation: {notation}")
    typer.echo(f"Selected Base: {base}")
    typer.echo(f"Calculation(s): {calculation}")
    if base != CommandContext.Base:
        CommandContext.Base = base
    CommandContext.IsInfix = (notation == Notation.infix)

    for calc in calculation:
        token_list = TokenParser(calc).parse()
        token_stack = RpnTransformer(token_list).transform()
        number = RpnCalculator(token_stack).compute()
        typer.echo(f"Result: {number}")


if __name__ == "__main__":
    app()
