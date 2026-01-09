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



ds = load_dataset("openwebtext")
# Save the train split to JSON
