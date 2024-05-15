import pytest
import os
def merge_and_write(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1:
            data1 = file1.read().strip()

        with open(file2_path, 'r') as file2:
            data2 = file2.read().strip()

        merged_data = data1 + ' ' + data2

        with open(output_file_path, 'w') as output_file:
            output_file.write(merged_data)

        with open(output_file_path, 'r') as output_file:
            data = output_file.read()
        return data
    except FileNotFoundError:
        return "Один из файлов не найден"

@pytest.fixture
def failiki(tmp_path):
    f1 = tmp_path / "f1.txt"
    f2 = tmp_path / "f2.txt"
    f1.write_text("texttttt f1")
    f2.write_text("texttttt f2")
    output_file = tmp_path / "out.txt"
    return f1, f2, output_file
def tst_merge_and_write(failiki):
    f1, f2, output_file = failiki
    result = merge_and_write(str(f1), str(f2), str(output_file))
    want = "texttttt f1 texttttt f2"
    assert result == want
    assert output_file.read_text() == want

def testNotfound(failiki):
    _, _, output_file = failiki
    notFile = "notfile.txt"
    result = merge_and_write(notFile, notFile, str(output_file))

    assert result == "Один из файлов не найден"