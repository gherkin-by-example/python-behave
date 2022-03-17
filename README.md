Gherkin By Example
==================

Gherkin By Example collection of projects to show how to configure and use tools
for the use of Gherkin as a specification language.

In this repository you'll find the examples to use Gherkin along
with the Python programming language and the [Behave] tool.


Python with Behave
------------------

This is a solution to URI Online Judge 1001 problem: add two numbers.

Some useful links before starting:
* [The problem statement](https://www.beecrowd.com.br/judge/en/problems/view/1001)
* [Example solutions in several programming languages](https://www.beegcrowd.com.br/judge/pt/faqs/about/examples)

The solution process presented here adopts a behavior-driven
development style. The original problem statement is first modeled
using the Gherkin language. The code also adopts a domain-driven
style using the Python programming language.

Two levels of modeling are adopted: system level and domain level,
each level has its own Gherkin specification.

The system level the behavior is described as a text-oriented input
and output. This behavior verifies that the solution can be accepted
by URI Online Judge.

For the domain level, the behavior description adopts a more conceptual
style, independent of a system interface. This second level adds a
separation of concerns between boundary and model.


Testing this solution
---------------------

Clone this repository:

```
$ git clone https://github.com/gherkin-by-example/python-behave
$ cd python-behave
```

This project requires [behave], and you can install using your
operating system package manager, or through `pip`. If using `pip`
it is recommended that you use a virtual environment:

```
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install behave
```
On some Python installations you could try:

```
$ python3 -m pip install behave
```

With everything in place you can run the whole test suite with:

```
$ behave
```

---
[behave]: https://behave.readthedocs.io
