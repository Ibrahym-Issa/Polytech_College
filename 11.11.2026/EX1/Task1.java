import java.util.Locale;
import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);

        double P = readDouble(scanner, "Введите сумму кредита P (> 0): ", 0.000001, Double.MAX_VALUE, false);
        double R = readDouble(scanner, "Введите годовую ставку R (0..100%): ", 0, 100, true);
        int N = readInt(scanner, "Введите срок N (1..360 мес.): ", 1, 360);
        double E = readDouble(scanner, "Введите дополнительный платёж E (>= 0): ", 0, Double.MAX_VALUE, true);

        double r = R / 1200.0;
        double A = (r > 0) ? (P * r / (1.0 - Math.pow(1.0 + r, -N))) : (P / N);

        // Расчёт без досрочного погашения (для сравнения)
        double balanceNoExtra = P;
        double totalInterestNoExtra = 0.0;
        for (int m = 1; m <= N; m++) {
            double interest = balanceNoExtra * r;
            totalInterestNoExtra += interest;
            double principal = A - interest;
            balanceNoExtra -= principal;
            if (balanceNoExtra < 0) balanceNoExtra = 0;
        }

        // Расчёт с досрочным погашением
        double balance = P;
        double totalInterest = 0.0;
        double lastPayment = 0.0;
        int actualMonths = 0;

        while (balance > 1e-9) {
            actualMonths++;
            double interest = balance * r;
            totalInterest += interest;
            double due = balance + interest;
            double payment = A + E;

            if (payment >= due) {
                lastPayment = due;
                balance = 0.0;
            } else {
                lastPayment = payment;
                balance = due - payment;
            }
        }

        int savedMonths = N - actualMonths;
        double savedInterest = totalInterestNoExtra - totalInterest;

        System.out.printf(Locale.US, "Платёж без доплаты: %.2f%n", A);
        System.out.printf(Locale.US, "Фактический срок: %d мес.%n", actualMonths);
        System.out.printf(Locale.US, "Всего процентов: %.2f%n", totalInterest);
        System.out.printf(Locale.US, "Последний платёж: %.2f%n", lastPayment);
        System.out.printf(Locale.US, "Сэкономлено месяцев: %d%n", savedMonths);
        System.out.printf(Locale.US, "Экономия на процентах: %.2f%n", savedInterest);
    }

    private static double readDouble(Scanner sc, String prompt, double min, double max, boolean inclusiveMin) {
        while (true) {
            System.out.print(prompt);
            if (sc.hasNextDouble()) {
                double val = sc.nextDouble();
                boolean minOk = inclusiveMin ? (val >= min) : (val > min);
                if (minOk && val <= max) return val;
            } else {
                sc.next();
            }
            System.out.println("Ошибка ввода. Повторите попытку.");
        }
    }

    private static int readInt(Scanner sc, String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);
            if (sc.hasNextInt()) {
                int val = sc.nextInt();
                if (val >= min && val <= max) return val;
            } else {
                sc.next();
            }
            System.out.println("Ошибка ввода. Введите целое число в заданных границах.");
        }
    }
}
