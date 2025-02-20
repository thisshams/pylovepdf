from setuptools import setup


# def readme():
#     with open('README.md') as f:
#         return f.read()


setup(name='pylovepdf_flavor',
      version='1.3.3.4',
      description='ilovepdf.com python API library',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='pdf unlock compress manipulate edit protect pdftojpg jpgtopdf pdfa',
      url='https://github.com/AndyBTuttofare/pylovepdfhvjv',
      author='Andrea Bruschi',
      author_email='moonx2006@gmail.com',
      license='GNU GPLv3',
      packages=['pylovepdf_flavor', 'pylovepdf_flavor.tools'],
      # data_files=[('pylovepdf/samples', ['*.py'])],
      install_requires=['requests', 'urllib3'],
      include_package_data=True)
