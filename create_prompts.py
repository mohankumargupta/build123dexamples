import sys
from pathlib import Path

subfolder="llm_build123d_to_fusion360"
prompt1_template = "from_build123d_to_fusion360.txt"
prompt2_template = "prompt2.txt"

if __name__ == "__main__":
    filename = sys.argv[1]
    subfolder_path = Path(subfolder)
    prompt1_template_path = subfolder_path / prompt1_template
    prompt2_template_path = subfolder_path / prompt2_template

    file_path = subfolder_path / "input_build123d" / filename
    stem =file_path.stem
    suffix_part1 = f'{stem}-prompt_part1.txt'
    suffix_part2 = f'{stem}-prompt_part2.txt'
    prompt_part1 = subfolder_path / suffix_part1
    prompt_part2 = subfolder_path / suffix_part2

    with open(file_path, 'r') as f:
        code = f.read()

    with open(prompt1_template_path, 'r') as f:
        prompt = f.read()

    total_prompt = prompt + code
    print(total_prompt)

    with open(prompt_part1, 'w') as f:
        f.write(total_prompt)

    




