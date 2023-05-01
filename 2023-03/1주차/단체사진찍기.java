import java.util.Arrays;

class Solution {
    int count = 0;
    String[] data;
    char[] peoples = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    
    public int index(char[] arr, char c) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == c) {
                return i;
            }
        }
        return 0;
    }

    public boolean check(char[] arr) {
        for (String elem : data) {
            char p1 = elem.charAt(0);
            char p2 = elem.charAt(2);
            char operator = elem.charAt(3);
            int wish_distance = (int) (elem.charAt(4) - '0');
            int curr_distance = Math.abs(index(arr, p1) - index(arr, p2)) - 1;
         
            if (operator == '=') {
                if (curr_distance != wish_distance) {
                    return false;
                } 
            } else if (operator == '>') {
                if (curr_distance <= wish_distance) {
                    return false;
                }
            } else if (operator == '<') {
                if (curr_distance >= wish_distance) {
                    return false;
                }
            }
        }
        return true;
    }
    
    // 순서를 지키면서 n 개중에서 r 개를 뽑는 경우
    public void perm(boolean[] visited, char[] output, int depth, int n, int r) {
        if (depth == r) {
            if (check(output)) {
                count++;
            }
            return;
        }
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                output[depth] = peoples[i];
                perm(visited, output, depth + 1, n, r);       
                visited[i] = false;
            }
        }
    }

    public int solution(int n, String[] data) {
        this.data = data;
        int length = peoples.length;
        boolean[] visited = new boolean[length];
        perm(visited, new char[length], 0, length, length);
        return count;
    }
}
