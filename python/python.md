2024-04-06

Python links
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)
- [Modern Python Developer Toolkit](https://pycon.switowski.com/)
- [Python Tips Book](https://book.pythontips.com/en/latest/index.htm)
	1. *args and **kwargs
	```
	def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

	test_var_args('yasoob', 'python', 'eggs', 'test')


	def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

	greet_me(name="yasoob")
	
	```
	
	2. Debugging
	breakpoint() builtin function
	pdb package
	--system-site-packages