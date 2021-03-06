from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Ubuntu',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ZAPZAPPY',
  version='0.0.1',
  description='zapzappy is a simple Whatsapp API',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Lucas Ribeiro',
  author_email='Lucas Ribeiro',
  license='MIT', 
  classifiers=classifiers,
  keywords='Whatsapp API', 
  packages=find_packages(),
  install_requires=[''] 
)