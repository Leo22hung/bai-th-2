def find_common_elements(num_list1, num_list2):
    # Tạo một set từ num_list1 để loại bỏ các phần tử trùng lặp
    set_num_list1 = set(num_list1)
    
    # Khởi tạo một list để lưu trữ các phần tử chung
    common_elements = []

    # Duyệt qua các phần tử trong num_list2
    for num in num_list2:
        # Kiểm tra xem phần tử có tồn tại trong set_num_list1 không
        if num in set_num_list1:
            # Nếu tồn tại, thêm vào list common_elements
            common_elements.append(num)

    return common_elements

# Example usage:
num_list1 = [1, 2, 2, 1]
num_list2 =[2, 2]
print("Common elements:", find_common_elements(num_list1, num_list2))
