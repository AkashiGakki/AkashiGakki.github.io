class AbsDouble {
    public static double abs(double x) {
        if (x < 0) {
            return -x;
        } else {
            return x;
        }
    }

    public static void main(String[] args) {
        double x = -2.3;
        System.out.println(abs(x));
    }
}