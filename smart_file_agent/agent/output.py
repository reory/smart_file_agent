# Formats the final output.

def format_markdown(output: dict) -> str:
    md = f"# Summary of {output['metadata']['name']}\n"
    md += f"**Mode:** {output['mode']}\n\n"
    md += f"**Steps:** {', '.join(output['steps'])}\n\n"
    md += output["summary"]
    return md