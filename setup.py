from setuptools import setup, find_packages

setup(name='Distutils',
      version='0.1',
      description='Inside Python',
      # author='Foo Bar, Spam Eggs',
      # author_email='foobar@baz.com, spameggs@joe.org',
      author='Roman Potashow',
      author_email='justgook@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      packages = find_packages(),
      scripts = ['say_hello.py'],
      # Project uses reStructuredText, so ensure that the docutils get
      # installed or upgraded on the target machine
      install_requires = ['docutils>=0.3'],
      package_data = {
          # If any package contains *.txt or *.rst files, include them:
          '': ['*.txt', '*.rst'],
          # And include any *.msg files found in the 'hello' package, too:
          'hello': ['*.msg'],
      },
     )