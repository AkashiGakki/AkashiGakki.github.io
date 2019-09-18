class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        String str = strs[0];
        for (int i = 0; i < strs.length; i++) {
            while (strs[i].indexOf(str) != 0) {
                str = str.substring(0, str.length()-1);
                if (str.isEmpty()) {
                    return "";
                }
            }
        }
        return str;
    }

    public static void main(String[] args) {
        String[] strs = new String[] {"flower","flow","flight"};
        Solution pre = new Solution();
        System.out.println(pre.longestCommonPrefix(strs));

    }
}