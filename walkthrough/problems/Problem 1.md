# Problem 1
#### Problem
![[p0001#]]
#### Concepts
[[Natural Numbers]]
#### Discussion
We can approach this purely computationally. We can easily iterate over the sum of each multiple of 3 up to and less than 1000. We just test each multiple to ensure they are below 1000 on each iteration. Next, we iterate through the sum of each multiple of 5 below.

Alternatively, we know that the largest multiple of 3 less than 1000 is roughly 1000 divided by 3. We can use this to approximate a limit to iterate to for 3. We could then do the same to find an upper limit for 5. The limits for each would be different. Unfortunately, this calculation would produce a negligible improvement on execution time since the brute force approach would be trivial for most modern computers.

Roughly,
3n+3(n+1)+...+5n+5(n+1)+...
3(n+n+1+n+2...+m+m+1...)+5(n+n+1+n+2...+m)
( 3(m+1+m+2...)+5(1) )(n+n+1+n+2...+m)

#### Solution

For each natural number from 0 to 1000, we: 

1. Multiply the number by 3 and ensure that the product is still less than 1000. 
2. If the product is less than 1000, we add it to the sum 
3. Next, to address multiples of 5, we repeat the process: 
4. For each natural number from 0 to 1000, multiply the number by 5 and ensure the product is less than 1000
5. If the product is less than 1000, we add it to the sum

#### Answer
<details><summary>Spoiler warning</summary>$ANSWER</details>

#### Tags