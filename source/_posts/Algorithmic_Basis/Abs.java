class Abs {
    public static int abs(int x) {
        if (x < 0) {
            return -x;
        } else {
            return x;
        }
    }

    public static void main(String[] args) {
        int x = -2;
        System.out.println(abs(x));
    }
}