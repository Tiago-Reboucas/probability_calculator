# Probability Calculator

Full code run with examples test can be found in: https://replit.com/@tiagoreboucas90/boilerplate-probability-calculator#prob_calculator.py

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

This project is to determine the approximate probability of drawing certain balls randomly from a hat.

The class `Hat` takes a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:

```text
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

A hat will always be created with at least one ball. The arguments passed into the hat object upon creation are converted to a `contents` instance variable. `contents` is list of strings containing one item for each ball in the hat. Each item in the list is a color name representing a single ball of that color. For example, if your hat is `{"red": 2, "blue": 1}`, `contents` is `["red", "red", "blue"]`.

The `Hat` class has a `draw()` method that accepts an argument indicating the number of balls to draw from the hat. This method removes balls at random from `contents` and return those balls as a list of strings. The balls do not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, it returns all the balls.

There is a `experiment()` function (not inside the `Hat` class). This function accept the following arguments:

- `hat`: A hat object containing balls that is copied inside the function.
- `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue - balls and 1 red ball from the hat, set `expected_balls` to `{"blue":2, "red":1}`.
- `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
- `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The `experiment()` function returns a probability.

For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.

Here is how you would call the `experiment()` function based on the example above with 2000 experiments:

```text
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                expected_balls={"red":2,"green":1},
                num_balls_drawn=5,
                num_experiments=2000)
```

Since this is based on random draws, the probability will be slightly different each time the code is run.

## Testing
- If you chose to open in [replit](https://replit.com/@tiagoreboucas90/boilerplate-probability-calculator#prob_calculator.py), the code is writen in `prob_calculator.py`. For development, you can use `main.py` to test the code. Click the "run" button and `main.py` will run.
- The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.
