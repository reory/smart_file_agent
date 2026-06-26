#  Implements the actual actions the agent can perform.
import re
from collections import Counter
import logging

logger = logging.getLogger(__name__)

def summarise_text(text: str) -> str:
    """Heuristic NLP Summariser that dynamically extracts the core meaning."""

    logger.info("Running upgraded summarise_text tool")
    
    if not text.strip():
        return "Summary:\n- The file is empty."

    # Split into sentences intelligently (handles periods, question marks, and newlines)
    # This keeps messy structural trees from being treated as one giant sentence
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+|\n+', text) if s.strip()]
    
    # Tokenize words and strip out common English filler words (stopwords)
    words = [w.strip(".,!?()-\"'\n").lower() for w in text.split()]
    stopwords = {
        'the', 'is', 'and', 'a', 'to', 'in', 'of', 'for', 'this', 'that', 
        'with', 'on', 'as', 'an', 'it', 'its', 'by', 'are', 'from', 'your'
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
        
        # Normalize by length so long bullet point walls don't accidentally win out
        sentence_scores[sentence] = score / (len(sentence_words) + 1)
        
    # Extract the top scoring sentences
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    
    # Fallback safety checks
    opening_idea = sorted_sentences[0] if len(sorted_sentences) > 0 else "No summary sentence found."
    key_detail = sorted_sentences[1] if len(sorted_sentences) > 1 else opening_idea

    # Format and clean up output
    summary = (
        "Summary:\n"
        f"- Opening idea: {opening_idea}\n"
        f"- Key detail: {key_detail}\n"
        f"- Keywords: {', '.join(top_keywords)}\n"
    )
    return summary.strip()


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
