class Max {

    public static double max(double[] list) {
        double max = list[0];
        for (int i = 0; i < list.length; i++) {
            if (list[i] > max) {
                max = list[i];
            }
        }
        return max;
    }

    public static void main(String[] args) {
        double[] list = new double[] {1.2, 3.0, 5, 0.4, 9, 6.8, 7};
        System.out.println(max(list));
    }
}