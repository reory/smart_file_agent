#  Implements the actual actions the agent can perform.
import logging
import re
from collections import Counter

logger = logging.getLogger(__name__)

def summarise_text(text: str) -> str:
    """Heuristic NLP Summariser that dynamically extracts the core meaning."""

    logger.info("Running upgraded summarise_text tool")
    
    if not text.strip():
        return "Summary:\n- The file is empty."

    # Remove fenced markdown code blocks
    text = re.sub(
        r"```.*?```",
        " ",
        text,
        flags=re.DOTALL,
    )

    # Remove remaining markdown fence markers
    text= text.replace("```", " ")

    # Remove markdown headings
    text = re.sub(
        r"^#+\s*",
        "",
        text,
        flags=re.MULTILINE,
    )

    # Remove markdown links but keep the visible text
    text = re.sub(
        r"\[([^\]]+)\]\([^)]+\)",
        r"\1",
        text,
    )

    # Remove markdown task list markers
    text = re.sub(
        r"\[[ xX]\]",
        " ",
        text,
    )

    # Remove image markers
    text = re.sub(
        r"!\[[^\]]*\]",
        " ",
        text,
    )

    # Remove common horizontal rules
    text = text.replace("---", " ")

    # Split into sentences intelligently (handles periods, question marks, and newlines)
    # This keeps messy structural trees from being treated as one giant sentence
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+|\n+', text) if s.strip()]

    # Filter out weak README-style fragments
    filtered_sentences = []

    for sentence in sentences:

        if len(sentence.split()) < 8:
            continue

        if sentence.startswith("!"):
            continue

        if sentence.startswith("["):
            continue

        filtered_sentences.append(sentence)

    sentences = filtered_sentences
    
    # Tokenise words and strip out common English filler words (stopwords)
    words = [w.strip(".,!?()-\"'\n").lower() for w in text.split()]
    stopwords = {
        'the', 'is', 'and', 'a', 'to', 'in', 'of', 'for', 'this', 'that', 
        'with', 'on', 'as', 'an', 'it', 'its', 'by', 'are', 'from', 'your',
        'how', 'file', 'project',
    }
    meaningful_words = [w for w in words if w and w not in stopwords and len(w) > 2]
    
    # Calculate word frequencies to see what the file is actually talking about
    word_frequencies = Counter(meaningful_words)
    
    # Extract top 5 keywords dynamically
    top_keywords = [word for word, count in word_frequencies.most_common(5)]
    
    # Score each sentence based on how many important keywords it contains
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = [w.strip(".,!?").lower() for w in sentence.split()]
        score = sum(word_frequencies[w] for w in sentence_words if w in word_frequencies)
        
        # Normalise by length so long bullet point walls don't accidentally win out
        sentence_scores[sentence] = score / (len(sentence_words) + 1)
        
    # Extract the top scoring sentences
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    
    # Prefer the first substantial sentence in the document
    opening_idea = "No summary sentence found."

    for sentence in sentences:
        if len(sentence.split()) >= 8:
            opening_idea = sentence
            break

    # Use scoring for the supporting detail
    key_detail = (
        sorted_sentences[0]
        if len(sorted_sentences) > 0
        else opening_idea
    )

    # Avoid duplication
    if key_detail == opening_idea and len(sorted_sentences) > 1:
        key_detail = sorted_sentences[1]
    

    # Format and clean up output
    summary = (
        "Summary:\n"
        f"- Opening idea: {opening_idea}\n"
        f"- Key detail: {key_detail}\n"
        f"- Keywords: {', '.join(top_keywords)}\n"
    )
    return summary.strip()


def extract_keywords(text: str, limit: int = 10) -> list[str]:
    """Extract meaningful keywords from text."""

    stopwords = {"the", "and", "for", "with", "this", "a", "in",
                "that","from","into","are","was", "is", "to", "of",
                "how", "file", "project",
    }

    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())

    words = [w for w in words if w not in stopwords]

    return [word for word, _ in Counter(words).most_common(limit)]



def bulletify(text: str) -> str:
    """Converts sentences into uniform bullet points."""

    raw_chunks = re.split(r'\n|\.\s+', text)

    bullets = []
    for chunk in raw_chunks:
        cleaned = chunk.strip()

        # Skip empty lines or the top-level title line
        if not cleaned or cleaned.lower().startswith("summary"):
            continue

        cleaned = re.sub(r'^[-\*\u2022]\s*', '', cleaned)
        cleaned = re.sub(r'^(Opening idea|Key detail|Keywords):\s*', '', cleaned, flags=re.IGNORECASE)

        if cleaned:
            
            # Ensure the bullet starts capitalised
            formatted_line = cleaned[0].upper() + cleaned[1:]
            bullets.append(f"- {formatted_line}")
            
    return "\n".join(bullets)
