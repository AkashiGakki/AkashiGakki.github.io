class Sqrt {
    public static double sqrt(double x) {
        if (x < 0) {
            return Double.NaN;
        }
        double err = 1e-15;
        double t = x;
        while(Math.abs(t - x / t) > err * t) {
            t = (x / t + t) / 2.0;
        }
        return t;
    }

    public static void main(String[] args) {
        double x = 9;
        System.out.println(sqrt(x));
    }
}