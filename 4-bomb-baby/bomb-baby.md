
## Level 3, Challenge 1: Bomb, Baby!

### Prompt: 

You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time. 

But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good! 

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!) 

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10<sup>50</sup>. For example, if M = "2" and F = "1", one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4", it would not be possible.

-- Test cases --  
Input: Solution.solution('2', '1')  
Output: 1  
  
Input: Solution.solution('4', '7')  
Output: 4  

---
### Approach:

I was given 96 hours to complete this challenge. Okay, we're starting to sweat a little here. This was really more math based and puzzle oriented. They ask you to see how many bombs replicate off of each other and the lowest numbers needed to get there. I struggled on this for quite a bit, and it really didn't hit me until the next day, literally while I was in the shower. I used my finger and the condensation on my glass shower wall to confirm this was correct. In reality, this problem isn't as hard as it looks! You basically want to see how many time one bomb can go into another and then subtract one bomb's current number with the other and repeat until we are down to one of both bombs or we go over and it's impossible. An example might suit a better explanation:

Say we have 4 Mach bombs and 10 Facula bombs:       
`(4, 11), count: 0`  
We can see the Mach bombs are less than Facula and see how many times Mach goes into Facula, count it, and subtract Facula from Mach:      
`(4, 3), count: 2`  
Now Facula has less than Mach, so we check how many times Facula goes into Mach:               
`(1, 3), count: 3`  
We do the same thing here, and we should check that we have only one of each bombs:          
`(1, 1), count: 5`  

![Wait... what?](https://github.com/mikedinhnguyen/google-foobar-challenge/blob/master/images/Screen%20Shot%202020-08-03%20at%209.49.35%20PM.png)

I submitted my answer, only to have gotten two test cases wrong. That's weird. I was so sure this was the correct answer! Ah ha, but let's read the prompt again. "**M and F will be string representations of positive integers no larger than 10<sup>50</sup>.**" Yeah, for this challenge up until now I've been storing these values into doubles, which is pretty much asking for trouble. But I had remembered from my Java training that in rare cases where big numbers are necessary, we break out the BigInteger class. Was it tedious converting all my code to BigInteger and conforming to its methods and protocol? Yes. Did my solution work after? More importantly, yes.

### Takeaways:

- Learned more about BigInteger and how to incorporate it
- Made sure we read the prompt carefully and how to approach edge cases
- Flexed my math skills

##### Completion Time: 1 day, 2 hours, 31 minutes, 49 seconds

---

I'm leaving the Java code in its original form before converting to BigInteger's class, just so it looks readable, and as a thoughtful exercise for anyone actually trying to steal my code for Google's Foobar challenge ;)

Java code:
``` java
   public static String solution(String x, String y) {
       int count = 0;
       double machBombs = Double.parseDouble(x);
       double faculaBombs = Double.parseDouble(y);
       
       while (machBombs > 1 || faculaBombs > 1) {
           if (machBombs == 1 && faculaBombs > 1) {
               count += faculaBombs - 1;
               faculaBombs = 1;
           }
           else if (faculaBombs == 1 && machBombs > 1) {
               count += machBombs - 1;
               machBombs = 1;
           }
           else if (faculaBombs > machBombs) {
               int divide = (int)(faculaBombs/machBombs);   
               count += divide;   
               faculaBombs -= (divide * machBombs);
           }
           else if (machBombs > faculaBombs) {
               int divide = (int)(machBombs/faculaBombs);   
               count += divide;    
               machBombs -= (divide * faculaBombs);
           }
           else break;
           
           if (machBombs < 1 || faculaBombs < 1) {
               break;
           }
           
       }
       
       if (machBombs == 1 && faculaBombs == 1) 
           return Integer.toString(count);
       return "impossible";
   }
```

---

![A successful submission](https://github.com/mikedinhnguyen/google-foobar-challenge/blob/master/images/Screen%20Shot%202020-08-04%20at%2012.40.52%20PM.png)