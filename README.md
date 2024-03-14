# Nonstandard

"The Python nonstandard library."

A collection of things not present in the Python standard library.

## Developing

Run all these commands from the project root directory.

Install the development dependencies using
`pip install -r requirements_development.txt`
.

Then install the project
`pip install -e .`
.

Then install pre-commit by running
`pre-commit install`
.

To run tests simply run
`pytest`
.

To run the pre-commit checks at any time use
`pre-commit run --all-files`
.

To build the project to publish it, run
`python -m build`
.
