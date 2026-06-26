# Formats the final output.


def format_markdown(output: dict) -> str:
    """Convert the output dictionary into a formatted Markdown string."""

    md = f"# Summary of {output['metadata']['name']}\n"
    md += f"**Mode:** {output['mode']}\n\n"
    md += f"**Steps:** {', '.join(output['steps'])}\n\n"
    md += output["summary"]
    return md
