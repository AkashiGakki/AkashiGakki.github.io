class Reverse {
    public static double[] rev(double[] list) {
        int N = list.length;
        for (int i = 0; i < N / 2; i++) {
            double temp = list[i];
            list[i] = list[N-1-i];
            list[N-1-i] = temp;
        }
        return list;
    }

    public static void main(String[] args) {
        double[] list = new double[] {1, 2, 3, 4, 5, 6, 7};
        double[] rev_list = rev(list);
        for (int i = 0; i < rev_list.length; i++) {
            System.out.println(rev_list[i]);
        }
    }
}