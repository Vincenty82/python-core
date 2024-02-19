from setuptools import setup, find_packages

setup(
    name='Cleaner',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:clean_folder_start',
        ],
    },
)
