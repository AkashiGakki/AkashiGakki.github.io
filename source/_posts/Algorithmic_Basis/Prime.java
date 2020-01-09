class Prime {
    // public static boolean isPrime(int n) {
    //     if (n < 2) {
    //         return false;
    //     } else {
    //         for (int i = 2; i * i <= n; i++) {
    //             if (n % i == 0) {
    //                 return false;
    //             } else {
    //                 return true;
    //             }
    //         }
    //     }
    // }

    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int x = 123;
        System.out.println(isPrime(x));
    }
}