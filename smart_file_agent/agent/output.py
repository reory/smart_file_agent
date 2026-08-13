# Formats the final output.


def format_markdown(output: dict) -> str:
    """Convert the output dictionary into a formatted Markdown string."""

    md = f"# Summary of {output['metadata']['name']}\n"
    md += f"**Mode:** {output['mode']}\n\n"
    md += f"**Steps:** {', '.join(output['steps'])}\n\n"
    md += output["summary"]
    md += "\n\n## Reasoning Trace\n"

    for idx, entry in enumerate(output["trace"], start=1):
        md += f"\n### Step {idx}\n"
        md += f"**Thought:** {entry['thought']}\n\n"
        md += f"**Action:** {entry['action']}\n\n"
        md += f"**Duration:** {entry['duration_ms']} ms\n\n"
        md += f"**Result:**\n{entry['result']}\n"

    return md
