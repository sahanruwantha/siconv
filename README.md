The `siconv` Python package simplifies the conversion between Sinhala and Singlish languages. Whether you're dealing with Sinhala text that needs transformation into Singlish or vice versa, `siconv` offers a user-friendly solution.

**Features:**

- Convert Sinhala text to Singlish
- Convert Singlish text to Sinhala
- Efficient and accurate language conversion algorithms


**Installation:**

Install the package using pip:

```bash
pip install siconv
```

**Usage:**

```python
from siconv import sinhala_to_singlish, singlish_to_sinhala

# Example Usage
sinhala_text = "ආයුබෝවන්"
converted_singlish = sinhala_to_singlish(sinhala_text)
print("Sinhala to Singlish:", converted_singlish)

singlish_text = "ayubowan"
converted_sinhala = singlish_to_sinhala(singlish_text)
print("Singlish to Sinhala:", converted_sinhala)
```

