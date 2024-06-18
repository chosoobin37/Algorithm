import java.util.Scanner;

public class baekjoon_2753 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();  // 사용자가 입력한 연도를 읽음
        sc.close();  // Scanner를 닫음
        System.out.println(checkYear(year));  // 윤년 여부를 판단한 후 결과를 출력
    }

    public static int checkYear(int year) {
        // 윤년 조건: 연도가 4로 나누어 떨어지며, 100으로 나누어 떨어지지 않거나 400으로 나누어 떨어지는 경우
        if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
            return 1;  // 윤년인 경우 1을 반환
        } else {
            return 0;  // 윤년이 아닌 경우 0을 반환
        }
    }
}
