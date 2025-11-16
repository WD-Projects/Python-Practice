def outer():
    def inner():
        print("I am inner function")
    return inner

f = outer()
f()        # calls inner()

'''
Step A — lines 1–2 (def fun1(): ...)

Python creates a function object for fun1 and binds the name fun1 to that object in the current module’s namespace.

Important: the body (print("I am fun1")) does NOT run now. def only creates the function object.

State after line 2 (conceptually):

fun1 → <function fun1> (a callable object)

Step B — lines 3–4 (def outer(): ...)

Python creates another function object for outer and binds the name outer to it.

outer contains code that, when executed later, will return fun1.

State after line 4:

fun1 → <function fun1>

outer → <function outer>

Nothing printed yet.

What happens at runtime (when code executes further)

Line 5: x = outer() — call outer

The interpreter calls the function object bound to outer.

Entering outer:

Its body executes return fun1.

fun1 inside outer refers to the function object we created earlier.

outer() returns that function object (it does not call fun1; it just returns it).

The returned function object is assigned to the name x.

State after line 5:

fun1 → <function fun1>

outer → <function outer>

x → <function fun1> (so x and fun1 point to the same function object)

No printing happened yet because fun1 was not executed.

Line 6: x() — call what x refers to

x currently refers to the function object <function fun1>.

x() calls that function object — equivalent to calling fun1().

Inside fun1, Python runs print("I am fun1").

The interpreter prints:
'''