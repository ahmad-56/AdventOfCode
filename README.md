> This is a repo for all of my AoC puzzle solutions solved using Python.

# Advent of Code — Solutions

[Advent of Code](https://adventofcode.com/) is an annual programming event featuring two-part puzzles with user-specific inputs. 
Since 2025, puzzles have been released daily from December 1 to December 12; earlier events ran for 25 days. Each completed part 
awards one star. Participants can also create private leaderboards to compete with friends.

AoC is a great platform to test and enhance your logical skills as it challenges you to think
of creative solutions. The difficulty level is well balanced — beginners can solve the earlier
puzzles while experienced programmers still find it challenging at times.

As a beginner myself, I have found many AoC puzzles to be very challenging, resulting in code
with logical errors. To ensure this does not happen often, I solve the given example solution
by writing my own piece of code and then implementing the same logic in the main puzzle.

I have made a separate section for the [folder structure](#-structure-of-folders), however I would just
like to explain it a bit here as well.
For each day there is an input which for which I create a `.txt` file (although previously I used to store 
them in `.py` files). Then I solve the example solution to check if my reasoning and logic is correct. The sample code
is saved in a file named `exp.py`. This step is very essential in my opinion as it helps me find my mistakes by
debugging the smaller example input. However, as it is an example and may not contain all
possible scenarios, it has its downsides too. Afterwards I implement the same solution on
the main input. This file is therefore named after each part: `part1.py` / `part2.py`. 

This structure is further explained below.

Moreover I have shared all my progress in the [progress](#-progress) section. Previosuly I had to
manually change the progress and update it whenever I solved a new probelm. However, now I use a python program
which inputs the user the date and puzzle solved and automatically updates the `README` file.

---

## 📂 Structure of Folders

```
advent-of-code/
├── README.md
├── 2015/
│   ├── Day01/
│   │   ├── part1.py
│   │   ├── part2.py
│   │   ├── input.py      # puzzle input
│   │   ├── exp.py        # example solution for part 1
│   │   └── exp2.py       # example solution for part 2
│   └── ...
├── 2016/
│   └── ...
|    .
|    .
|    .
└── 2025/
    └── ...
```

---
## ⭐ Progress
> Last updated: 22nd September 2026
<br>Latest Puzzle Solved: 2017 Day 1 Part 1 & 2
<table>
  <tr>
    <th align="center">Total Progress:</th>
    <th align="center">70*/524</th>
  </tr>
</table>

<table>
  <tr>
    <th align="center">Year</th>
    <th align="center">Stars</th>
    <th align="center">Out of</th>
  </tr>
  <tr><td align="center">2025</td><td align="center">7*</td><td align="center">24</td></tr>
  <tr><td align="center">2024</td><td align="center">4*</td><td align="center">50</td></tr>
  <tr><td align="center">2023</td><td align="center">4*</td><td align="center">50</td></tr>
  <tr><td align="center">2022</td><td align="center">14*</td><td align="center">50</td></tr>
  <tr><td align="center">2021</td><td align="center">6*</td><td align="center">50</td></tr>
  <tr><td align="center">2020</td><td align="center">4*</td><td align="center">50</td></tr>
  <tr><td align="center">2019</td><td align="center">6*</td><td align="center">50</td></tr>
  <tr><td align="center">2018</td><td align="center">4*</td><td align="center">50</td></tr>
  <tr><td align="center">2017</td><td align="center">5*</td><td align="center">50</td></tr>
  <tr><td align="center">2016</td><td align="center">4*</td><td align="center">50</td></tr>
  <tr><td align="center">2015</td><td align="center">12*</td><td align="center">50</td></tr>
  <tr><td align="center">Total</td><td align="center">70*</td><td align="center">524</td></tr>
</table>


## 🔗 Links

- 🌐 [Advent of Code](https://adventofcode.com/)
- 💬 [About AoC](https://adventofcode.com/2024/about)

---

*Solutions by Ahmad*
