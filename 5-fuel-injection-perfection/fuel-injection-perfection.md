
## Level 3, Challenge 2: Fuel Injection Perfection

### Prompt:  

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly.  

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.  

The fuel control mechanisms have three operations:  

1) Add one fuel pellet  

2) Remove one fuel pellet  

3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)  

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.  

For example:  
solution(4) returns 2: 4 -> 2 -> 1  
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1  

Test cases  
Input:  
Solution.solution('4')  
Output:  
    2  

Input:  
Solution.solution('15')  
Output:  
    5  

---
### Approach:

I was given 96 hours to complete this challenge. I had some real trouble with this problem, but probably not for the reason you're thinking of. The math was pretty interesting for this one. We want to always try to divide by 2, since it's the fastest way to reach zero. We only want to subtract when we land on an odd number, or add when the number we add to can divide twice as fast as subtracting. This took me a while to figure out and it was even more frustrating when my logic I felt was airtight, and yet I kept failing the test cases.  

Java code:  
``` java
public static int solution(String x) {
  int count = 0;
  double fuel = Double.parseDouble(x);

  while (fuel > 1) {

    if (fuel % 2 == 0)
      fuel /= 2;
    else if (fuel != 3 && fuel % 4 == 1) 
      fuel++;
    else
      fuel--;

    count++;
  }

  return count;
}
``` 

Unlike the previous round, I think I knew where my code was going wrong. Since the solution input can be taken up to 309 digits long, I figured that using a double would do the trick. This didn't work. I tried using BigInteger as well but there was some loss of conversion in the math, and got a totally different number. Out of pure frustration and curiosity, I converted my code to Python.  

Python code:  
``` python
def solution(n):
  count = 0
  fuel = int(n)
  while (fuel > 1): 
    if (fuel % 2 == 0):
      fuel = fuel / 2
    elif ((fuel == 3) or (fuel % 4 == 1)):
      fuel -= 1
    else:
      fuel += 1
    count += 1
  return count
```

The entire logic stayed the same. And it worked. I'm not an expert on Python but I don't think it doesn't gets hung up on the length of integers or memory (I really don't know how it works). But hey, a win is a win.  

![python](https://github.com/mikedinhnguyen/google-foobar-challenge/blob/master/images/Screen%20Shot%202020-08-06%20at%202.55.23%20PM.png)

### Takeaways:  

- Made aware to be mindful of data type limits in Java  
- Python > Java when it comes to worrying about data type limits  

##### Completion Time: 1 day, 18 hours, 25 minutes, 10 seconds  

---

![A successful submission?](https://github.com/mikedinhnguyen/google-foobar-challenge/blob/master/images/Screen%20Shot%202020-08-06%20at%202.57.53%20PM.png)