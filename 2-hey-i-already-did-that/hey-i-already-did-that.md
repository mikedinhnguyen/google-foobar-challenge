
## Level 2, Challenge 1: Hey, I Already Did That!

### Prompt: 

Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep her minions on their toes. But you've noticed a flaw in the algorithm - it eventually loops back on itself, so that instead of assigning new minions as it iterates, it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and over again. You think proving this to Commander Lambda will help you make a case for your next promotion.

You have worked out that the algorithm has the following process: 

1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2

For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and it will stay in this cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.

Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function solution(n, b) which returns the length of the ending cycle of the algorithm above starting with n. For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1.

---
### Approach:

I was given 72 hours to complete this challenge. This one was pretty interesting! There was a lot of confusion at first about using different bases besides base 10, but I was really interested to learn more about it. At first, I tried to figure out how to base convert for every base number, until I realized the method is present in the Integer class, making life pretty easy for me. I keep an ArrayList as storage of numbers I have already obtained, including our starting number. I convert the x and y to base 10, if needed, and then do the math for z. Check if z is a number we have visited already. If not, we rinse and repeat, or rather rinse and recurse, until we find a cycle or a constant, in which we return the correct length for either case.

### Takeaways:

- Learned about converting to base *n*
- Refreshed on keeping track of cycles

##### Completion Time: 3 hours, 59 minutes, 19 seconds

---
Java code:
``` java
static ArrayList<String> storage = new ArrayList<>();

public static String baseConversion(String number, int sBase, int dBase) { 
    return Integer.toString(Integer.parseInt(number, sBase), dBase); 
} 

public static String rearrangeN(String number, boolean descending){
    // do order ascending always
    // if descending, reverse the string
    char[] ch = number.toCharArray();
    Arrays.sort(ch);
    String newNumber = Arrays.toString(ch).replace("[", "").replace("]", "").replace(", ", "");
    StringBuilder sb = new StringBuilder(newNumber);
    
    if (descending) {
        sb.reverse();
    }
    
    return sb.toString();
}

public static int solution(String n, int b) {
    storage.add(n);
    int k = n.length();
    
    String z;
    String xStr = rearrangeN(n, true);
    String yStr = rearrangeN(n, false);
    
    if (b != 10) {
        String newX = baseConversion(xStr, b, 10);
        String newY = baseConversion(yStr, b, 10);
        int x = Integer.parseInt(newX);
        int y = Integer.parseInt(newY);
        int beforeZ = x-y;
        z = baseConversion(Integer.toString(beforeZ), 10, b);
        
    }
    else {
        int x = Integer.parseInt(xStr);
        int y = Integer.parseInt(yStr);
        int beforeZ = x - y;
        z = Integer.toString(beforeZ);
    }
        
    StringBuilder sb = new StringBuilder(z);
    while (sb.length() < k) {
        sb.insert(0, "0");
    }
    String zStr = sb.toString();

    if (storage.contains(zStr)) {
        if (zStr.equals(n)) {
            return 1;
        }
        else {
            int count = 0;
            for (int i = storage.indexOf(zStr); i < storage.size(); i++) {
                count++;
            }
            return count;
        }
    }

    n = zStr;
    return solution(n, b); 
}
```

---

![Passing all test cases](https://github.com/mikedinhnguyen/google-foobar-challenge/blob/master/images/Screen%20Shot%202020-07-28%20at%203.23.52%20PM.png)

![A successful submission](https://github.com/mikedinhnguyen/google-foobar-challenge/blob/master/images/Screen%20Shot%202020-07-28%20at%203.35.10%20PM.png)