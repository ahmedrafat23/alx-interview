def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Start each row with a 1
        new_row = [1]
        # Calculate the in-between values using previous row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        # End each row with a 1
        new_row.append(1)
        triangle.append(new_row)

    return triangle

