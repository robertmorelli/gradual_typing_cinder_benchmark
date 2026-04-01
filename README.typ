#set text(font: "Fira Mono")
= wtf does the detyper do
== definitions:
1. *intent*: a particular ast tree edit at a particular node.
2. *type category*: a place a type may appear like a parameter, function body assignment statement, or return annotation.
3. *type kind*: a classification of types that guides removal strategy. if the same removal strategy works for 2 types in all *categories* then they will be the same *kind*.
4. *category policy*: given a *category* and a *kind*, it is the set of *intents* which should result in the safe removal of an annotation.
5. *guide*: the guide is the set of functions which we intend to detype.

== File descriptions:
1. *rules.py*: contains a utility for determining what *kind* of type an annotation might be as well as the *category policies*
2. *tasks.py*: contains the *intent* definition, the functions which apply *intents*, the canonical unification of *intents*, and the detyper class itself which holds, systematically unifies and executes a set of *intents*.
3. *plan_data.py*: contains a primitive type unifier which handles only the `T` / `Optional[T]` case and fails on almost everything else, as well as a function which constructs metadata on each function and whether it is detyped according to the *guide*.
4. *pipeline.py*: orchestrates the detyping of a program. it has utilities for naming permutations, normalizing the ast, injecting imports, running the detyping of some source code and then writing the result.
5. *ast_utils.py*: contains utilities for finding ast nodes of interest including all function and method definitions, all function call sites, all method call sites, and all annotations of each *category* within a function.
6. *artifacts.py*: is a thin wrapper around utilities in *pipeline.py* which makes interfacing easier
7. *generators.py*: a set of utility functions each of which generate all *intents* for a given *context* and wrap them in *detyper* objects.
8. *main.py*: provides a cli interface for the utilities in *artifacts* and *pipeline* and resolves file system nonsense.
