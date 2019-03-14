package kyuEight;

public class SheepCount {

    public static String sheepCounting(int num) {
        String count = "";
        for (int i = 1; i <= num; i++) {
            count += Integer.toString(i) + " sheep...";
        }
        return count;
    }
}
