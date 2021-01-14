# Problem 9
#### Problem
![[p0009#]]
#### Concepts
#### Discussion
A brute-force approach will solve this problem trivially fast on modern computers. I would like to avoid the brute-force method for this problem, so I choose to solve most of the problem using algebra. The result requires only solving a simple equation for the only integer value of $a$ and $b$.

Given,

$$a^2 + b^2 = c^2$$

$$a + b + c = 1000$$

Then,

$$c = \sqrt(a^2+b^2)$$

$$a+b+\sqrt(a^2+b^2)=1000$$

$$\sqrt(a^2+b^2)=1000-a-b$$

$$a^2+b^2=(1000-a-b)^2$$

$$a^2+b^2=1000^2-1000a-1000b-1000a+a^2+ab-1000b+ab+b^2$$

$$a^2+b^2=1000^2-2000a-2000b+2ab+a^2+b^2$$

$$1=1000^2-2000a-2000b+2ab$$

$$1=1000(1000-2a)-b(2000-2a)$$

$$b(2000-2a)=1000(1000-2a)$$

$$b=\frac{1000(1000-2a)}{2000-2a}$$

$$b=\frac{1000(500-a)}{1000-a}$$

Therefor,
 * if $a=0$, then $b=500$
 * if $b=0$, then $a=500$
 * Since $b<c$, then the upper limit of $b$ is where $b$ approaches $c$. Thus, $b<500$.
 * Since $a<b$, then the upper limit of $a$ is where $a$ approaches $a=b$

$$b=\frac{1000(500-b)}{1000-b}$$

$$b(1000-b)=1000*500-1000b$$

$$1000b-b^2=1000*500-1000b$$

$$0=1000*500-2000b+b^2$$

Quadratic formula,

$$b=\frac{2000\pm\sqrt{(-2000)^2-4(1)(1000*500)}}{2(1)}$$

$$b=500(2\pm\sqrt{2})$$

For $b<500<1000$, $b=292.89$, so $a$ must be $a < 500(2-\sqrt{2})$.

Altogether we have,

$$b=\frac{1000(500-a)}{1000-a}$$

$$1 < a < 500(2-\sqrt{2})$$

$$1 < b < 500$$

And more abstractly,

$$b=\frac{n(n/2-a)}{n-a}$$

$$1 < a < n/2(2-\sqrt{2})$$

$$1 < b < n/2$$

According to the problem statement, only one unique pair of $a,b$ should exist given this criteria. Find this pair and calculate the product $abc$.

#### Solution
#### Answer
<details><summary>Spoiler warning</summary>$ANSWER</details>


#### Tags