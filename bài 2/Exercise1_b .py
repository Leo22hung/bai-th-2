def count_words(file_path):
    # Khởi tạo một từ điển để lưu trữ số lần xuất hiện của mỗi từ
    result = {}

    # Mở file và đọc từng dòng
    with open(file_path, 'r') as file:
        for line in file:
            # Tách các từ trong dòng và chuyển đổi chúng thành chữ thường
            words = line.strip().lower().split()

            # Đếm số lần xuất hiện của mỗi từ trong dòng
            for word in words:
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1

    return result

# Ví dụ sử dụng:
file_path = ["https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko"]
print("Dictionary đếm số lần các từ xuất hiện:", count_words(file_path))

