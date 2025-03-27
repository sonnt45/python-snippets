import base64
import os


def convert(input_path):
    with open(input_path, 'rb') as file:
        base64_str = base64.b64encode(file.read()).decode('utf-8')

    output_path = os.path.splitext(input_path)[0] + '.txt'

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(base64_str)

    return output_path


def main():
    input_file = r'D:\file.xlsx'
    output_file = convert(input_file)
    print(f'Saved to {output_file}')


main()
