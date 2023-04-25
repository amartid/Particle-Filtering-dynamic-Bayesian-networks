# Advanced Artificial Intelligence
## Dynamic Bayesian Networks
This code was implemented for the 3rd assignment on Advanced Artificial Intelligence Course - Master in Applied Informatics.

## The Problem

A body moves in a one-dimensional space of three regions, L, C, and R, as shown in the figure below:


| L | R | C |
|:-:|:-:|:-:|


At each moment in time, the body is in one of the three regions. There is always wind blowing in the movement space of the object, which can be either eastward (E, blowing to the left) or westward (W, blowing to the right).

The transition model is as follows: (At table - .xls file)

-  The direction of the wind, At, at time t depends on its direction At-1 at the previous time t-1, according to the following table:


<table class="tg">
<tbody>
  <tr>
    <td class="tg-t6k2"></td>
    <td class="tg-lhti" colspan="2">At</td>
  </tr>
  <tr>
    <td class="tg-vrnj">At-1</td>
    <td class="tg-nrix">E</td>
    <td class="tg-nrix">W</td>
  </tr>
  <tr>
    <td class="tg-9wq8">E</td>
    <td class="tg-nrix">0.7</td>
    <td class="tg-nrix">0.3</td>
  </tr>
  <tr>
    <td class="tg-9wq8">W</td>
    <td class="tg-nrix">0.3</td>
    <td class="tg-nrix">0.7</td>
  </tr>
</tbody>
</table>

That is, there is always a 70% chance for the wind to maintain its direction and a 30% chance to change it.

-  The position Xt of the object at time t depends on its position Xt-1 and the direction of the wind At-1 at the previous time t-1, according to the following table:

<table class="tg">
<tbody>
  <tr>
    <td class="tg-t6k2"></td>
    <td class="tg-uzvj"></td>
    <td class="tg-vrnj" colspan="3">Xt</td>
  </tr>
  <tr>
    <td class="tg-vrnj">Xt-1</td>
    <td class="tg-vrnj">At-1</td>
    <td class="tg-9wq8">L</td>
    <td class="tg-9wq8">C</td>
    <td class="tg-9wq8">R</td>
  </tr>
  <tr>
    <td class="tg-9wq8">L</td>
    <td class="tg-9wq8">E</td>
    <td class="tg-9wq8">1</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">0</td>
  </tr>
  <tr>
    <td class="tg-9wq8">L</td>
    <td class="tg-9wq8">W</td>
    <td class="tg-9wq8">0.5</td>
    <td class="tg-9wq8">0.5</td>
    <td class="tg-9wq8">0</td>
  </tr>
  <tr>
    <td class="tg-9wq8">C</td>
    <td class="tg-9wq8">E</td>
    <td class="tg-9wq8">0.5</td>
    <td class="tg-9wq8">0.5</td>
    <td class="tg-9wq8">0</td>
  </tr>
  <tr>
    <td class="tg-9wq8">C</td>
    <td class="tg-9wq8">W</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">0.5</td>
    <td class="tg-9wq8">0.5</td>
  </tr>
  <tr>
    <td class="tg-9wq8">R</td>
    <td class="tg-9wq8">E</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">0.5</td>
    <td class="tg-9wq8">0.5</td>
  </tr>
  <tr>
    <td class="tg-9wq8">R</td>
    <td class="tg-9wq8">W</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">1</td>
  </tr>
</tbody>
</table>


In other words, the object never moves against the wind, while there is always a 50% chance of staying in the same position and a 50% chance of moving one position in the direction of the wind (unless there is no new position in the direction of the wind, in which case it remains still with 100% probability). Note that the object can never move two positions.

There is a camera that tells us the region where the object is located at each moment in time. The relevant sensor model is given by the following table:
<table class="tg">
<tbody>
  <tr>
    <td class="tg-t6k2"></td>
    <td class="tg-lhti" colspan="3">Et</td>
  </tr>
  <tr>
    <td class="tg-wa9f">Xt-1</td>
    <td class="tg-cly1">L</td>
    <td class="tg-cly1">C</td>
    <td class="tg-cly1">R</td>
  </tr>
  <tr>
    <td class="tg-lboi">L</td>
    <td class="tg-cly1">0.7</td>
    <td class="tg-cly1">0.2</td>
    <td class="tg-cly1">0.1</td>
  </tr>
  <tr>
    <td class="tg-lboi">C</td>
    <td class="tg-cly1">0.3</td>
    <td class="tg-cly1">0.4</td>
    <td class="tg-cly1">0.3</td>
  </tr>
  <tr>
    <td class="tg-cly1">R</td>
    <td class="tg-cly1">0.1</td>
    <td class="tg-cly1">0.2</td>
    <td class="tg-cly1">0.7</td>
  </tr>
</tbody>
</table>

At time t=0, east wind is blowing (A0=E), and the object is equally likely to be in one of the three positions. Observations from the camera start at time t=1.

Let (e1,e2,e3) be a sequence of three observations from the camera.

a) Calculate the most likely sequence of states the object passed through.

-   P(X2 | e1:3)
-   P(X3 | e1:3)
-   P(X4 | e1:3)
-   P(A2 | e1:3)
-   P(A3 | e1:3)
-   P(A4 | e1:3)

b) Calculate approximately the above probability distributions by implementing any of the relevant algorithms - particle filtering in a programming language of your choice. Compare with the result from the previous question.

c) Find the most probable sequence of object positions and wind directions (combined, not separately) for the time interval from t=0 to t=3.

Various sequences of camera observations are given:

<table class="tg">
<tbody>
  <tr>
    <td class="tg-c3ow">e1</td>
    <td class="tg-c3ow">e2</td>
    <td class="tg-c3ow">e3</td>
  </tr>
  <tr>
    <td class="tg-c3ow">C</td>
    <td class="tg-c3ow">C</td>
    <td class="tg-c3ow">C</td>
  </tr>
</tbody>
</table>

## Implementation

The project was implemented using Python programming language. The relevant solution for predicting the motion of the body and the most probable sequence of object positions and wind directions were implemented using particle filtering algorithm.


## Code execution

After printing the explanation of all tables and elements of the problem on the screen, the value 0 is given to t (time) and the method for constructing the initial state is called. Then, for t less than 4, the iteration of applying the position transition model, the wind transition model, and the calculation of the gravity coefficients follows. For t different than 4, sampling takes place. The values of the sampling are transferred to array A before the next iteration. Here, a check has been introduced to verify that the values have been copied correctly. Finally, for all cases, the values of the position probability and wind probability for array A are calculated and the results for each time are printed on the screen. Once all iterations are completed, the final results are printed in the form of arrays and columns.

## Regarding the results

Since the sampling is done with the randomness coefficient each time the code runs, there are different results, but there is a convergence of the values towards the values obtained with the Filtering-Smoothing method followed in Excel, and this is apparent and the goal (with a small deviation of the order of the 2nd decimal place).
