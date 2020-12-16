from enum import Enum
import typer


class Notation(str, Enum):
    infix = "infix"
    rpn = "rpn"


app = typer.Typer()
notationOption = typer.Option(Notation.infix, "--notation", "-n", help="calculation notation can be: infix or rpc. default is infix")
baseOption = typer.Option(10, "--base", "-b", help="base for the compute")


@app.command()
def compute(calculation: str,
            notation: Notation = notationOption,
            base: int = baseOption):
    typer.echo(f"Selected Notation: {notation}")
    typer.echo(f"Selected Base: {base}")
    typer.echo(f"Calculation: {calculation}")
    raise Exception()


if __name__ == "__main__":
    app()
