package kyuSeven;
// Metro.java

// author: awakenedhaki

import java.util.ArrayList;

public class Metro {

    public static int countPassengers(ArrayList<int[]> stops) {
        int inBus = 0;
        for (int i = 0; i <stops.size(); i++) {
            inBus += stops.get(i)[0];
            inBus -= stops.get(i)[1];
        }
        return inBus;
    }
}

