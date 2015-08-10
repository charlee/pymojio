from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pymojio',
      version='0.1',
      description='A python SDK for moj.io',
      long_description='A python SDK for moj.io.',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries',
      ],
      keywords='mojio moj.io sdk',
      url='http://github.com/charlee/pymojio',
      author='Charlee Li',
      author_email='charlee@envisageny.com',
      license='MIT',
      packages=['pymojio'],
      install_requires=[
          'oauth2client',
          'requests==2.7.0',
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      
)

