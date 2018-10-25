from setuptools import setup, find_packages
setup(
	name='read-ATM2-icessn',
	version='1.0.0.2',
	description='Reads Level-2 Airborne Topographic Mapper (ATM) Icessn Elevation, Slope, and Roughness data products',
	url='https://github.com/tsutterley/read-ATM2-icessn',
	author='Tyler Sutterley',
	author_email='tyler.c.sutterley@nasa.gov',
	license='MIT',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Physics',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
	],
	keywords='NSIDC IceBridge ILATM2 Icessn',
	packages=find_packages(),
	install_requires=['numpy'],
)
