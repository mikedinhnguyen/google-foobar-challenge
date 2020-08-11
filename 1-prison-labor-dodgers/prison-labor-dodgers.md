
## Challenge 1, Round 1: Prison Labor Dodgers

### Prompt: 

Commander Lambda is all about efficiency, including using her bunny prisoners for manual labor. But no one's been properly monitoring the labor shifts for a while, and they've gotten quite mixed up. You've been given the task of fixing them, but after you wrote up new shifts, you realized that some prisoners had been transferred to a different block and aren't available for their assigned shifts. And manually sorting through each shift list to compare against prisoner block lists will take forever - remember, Commander Lambda loves efficiency!

Given two almost identical lists of prisoner IDs x and y where one of the lists contains an additional ID, write a function answer(x, y) that compares the lists and returns the additional ID.

For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], the function answer(x, y) would return 6 because the list x contains the integer 6 and the list y doesn't. Given the lists x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], the function answer(x, y) would return -4 because the list y contains the integer -4 and the list x doesn't.

In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 but never more than 99, and one of the lists will contain an additional unique integer which should be returned by the function. The same n non-unique integers will be present on both lists, but they might appear in a different order, like in the examples above. Commander Lambda likes to keep her numbers short, so every prisoner ID will be between -1000 and 1000.

---
### Approach:

I was given 24 hours to complete this challenge. The difficulty was pretty much equivalent to an easy LeetCode / interview question, but a little more fleshed out content wise. Since I wanted to keep track of the outlier of both arrays, I checked which of the two arrays was bigger and then track the numbers of the bigger array via HashMap. Since it's guaranteed that there will be one outlier, when you check the smaller array, you'll want to check if its count in the HashMap is 0, or if it doesn't even exist at all. If so, just return that value.

##### Completion Time: Around 3 hours

---
Java code:
``` java
public static int solution(int[] x, int[] y) {
    Map<Integer, List<Integer>> nums = new HashMap<>();
    
    if (x.length < y.length) {
        for (int i = 0; i < x.length; i++) {
        	if (nums.get(x[i] % 10) == null) {
        		nums.put(x[i] % 10, new LinkedList<Integer>());
        	}
        	nums.get(x[i] % 10).add(x[i]);
        }
        for (int i = 0; i < y.length; i++) {
            if (nums.get(y[i] % 10) == null ){
                return y[i];
            }
            if (!nums.get(y[i] % 10).contains(y[i])) {
            	return y[i];
            }
            nums.remove(y[i] % 10, y[i]);
        }
    }
    
    if (y.length < x.length) {
        for (int i = 0; i < y.length; i++) {
        	if (nums.get(y[i] % 10) == null) {
        		nums.put(y[i] % 10, new LinkedList<Integer>());
        	}
        	nums.get(y[i] % 10).add(y[i]);
        }
        for (int i = 0; i < x.length; i++) {
            if (nums.get(x[i] % 10) == null ){
                return x[i];
            }
            if (!nums.get(x[i] % 10).contains(x[i])) {
            	return x[i];
            }
            nums.remove(x[i] % 10, x[i]);
        }
    }
    
    return -1000;
}
```