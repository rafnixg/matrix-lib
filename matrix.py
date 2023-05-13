"""
# Libreria para operaciones con matrices

- Suma
- Multiplicacion
- Transpuesta
- Determinante
- Multiplicacion por escalar
- Multiplicacion punto
- Cofactor
- Forma

"""


class Matrix:
    """Matriz de n x m"""

    def __init__(self, matrix: list[list]):
        self.matrix = matrix

    def shape(self):
        """
        :return: Tupla con el numero de filas y columnas
        """
        return len(self.matrix), len(self.matrix[0])


    def scalar(self, scalar: int):
        """
        Multiplicacion por escalar
        :param scalar: Escalar
        :return: Matriz resultante
        """
        rows, cols = self.shape()
        result = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(self.matrix[i][j] * scalar)
            result.append(row)
        return Matrix(result)

    def dot(self, other: "Matrix"):
        """
        Multiplicacion punto
        :param other: Matriz a multiplicar
        :return: Matriz resultante
        """
        rows, cols = self.shape()
        if self.shape() != other.shape():
            raise ValueError("Las matrices deben tener las mismas dimensiones")
        result = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(self.matrix[i][j] * other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def transpose(self):
        """
        :return: Matriz transpuesta
        """
        rows, cols = self.shape()
        result = []
        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(self.matrix[j][i])
            result.append(row)
        return Matrix(result)

    def __str__(self):
        return str(self.matrix)

    def __len__(self):
        rows, cols = self.shape()
        return rows * cols

    def __add__(self, other: "Matrix"):
        """
        Suma de matrices
        :param other: Matriz a sumar
        :return: Matriz resultante
        """
        if self.shape() != other.shape():
            raise ValueError("Las matrices deben tener las mismas dimensiones")
        rows, cols = self.shape()
        result = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other: "Matrix"):
        """
        Multiplicacion matricial A * B
        :param other: Matriz a multiplicar
        :return: Matriz resultante
        """
        rows, cols = self.shape()
        rows2, cols2 = other.shape()
        if cols != rows2:
            raise ValueError("Las matrices no son multiplicables")
        result = []
        for i in range(rows):
            row = []
            for j in range(cols2):
                total = 0
                for k in range(cols):
                    total += self.matrix[i][k] * other.matrix[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)


if __name__ == "__main__":
    matrix1 = Matrix([[2, -2, 0], [-3, 1, 2], [1, -3, -1]])
    matrix2 = Matrix([[2, -2, 0], [-3, 1, 2], [1, -3, -1]])
    print("matrix1", matrix1)
    print("matrix2", matrix1)
    print("matrix_shape1", matrix1.shape())
    print("matrix_sahpe2", matrix2.shape())
    print(matrix1 + matrix2)
    print(matrix1 * matrix2)
    print(matrix1.transpose())
    print(matrix1.scalar(2))
