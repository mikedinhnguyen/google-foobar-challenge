
## Level 3, Challenge 3: Doomsday Fuel  

### Prompt:  

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state). You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.  

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly.   

For example, consider the matrix m:  
[  
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability  
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities  
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)  
  [0,0,0,0,0,0],  # s3 is terminal  
  [0,0,0,0,0,0],  # s4 is terminal  
  [0,0,0,0,0,0],  # s5 is terminal  
]  
So, we can consider different paths to terminal states, such as:  
s0 -> s1 -> s3  
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4  
s0 -> s1 -> s0 -> s5  
Tracing the probabilities of each, we find that:  
s2 has probability 0  
s3 has probability 3/14  
s4 has probability 1/7  
s5 has probability 9/14  
So, putting that together, and making a common denominator, gives an answer in the form of [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is [0, 3, 2, 9, 14].  

--Test cases--  

Input:  
{{0, 2, 1, 0, 0},  
{0, 0, 0, 3, 4},  
{0, 0, 0, 0, 0},  
{0, 0, 0, 0, 0},  
{0, 0, 0, 0, 0}}  
Output:  
[7, 6, 8, 21]  

Input:  
{{0, 1, 0, 0, 0, 1},   
{4, 0, 0, 3, 2, 0},  
{0, 0, 0, 0, 0, 0},  
{0, 0, 0, 0, 0, 0},  
{0, 0, 0, 0, 0, 0},  
{0, 0, 0, 0, 0, 0}}  
Output:  
[0, 3, 2, 9, 14]  

---
### Approach:

I was given 96 hours to complete this challenge. This was it. The straw that broke the camel's back. The challenge that nearly broke me. And it was also my downfall of my Google Foobar challenge attempt. If you were looking to me because you have had the unfortunate ordeal of randomly getting this problem, here is my one true advice: research "absorbing Markov chains" on YouTube. I was a bit foolish by letting myself not solve this problem until I had two days left. I was really struggling with the probabilities, and the answer lied in Markov chains, which I had never heard of before this challenge. I also didn't do something I was proud of: looking up hints from other people who also had struggled with this question. By this point, I had known that after I had completed this challenge, I could send out my challenge results to a recruiter, but after looking stuff up, that possibility of them reaching out back to me was getting lower and lower. But I wasn't trying to get a job at Google, I just wanted the satisfaction of completing the challenge! I had to borrow a lot of code when it came to converting decimals to fractions and finding the inverse of a matrix. I was so close to getting all the test cases! I had 9 out of 10 cases, but I was confused as to what the problem could be. Well, someone had leaked the test cases of the Doomsday Fuel challenge, and I tried testing all of them against my code and found out, that I needed to arrange the rows and columns of the matrix in a specfic way relating to Markov chains. With a lot of time in the past few days already poured into this challenge, I was exhausted. I felt bad giving up. I was so close. But I had failed to find a solution before my time ran out.

![:(]()

### Takeaways:  

- Learned about Markov chains  
- Tested my math on matrices, fractions, and Gaussian elimination  
- Do not understimate how much time you have on a problem  
- No one knows everything  

##### Completion Time: N/A

---

Java code:  
``` java

``` 

Some helpful links:  
[Converting Decimal to Fractions](https://stackoverflow.com/questions/56684745/converting-decimal-into-fractions-java-and-python-gives-different-output)
[How to find inverse matrix in Java](https://www.sanfoundry.com/java-program-find-inverse-matrix/)
[Doomsday Fuel Test Cases](https://pastebin.com/HAiEwnD2)
