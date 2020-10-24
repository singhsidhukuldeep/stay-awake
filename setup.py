from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Programming Language :: Python :: 3'
]

setup(
    name='stay-awake',
    version='0.1',
    description='Simple Platform Independent Python package to keep your system awake without affecting workflow!',
    long_description='Read more at https://github.com/singhsidhukuldeep/stay-awake',
    url='https://github.com/singhsidhukuldeep/stay-awake',
    author='Kuldeep Singh Sidhu',
    author_email='singhsidhukuldeep@gmail.com',
    classifiers=classifiers,
    keywords='stay awake',
    packages=find_packages(),
    install_requires=['pyautogui', 'tqdm'],
    zip_safe = False,
)