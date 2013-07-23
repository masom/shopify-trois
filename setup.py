"""
Shopify Trois
---------------

Shopify API for Python 3
"""

from setuptools import setup


setup(
    name='shopify-trois',
    version='1.1-dev',
    url='http://masom.github.io/shopify-trois',
    license='MIT',
    author='Martin Samson',
    author_email='pyrolian@gmail.com',
    maintainer='Martin Samson',
    maintainer_email='pyrolian@gmail.com',
    description='Shopify API for Python 3',
    long_description=__doc__,
    packages=[
        'shopify_trois', 'shopify_trois.models', 'shopify_trois.engines',
        'shopify_trois.engines.http'
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'requests>=1.2.3'
    ],
    test_suite='nose.collector',
    tests_require=[
        'pytest', 'nose', 'mock'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
