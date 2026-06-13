# The Farmer Was Replaced

## Pumpkin

> The yield of a giant pumpkin depends on the size of the pumpkin.
>
> ...
> A `nxn` pumpkin yields `n*n*6` pumpkins for `n >= 6`.
>
> It's a good idea to get at least 6x6 size pumpkins to get the full multiplier.

### Pumpkin Master

Multiple drones are used to plant pumpkins in [`pumpkin_master.py`](./pumpkin_master.py).

## Cactus

> A cactus is considered to be in sorted order if all neighboring cacti to the `North` and `East` are fully grown and larger or equal in size and all neighboring cacti to the `South` and `West` are fully grown and smaller or equal in size.
>
> The harvest will only spread if all adjacent cacti are fully grown and in sorted order.
This means that if a square of grown cacti is sorted by size and you harvest one cactus, it will harvest the entire square.
>
> ...
>
> You will receive cactus equal to the number of harvested cacti squared. So if you harvest `n` cacti simultaneously you will receive `n**2 Items.Cactus`

### Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

If we plant a full field of cacti, we have to sort all the cacti to maximize the number of harvested cacti at once.

### Approach
<!-- Describe your approach to solving the problem. -->

> Hint 1: If the rows are already sorted, sorting the columns will not unsort the rows.

We can sort all the cacti by sorting the rows and then the columns.

> Hint 2: ... you can only swap neighboring cacti.

If we use a sorting algorithm that only compares and swaps neighbors, the time complexity of the algorithm must be $O(n^2)$ on average[^lower-bound-on-simple-sorts]. Candidate sorting algorithms are bubble sort, cocktail sort, and gnome sort to name a few.

[^lower-bound-on-simple-sorts]: <https://courses.washington.edu/css501/ksung/Notes/13.Sorting/Lecture%2012%20-%20Sorting.htm>

### Complexity

Let $n$ be the world size. First, let's consider the case of a single drone. For a full field of cacti, the total number of one-dimensional sorts is $n*2$ ($n$ columns and $n$ rows), where $n$ is the world size.

- Time complexity: $O(n^3)$. Planting a full field of cacti takes $O(n^2)$, and sorting a full field of cacti takes $O(n^3)$.

Next, let's consider the case of using $n$ drones simultaneously.

- Time complexity: $O(n^2)$. Planting a full field of cacti takes $O(n)$, and sorting a full field of cacti takes $O(n^2)$.

### Code

Cocktail sort and gnome sort are implemented in [`cactus.py`](./cactus.py). This program uses only one drone.

Multiple drones are used to plant and sort cacti in [`cactus_mega.py`](./cactus_mega.py). This program saves a lot of time compared to the single-drone program.
