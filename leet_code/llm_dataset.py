from datasets import load_dataset

# Load the Alpaca cleaned dataset
# ds = load_dataset("yahma/alpaca-cleaned")
# print(ds)

# Save the train split to JSON
# ds["train"].to_json("C:\\Users\\LENOVO\\Desktop\\alpaca_cleaned.json")

from datasets import load_dataset

ds = load_dataset("tatsu-lab/alpaca")


# Save the train split to JSON

# ds["train"].to_json("C:\\Users\\LENOVO\\Desktop\\alpaca.json")


# from datasets import load_dataset
# ds = load_dataset("wikitext", "wikitext-2-raw-v1")

# # Save the train split to JSON

# ds["train"].to_json("C:\\Users\\LENOVO\\Desktop\\wikitext2.json")



# ds = load_dataset("openwebtext")
# # Save the train split to JSON

# ds["train"].to_json("C:\\Users\\LENOVO\\Desktop\\openwebtext.json")



# import fitz  # PyMuPDF

# pdf_path = r"D:\kau_farming.pdf"
# txt_path = r"D:\kau_farming_raw.txt"

# doc = fitz.open(pdf_path)

# with open(txt_path, "w", encoding="utf-8") as f:
#     for page in doc:
#         text = page.get_text()
#         if text:
#             f.write(text + "\n")

# print("Text extraction completed")



import re

input_path = "D:\\n-gram\\kau_farming_raw.txt"
output_path = "D:\\n-gram\\kau_farming_clean.txt"

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

# Remove page numbers
text = re.sub(r"\n\d+\n", "\n", text)

# Remove multiple newlines
text = re.sub(r"\n{2,}", "\n", text)

# Remove special bullets
text = re.sub(r"[•●▪►]", "", text)

# Normalize spacing
text = re.sub(r"\s+", " ", text)

# Lowercase (recommended for n-gram)
text = text.lower()

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Clean text ready for n-gram model")
