"""Command line entry point placeholder for Codex development."""

import click


@click.group()
def main() -> None:
    """HVAC duct pressure automation tool."""


@main.command()
@click.argument("dxf_path")
@click.option("--out", "out_dir", default="output", show_default=True)
def audit(dxf_path: str, out_dir: str) -> None:
    """Audit DXF layers and entity counts. Implement in task 01."""
    raise NotImplementedError("Codex task 01 should implement this command")


if __name__ == "__main__":
    main()
