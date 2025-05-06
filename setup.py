from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='ddnet_parser',
  version='1.0.0',
  author='neyxezz',
  author_email='bassboosthelp@gmail.com',
  description='Простой парсер данных с master1.ddnet.org и ddstats.tw',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/neyxezz/test',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: Public Domain',
    'Operating System :: OS Independent'
  ],
  keywords='ddnet_parser ddnet_master ddnet',
  project_urls={
    'Documentation': 'https://github.com/neyxezz/test/blob/main/docs/docs.md',
    'DDnet-Master': 'https://master1.ddnet.org/',
    'DDStats-TW': 'https://ddstats.tw/'
  },
  python_requires='>=3.7'
)
