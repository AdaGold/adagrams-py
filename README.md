# AdaGrams

## Skills Assessed

- Following directions and reading comprehension
- Reading tests
- Using git to maintain code
- Manipulating and processing data in lists and strings

## Goal

An [anagram](https://en.wikipedia.org/wiki/Anagram) is a word or phrase formed by rearranging the letters of a different word or phrase. In this project you will be creating _Adagrams_, a game in which a player is given a random set of letters and must make an anagram using those letters.  Each submitted word will score points.

While working on _Adagrams_, it may help to think of a physical metaphor for this game, such as other common word games like [_Scrabble_](https://en.wikipedia.org/wiki/Scrabble) or [_Bananagrams_](https://en.wikipedia.org/wiki/Bananagrams). These games all feature a _pool_ of letter _tiles_ that the player _draws_ from.

In this version of _Adagrams_, we will only be working with the English alphabet.

![an image of a pile of letter tiles](images/letter-tiles.jpeg)

## One-Time Project Setup

Follow these directions once, at the beginning of your project:


1. Navigate to your projects folder named `projects`.

If you followed Ada's recommended file system structure from the Intro to Dev Environment lesson in Learn, you can navigate to your projects folder with the following command:

```bash
$ cd ~/Developer/projects
```

2. In Github click on the "Fork" button in github and fork the repository to your Github account.  This will make a copy of the project in your github account. 

![Fork Button](images/fork.png)

3. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `adagrams-py`, and then puts the project into this new folder.  Make sure you are cloning from your copy of the project and not the class version (ada-cX).

```bash
$ git clone ...
```

Use `ls` to confirm there's a new project folder

4. Move your location into this project folder

```bash
$ cd adagrams-py
```

5. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

6. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

7. Install dependencies once at the beginning of this project with

```bash
# Must be in activated virtual environment
$ pip install -r requirements.txt
```

Summary of one-time project setup:
- [ ] Fork the project respository
- [ ] `cd` into your `projects` folder
- [ ] Clone the project onto your machine
- [ ] `cd` into the `adagrams-py` folder
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`

## Project Development Workflow

1. When you want to begin work on this project, ensure that your virtual environment is activated:

```bash
$ source venv/bin/activate
```

2. Run the game and play test your current wave.  Replace the word `wave` below with the wave number (ie, 1, 2, 3 or 4):

```bash
# Must be in activated virtual environment
$ python main.py wave
```

3. Use play-testing to guide your development.

4. Use tests to verify your functions after thoroughly play-testing. See instructions for running tests in the section below. *A complete set of unit tests is provided for this project.*

5. Use git to commit your work regularly!  Commit between each wave.

```bash
# Add your current work
$ git add .
$ git commit -m "meaningful message explaining your commit"
```

6. Move on to the next wave!

7. When you are finished working for the day, deactivate your environment with deactivate or closing the Terminal tab/window

```bash
$ deactivate
```

## Details About How to Run Tests

1. Find the test file that contains the test you want to run.

   - Check the `tests` folder, and find the test file you want to run
   - In that test file, read through each test case


2. Run the tests for your specific wave

```bash
# Must be in activated virtual environment
$ pytest tests/test_wave_01.py
```

3. Run all tests that exist in this project with:

```bash
# Must be in activated virtual environment
$ pytest
```

4. If you want to see any `print` statements print to the console, add `-s` to the end of any `pytest` command:

```bash
# Must be in activated virtual environment
$ pytest -s
```

## Project Write-Up: How to Complete and Submit


The goal of this project is to write code in `game.py` so each of the functions meet the requirements outlined in the Project Directions below. 

Go through the waves one-by-one and build the features of this game.

You will use play-testing and unit tests to drive your development.

At submission time, no matter where you are, submit the project via Learn.

This will let us give feedback on what you've finished so that you can be better prepared for the next project.

## Project Directions

### Get Familiar

Take time to read through the Wave 1 implementation requirements and the tests for Wave 1. Write down your questions, and spend some time going through your understanding of the requirements and tests. Make sure you can run `$ pytest` and see the tests fail.

If, after you have taken some time to think through the problem and would like direction for how to dissect the problem, or if you need clarity on the terms/vocabulary we used in this project, you can check out [a small hint we've provided](./project_docs/hints.md).

### A Note About `random`, Libraries, and Built-In Methods

👀 **Please review this section carefully** 👀

We include an import statement in `game.py` which imports the [`randint`](https://docs.python.org/3/library/random.html#random.randint) function from the `random` module. **Do not change this import statement.** You may only use the `randint` function from the `random` module. 

As this is our first project and we're familiarizing ourselves with Python, the more code that we write, the more practice we get, both with syntax, and with thinking about how to approach the problem. In the near future, with more practice and time spent coding we will permit the use of library functions. All of the wave requirements for this project can be achieved without any of the other `random` methods, like `sample`, `choice`, or `select`.

Additionally, there are helper methods in the "built-in" scope, such as `max`, which we ask you to refrain from using in this project too. However, methods on collections that are necessary for adding, removing, or iterating of data are fine to use. There's really no other way for you to work with data in collections than to use their supplied methods. 

Implement as much as possible on your own for the version you submit for review. This won't be our recommendation forever, but especially early in the program, the more logic you plan out, and the more code you challenge yourself to write, the stronger a foundation you'll be building for yourself. If you do still want to try out those other functions, you can always make another copy of the project to play around with to get even more practice! But please do not include them in your submitted version.

### Wave 1: draw_letters

Your first task is to build a hand of 10 letters for the user. To do so, implement the function `draw_letters` in `game.py`. This method should have the following properties:

- No parameters
- Returns an array of ten strings
  - Each string should contain exactly one letter
  - These represent the hand of letters that the player has drawn
- The letters should be randomly drawn from a pool of letters
  - This letter pool should reflect the distribution of letters as described in the table below
  - There are only 2 available `C` letters, so `draw_letters` cannot ever return more than 2 `C`s
  - Since there are 12 `E`s but only 1 `Z`, it should be 12 times as likely for the user to draw an `E` as a `Z`
- Invoking this function should **not** change the pool of letters
  - Imagine that the user returns their hand to the pool before drawing new letters

#### Distribution of Letters

| Letter : Qty. | Letter : Qty. |
|:------:|:-----:|
| A : 9  | N : 6 |
| B : 2  | O : 8 |
| C : 2  | P : 2 |
| D : 4  | Q : 1 |
| E : 12 | R : 6 |
| F : 2  | S : 4 |
| G : 3  | T : 6 |
| H : 2  | U : 4 |
| I : 9  | V : 2 |
| J : 1  | W : 2 |
| K : 1  | X : 1 |
| L : 4  | Y : 2 |
| M : 2  | Z : 1 |

**Note:** Making sure that the drawn letters match the rules of the letter pool can be straightforward or very difficult, depending on how you build the data structure for the letter pool. It is worth spending some time to think carefully about this.


### Wave 2: use_available_letters

Next, you need a way to check if an input word (a word a player submits) only uses characters that are contained within a collection (or hand) of drawn letters. Essentially, you need a way to check if the word is an anagram of some or all of the given letters in the hand.

To do so, implement the function called `uses_available_letters` in `game.py`. This function should have the following properties:

- Has two parameters:
   - `word`, the first parameter, describes some input word, and is a string
   - `letter_bank`, the second parameter, describes an array of drawn letters in a hand. You can expect this to be an array of ten strings, with each string representing a letter
- Returns either `True` or `False`
- Returns `True` if every letter in the `input` word is available (in the right quantities) in the `letter_bank`
- Returns `False` if not; if there is a letter in `input` that is not present in the `letter_bank` or has too much of compared to the `letter_bank`

### Wave 3: score_word

Now you need a function returns the score of a given word as defined by the Adagrams game.

Implement the function `score_word` in `game.py`. This method should have the following properties:

- Has one parameter: `word`, which is a string of characters
- Returns an integer representing the number of points
- Each letter within `word` has a point value. The number of points of each letter is summed up to represent the total score of `word`
- Each letter's point value is described in the table below
- If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points

#### Score chart

|Letter                        | Value|
|:----------------------------:|:----:|
|A, E, I, O, U, L, N, R, S, T  |   1  |
|D, G                          |   2  |
|B, C, M, P                    |   3  |
|F, H, V, W, Y                 |   4  |
|K                             |   5  |
|J, X                          |   8  |
|Q, Z                          |   10 |

### Wave 4: get_highest_word_score

After several hands have been drawn, words have been submitted, checked, scored, and played, you need a way to find the highest scoring word. This function looks at the list of `word_list` and calculates which of these words has the highest score, applies any tie-breaking logic, and returns the winning word in a special data structure.

Implement a function called `get_highest_word_score` in `game.py`. This method should have the following properties:

- Has one parameter: `word_list`, which is a list of strings
- Returns a tuple that represents the data of a winning word and its score.  The tuple must contain the following elements:
  - index 0 ([0]): a string of a word
  - index 1 ([1]): the score of that word
- In the case of tie in scores, use these tie-breaking rules:
    - prefer the word with the fewest letters...
    - ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
    - If the there are multiple words that are the same score and the same length, pick the first one in the supplied list
