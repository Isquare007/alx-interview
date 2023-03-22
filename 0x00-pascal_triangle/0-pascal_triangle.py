# returns the list of integers representing the pascal triangle

def pascal_triangle(n):
    if n <= 0:
        return []

    pascal_list = [[1]]

    for i in range(1, n):
        prev_row = pascal_list[-1]
        cur_row = [1]
        for j in range(1, i):
            cur_row.append(prev_row[j-1] + prev_row[j])
        cur_row.append(1)
        pascal_list.append(cur_row)

    return pascal_list
