class MatrixMult {
    public static double[][] multip(double[][] array1, double[][] array2) {
        int N = array1.length;
        double[][] matrix = new double[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    matrix[i][j] += array1[i][k] * array2[k][j];
                }
            }
        }
        return matrix;
    }

    public static void main(String[] args) {
        double[][] array1 = new double[][] {
            {1, 2, 3}, {3, 2, 1}
        };
        double[][] array2 = new double[][] {
            {1, 2, 3}, {3, 2, 1}
        };
        double[][] matrix = multip(array1, array2);
        int M = array1.length;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                System.out.println(matrix[i][j]);
            }
        }
    }
}