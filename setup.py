import os
from setuptools import setup

import django_bootstrap


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


package_dir = 'django_bootstrap'

packages = []
for dirpath, dirnames, filenames in os.walk(package_dir):
    # ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
        
template_patterns = [
    'templates/*.html',
    'templates/*/*.html',
    'templates/*/*/*.html'
]

package_data = dict(
    (package_name, template_patterns)
    for package_name in packages
)

setup(
    name='django-bootstrap-mega',
    description='Twitter Bootstrap ready Django forms.',
    long_description=read('README.mkd'),
    author='Chris Spencer',
    packages=['django_bootstrap'],
    package_data=package_data,
    version=django_bootstrap.__version__,
    url='http://github.com/chrisspen/django-bootstrap',
    keywords=[],
    license='Apache 2.0',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Topic :: Internet :: WWW/HTTP :: WSGI',
      'Framework :: Django'
    ],
    zip_safe=False,
    install_requires=['Django>=1.10']
)
