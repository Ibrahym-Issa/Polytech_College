import java.util.Locale;
import java.util.Scanner;

public class Task2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);
        double V = -1;

        while (true) {
            System.out.print("Введите объём потребления воды V (>= 0 м³): ");
            if (scanner.hasNextDouble()) {
                V = scanner.nextDouble();
                if (V >= 0) break;
            } else {
                scanner.next();
            }
            System.out.println("Ошибка: объём должен быть неотрицательным числом.");
        }

        double tier1Vol = Math.min(V, 10.0);
        double tier2Vol = (V > 10.0) ? Math.min(V - 10.0, 10.0) : 0.0;
        double tier3Vol = (V > 20.0) ? (V - 20.0) : 0.0;

        double cost1 = tier1Vol * 85.0;
        double cost2 = tier2Vol * 120.0;
        double cost3 = tier3Vol * 175.0;

        double waterCost = cost1 + cost2 + cost3;
        double discount = (V <= 15.0) ? (waterCost * 0.10) : 0.0;
        double subscriptionFee = 600.0;
        double totalBill = (waterCost - discount) + subscriptionFee;
        double effectivePrice = (V > 0) ? ((waterCost - discount) / V) : 0.0;

        System.out.printf(Locale.US, "Диапазон 1 (до 10 м³): %.2f тг%n", cost1);
        System.out.printf(Locale.US, "Диапазон 2 (10–20 м³): %.2f тг%n", cost2);
        System.out.printf(Locale.US, "Диапазон 3 (свыше 20 м³): %.2f тг%n", cost3);
        System.out.printf(Locale.US, "Стоимость воды до скидки: %.2f тг%n", waterCost);
        System.out.printf(Locale.US, "Скидка: %.2f тг%n", discount);
        System.out.printf(Locale.US, "Итоговый счёт (с абонплатой 600 тг): %.2f тг%n", totalBill);
        System.out.printf(Locale.US, "Эффективная цена 1 м³ (без абонплаты): %.2f тг%n", effectivePrice);
    }
}
