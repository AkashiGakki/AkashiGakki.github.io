class Avg {
    public static double avg(double[] list) {
        int N = list.length;
        double sum = 0;
        for (int i = 0; i < N; i++) {
            sum += list[i];
        }
        double average = sum / N;
        return average;
    }

    public static void main(String[] args) {
        double[] list = new double[] {1, 2, 3, 4, 5, 6, 7, 8, 9};
        double avg = avg(list);
        System.out.println(avg);
    }
}