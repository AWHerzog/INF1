
class Matrix:
    def __init__(self, data):
        assert isinstance(data, list) and len(data) > 0, "Matrix must contain at least one non-empty row."
        assert all(isinstance(row, list) for row in data) and len(data[0]) > 0, "Matrix must contain lists with at least one element."

        row_length = len(data[0])
        assert all(len(row) == row_length for row in data), "All rows must have the same length."

        assert all(isinstance(value, (int, float)) for row in data for value in row), "All values must be integers or floats."

        self._data = data

    def __repr__(self):
        return f"Matrix({self._data})"

    def __add__(self, other):
        assert isinstance(other, Matrix), "Can only add another Matrix."
        assert len(self._data) == len(other._data) and len(self._data[0]) == len(other._data[0]), "Matrices must have the same dimensions."

        result_data = [
            [self._data[i][j] + other._data[i][j] for j in range(len(self._data[0]))]
            for i in range(len(self._data))
        ]
        return Matrix(result_data)

    def __mul__(self, other):
        assert isinstance(other, Matrix), "Can only multiply with another Matrix."

        num_rows_a, num_cols_a = len(self._data), len(self._data[0])
        num_rows_b, num_cols_b = len(other._data), len(other._data[0])
        assert num_cols_a == num_rows_b, "Number of columns of A must match number of rows of B."

        result_data = [
            [
                sum(self._data[i][k] * other._data[k][j] for k in range(num_cols_a))
                for j in range(num_cols_b)
            ]
            for i in range(num_rows_a)
        ]
        return Matrix(result_data)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self._data == other._data

    def __hash__(self):
        data_tuple = tuple(tuple(row) for row in self._data)
        return hash(data_tuple)