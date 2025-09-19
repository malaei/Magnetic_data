import os

def insert_spacegroup_in_readme(compound_dir):
    readme_file = os.path.join(compound_dir, "README.md")
    sym_file = os.path.join(compound_dir, "sym.txt")

    if not (os.path.exists(readme_file) and os.path.exists(sym_file)):
        return  # skip if files missing

    # Read the space group line
    with open(sym_file, "r") as f:
        space_group_line = f.readline().strip()

    # Read README.md
    with open(readme_file, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if "Structure" in line:
            # add blank line before space group line
            new_lines.append("\n")
            new_lines.append(f"{space_group_line}\n\n")

    # Write back to README.md
    with open(readme_file, "w") as f:
        f.writelines(new_lines)

def process_all_compounds(root_dir="."):
    for entry in os.listdir(root_dir):
        compound_dir = os.path.join(root_dir, entry)
        if os.path.isdir(compound_dir):
            insert_spacegroup_in_readme(compound_dir)

if __name__ == "__main__":
    process_all_compounds(".")

