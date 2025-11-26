## 1. Codes
The complete codes are shown in `main.py`

## 2. Outputs

### Text 1 Cleaned

Apples are one of the most widely cultivated and consumed fruits in the world. Known for their crisp texture, sweet-tart flavor, and impressive versatility, apples have a long and fascinating history that spans cultures, continents, and centuries. Botanically classified as Malus domestica, apples belong to the Rosaceae family, which also includes pears, cherries, and roses. The domestic apple traces its ancestry to the wild apple species Malus sieversii, native to the mountains of Central Asia-particularly in what is now Kazakhstan. Ancient traders along the Silk Road helped spread apples westward to Europe and eastward to China. Over time, through both natural cross-pollination and human intervention, the apple evolved into the diverse array of cultivars we enjoy today. Apples were highly prized by ancient civilizations. The Greeks and Romans cultivated them extensively, and they became symbolic in many myths and traditions. In Norse mythology, apples were believed to grant eternal youth. In the biblical tradition, the apple became associated-though possibly inaccurately-with the fruit of the Tree of Knowledge.

### Text 1 Chunks (≤200 chars each)
1. Apples are one of the most widely cultivated and consumed fruits in the world.
2. Known for their crisp texture, sweet-tart flavor, and impressive versatility, apples have a long and fascinating history that spans cultures, continents, and centuries.
3. Botanically classified as Malus domestica, apples belong to the Rosaceae family, which also includes pears, cherries, and roses.
4. The domestic apple traces its ancestry to the wild apple species Malus sieversii, native to the mountains of Central Asia-particularly in what is now Kazakhstan.
5. Ancient traders along the Silk Road helped spread apples westward to Europe and eastward to China.
6. Over time, through both natural cross-pollination and human intervention, the apple evolved into the diverse array of cultivars we enjoy today. Apples were highly prized by ancient civilizations.
7. The Greeks and Romans cultivated them extensively, and they became symbolic in many myths and traditions. In Norse mythology, apples were believed to grant eternal youth.
8. In the biblical tradition, the apple became associated-though possibly inaccurately-with the fruit of the Tree of Knowledge.

### Text 2 Cleaned

when the sun rises over the distant hills and the birds begin to sing their morning songs while the dew still clings to the grass and the breeze carries the scent of blooming flowers through the quiet streets where people slowly start to stir from their sleep and the world gently shifts from night to day with a sense of calm that is fleeting yet beautiful and everything feels suspended in a moment of possibility before the rush of time resumes its usual pace and the responsibilities of life return to fill the hours with motion sound and urgency until the sun once again sinks below the horizon and darkness wraps the earth in stillness once more

### Text 2 Chunks (≤200 chars each)
1. when the sun rises over the distant hills and the birds begin to sing their morning songs while the dew still clings to the grass and the breeze carries the scent of blooming flowers through the quiet
2. streets where people slowly start to stir from their sleep and the world gently shifts from night to day with a sense of calm that is fleeting yet beautiful and everything feels suspended in a moment
3. of possibility before the rush of time resumes its usual pace and the responsibilities of life return to fill the hours with motion sound and urgency until the sun once again sinks below the horizon
4. and darkness wraps the earth in stillness once more


## 3. Reasoning & Explanation
### How boundaries were chosen

- Primary rule: Break on sentence ends (. ! ?) when available → keeps natural TTS rhythm.
- When sentence too long (as in text2):
    - Use textwrap.wrap to break at natural spaces under 200 chars.
    - Ensures that TTS pauses at phrase-like points rather than mid-word.


### What redundant characters were removed

| Removed/normalized             | Reason                                      |
| ------------------------------ | ------------------------------------------- |
| Multiple spaces → single space | Prevents awkward long pauses                |
| Newlines → single space        | TTS handles continuous text better          |
| Em-dashes (—) → hyphen (-)     | TTS often over-pauses on em-dash characters |
| Trailing/leading whitespace    | Clean formatting                            |
| Excess punctuation sequences   | Avoids unnatural inflection                 |

### How these changes improve TTS

- Cleaner text means more predictable prosody.
- Sentence-based chunks allow TTS to insert natural pauses.
- Removing awkward unicode characters avoids glitchy pauses or mispronunciations.
- Chunks <200 characters ensure good breath/pacing units for TTS engines.

## 4. Considerations for Other Languages

To generalize this process to non-English languages, you would need to consider:

1. Different sentence boundary rules
- Chinese/Japanese do not use spaces; segmentation must use NLP tokenizers.
- Spanish uses inverted punctuation (¿ ¡).
- German often forms extremely long compound words — chunking must consider syllables carefully.

2. Word segmentation
- Thai has no spaces between words → requires a word-segmentation model.
- Chinese uses 。 ！ ？ instead of . ! ?

3. Prosody differences
- Some languages expect pauses after commas; others do not.
- Tonal languages (Chinese, Vietnamese) must avoid splitting in ways that mislead tone grouping.

4. Script normalization
- Some languages need Unicode normalization (NFC/NFKC).
- Right-to-left languages (Arabic, Hebrew) need careful handling to avoid breaking ligatures.

5. Diacritics
- Removing diacritics is usually not acceptable, since they change meaning.