from sys import version
from setuptools import setup

setup(
	name = 'commands',
	version = '0.1.0',
	packages = ['commands'],
	entry_points = {
		'console_scripts': [
			'gitc = commands.__main__:main'
		]
	}
)