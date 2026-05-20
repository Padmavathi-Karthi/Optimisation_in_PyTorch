import nbformat

file_path = "LLM_Architectures.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Remove broken widget metadata safely
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Save cleaned notebook
with open(file_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook cleaned for GitHub rendering")