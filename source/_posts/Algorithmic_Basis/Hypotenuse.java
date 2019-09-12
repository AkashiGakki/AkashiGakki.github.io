class Hypotenuse {
    public static double hypotense(double a, double b) {
        return Math.sqrt(a * a + b * b);
    }

    public static void main(String[] args) {
        double x = 3;
        double y = 4;
        System.out.println(hypotense(x,y));
    }
}