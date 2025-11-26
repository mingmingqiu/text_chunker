# I use sentence level chunks without overlapping between chunks for the following reasons:
#   - since this task is for TTS, not RAF, thus, no need to have overlapping chunks to improve context understanding.
#   - sentence level chunks are more natural for TTS synthesis.
#   - non-overlapping chunks reduce the total number of chunks, thus reducing the cost of using LLMs for processing.
# Furthermore, I have not used LangChain's built-in text splitter because:
#   - LangChain is overkill for simple chunking.
#   - Sentence-level splitting + cleaning is perfect for TTS.
#   - No overlap is desirable (overlapping breaks TTS flow).

import re
import textwrap

MAX_LEN = 200

def clean_text(t):
    # remove redundant characters for TTS:
    # - Excess whitespace
    # - Multiple newlines
    # - Strange dashes replaced with normal punctuation
    t = t.replace("—", "-")
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def chunk_text(t, max_len=200):
    chunks = []
    current = ""

    # split primarily by sentence boundaries but keep punctuation
    sentences = re.split(r'([.!?])', t)
    # recombine to restore punctuation
    trailing = [sentences[-1]] if len(sentences) % 2 != 0 else []
    sentences = ["".join(i) for i in zip(sentences[0::2], sentences[1::2])] + trailing

    for s in sentences:
        s = s.strip()
        if not s:
            continue

        if len(s)<=max_len:
            if len(current) + len(s) + 1 <= max_len:
                current += " " + s if current else s
            else:
                if current:
                    chunks.append(current)
                current = s
        else:
            # sentence longer than max_len, need to further split
            sub_sentences = textwrap.wrap(s, width=max_len)
            for sub_s in sub_sentences:
                sub_s = sub_s.strip()
                if len(current) + len(sub_s) + 1 <= max_len:
                    current += " " + sub_s if current else sub_s
                else:
                    if current:
                        chunks.append(current)
                    current = sub_s


    if current:
        chunks.append(current)

    return chunks

def process(text):
    cleaned = clean_text(text)
    chunks = chunk_text(cleaned, MAX_LEN)
    return cleaned, chunks


text1 = """Apples are one of the most widely cultivated and consumed fruits in the world. Known for their crisp texture, sweet-tart flavor, and impressive versatility,
apples have a long and fascinating history that spans cultures, continents, and centuries. Botanically classified as Malus domestica, apples belong to the Rosaceae family, which also includes pears, cherries, and roses.

The domestic apple traces its ancestry to the wild apple species Malus sieversii, native to the mountains of Central Asia—particularly in what is now Kazakhstan. Ancient traders along the Silk Road helped spread apples westward to Europe and eastward to China. Over time, through both natural cross-pollination and human intervention, the apple evolved into the diverse array of cultivars we enjoy today.

Apples were highly prized by ancient civilizations. The Greeks and Romans cultivated them extensively, and they became symbolic in many myths and traditions. In Norse mythology, apples were believed to grant eternal youth. In the biblical tradition, the apple became associated—though possibly inaccurately—with the fruit of the Tree of Knowledge."""

text2 = """when the sun rises over the distant hills and the birds begin to sing their morning songs while the dew still clings to the grass and the breeze carries the scent of blooming flowers through the quiet streets where people slowly start to stir from their sleep and the world gently shifts from night to day with a sense of calm that is fleeting yet beautiful and everything feels suspended in a moment of possibility before the rush of time resumes its usual pace and the responsibilities of life return to fill the hours with motion sound and urgency until the sun once again sinks below the horizon and darkness wraps the earth in stillness once more """

cleaned1, chunks1 = process(text1)
cleaned2, chunks2 = process(text2)

save_path = "results_.md"
with open(save_path, "w") as f:
    f.write("# Outputs\n\n")
    f.write("## Text 1 Cleaned\n\n")
    f.write(cleaned1 + "\n\n")
    f.write("## Text 1 Chunks (≤200 chars each)\n")
    for i, chunk in enumerate(chunks1):
        f.write(str(i+1)+". " + chunk + "\n")
    f.write("\n")

    f.write("## Text 2 Cleaned\n\n")
    f.write(cleaned2 + "\n\n")
    f.write("## Text 2 Chunks (≤200 chars each)\n")
    for i, chunk in enumerate(chunks2):
        f.write(str(i+1)+". " + chunk + "\n")