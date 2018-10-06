import io

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-mock',
    'pytest-click',
    'pytest-pylint',
]

setup(
    name='Lektor',
    version='3.1.2',
    url='http://github.com/lektor/lektor/',
    description='A static content management system.',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='BSD',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Babel',
        'EXIFRead',
        'Flask',
        'Jinja2>=2.4',
        'click>=6.0',
        'functools32;python_version<"3.2.3"',
        'inifile',
        'mistune>=0.7.0',
        'pip',
        'python-slugify',
        'requests[security]',
        'setuptools',
        'watchdog',
    ],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'ipython': ['ipython'],
    },
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points='''
        [console_scripts]
        lektor=lektor.cli:main
    '''
)
