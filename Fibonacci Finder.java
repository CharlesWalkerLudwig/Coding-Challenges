public class FibonacciFinder {
  public static void main(String[] args) {
    System.out.print(fibFinder(6));
  }
 
  public static int fibFinder(int n) {
  if (n == 0 || n == 1) {
    return n;
  } else {
    return fibFinder(n - 1) + fibFinder(n - 2);
  }
  }
}
