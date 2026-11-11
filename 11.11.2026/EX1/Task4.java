import java.util.Locale;
import java.util.Scanner;

public class Task3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);
        int N = readInt(scanner, "Введите количество дней N (3..100): ", 3, 100);

        double[] incomes = new double[N];
        double[] expenses = new double[N];
        double[] dailyBalances = new double[N];

        for (int i = 0; i < N; i++) {
            incomes[i] = readNonNegativeDouble(scanner, "День " + (i + 1) + " — доход: ");
            expenses[i] = readNonNegativeDouble(scanner, "День " + (i + 1) + " — расход: ");
            dailyBalances[i] = incomes[i] - expenses[i];
        }

        double totalIncome = 0.0;
        double totalExpense = 0.0;

        int bestDay = 1;
        double maxDailyBalance = dailyBalances[0];

        int currentLossStreak = 0;
        int maxLossStreak = 0;

        double cumulativeBalance = 0.0;
        double minCumulativeBalance = Double.MAX_VALUE;
        int minCumulativeDay = 1;

        for (int i = 0; i < N; i++) {
            totalIncome += incomes[i];
            totalExpense += expenses[i];

            if (dailyBalances[i] > maxDailyBalance) {
                maxDailyBalance = dailyBalances[i];
                bestDay = i + 1;
            }

            if (dailyBalances[i] < 0) {
                currentLossStreak++;
                if (currentLossStreak > maxLossStreak) {
                    maxLossStreak = currentLossStreak;
                }
            } else {
                currentLossStreak = 0;
            }

            cumulativeBalance += dailyBalances[i];
            if (cumulativeBalance < minCumulativeBalance) {
                minCumulativeBalance = cumulativeBalance;
                minCumulativeDay = i + 1;
            }
        }

        double totalBalance = totalIncome - totalExpense;
        double averageBalance = totalBalance / N;

        System.out.printf(Locale.US, "Доходы всего: %.2f%n", totalIncome);
        System.out.printf(Locale.US, "Расходы всего: %.2f%n", totalExpense);
        System.out.printf(Locale.US, "Итоговый баланс: %.2f%n", totalBalance);
        System.out.printf(Locale.US, "Средний баланс: %.2f%n", averageBalance);
        System.out.printf(Locale.US, "Лучший день: %d (%.2f)%n", bestDay, maxDailyBalance);
        System.out.printf(Locale.US, "Длина серии убыточных дней: %d%n", maxLossStreak);
        System.out.printf(Locale.US, "Минимальный накопленный баланс: %.2f (день %d)%n", minCumulativeBalance, minCumulativeDay);
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
            System.out.println("Ошибка ввода. Введите целое число от " + min + " до " + max + ".");
        }
    }

    private static double readNonNegativeDouble(Scanner sc, String prompt) {
        while (true) {
            System.out.print(prompt);
            if (sc.hasNextDouble()) {
                double val = sc.nextDouble();
                if (val >= 0) return val;
            } else {
                sc.next();
            }
            System.out.println("Ошибка ввода. Сумма должна быть >= 0.");
        }
    }
}
