from setuptools import setup


with open('readme.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='Filish Storage',
    license='MIT',
    author='Nikolay Oceean',
    description='No yet',
    long_description=readme,
    packages=['filish_storage'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        # Nothing yet
    ],
    # entry_points={
    #     'console_scripts': [
    #         'filish = filish:cli',
    #     ],
    # },
)