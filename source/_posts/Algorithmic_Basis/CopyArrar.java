class CopyArray {
    public static int[] copy(int[] list) {
        int N = list.length;
        int[] list_new = new int[N];
        for (int i = 0; i < N; i++) {
            list_new[i] = list[i];
        }
        return list_new;
    }

    public static void main(String[] args) {
        int[] list1 = new int[] {1, 2, 3, 4, 5, 6, 7};
        int[] list2 = copy(list1);
        for (int i : list2) {
            System.out.println(i);
        }
    }
}