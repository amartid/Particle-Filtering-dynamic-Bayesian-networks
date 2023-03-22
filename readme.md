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


<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-t6k2{border-color:inherit;font-style:italic;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-lhti{font-style:italic;text-align:center;vertical-align:middle}
.tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-vrnj{border-color:inherit;font-style:italic;text-align:center;vertical-align:middle}
.tg .tg-nrix{text-align:center;vertical-align:middle}
</style>
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
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-t6k2{border-color:inherit;font-style:italic;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-uzvj{border-color:inherit;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-vrnj{border-color:inherit;font-style:italic;text-align:center;vertical-align:middle}
</style>
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

| e1 | e2 | e3 |
|----|----|----|
| C  | C  | C  |

## Implementation

The project was implemented using Python programming language. The relevant solution for predicting the motion of the body and the most probable sequence of object positions and wind directions were implemented using particle filtering algorithm.
