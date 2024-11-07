from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here, for example:
        # 'numpy', 'requests'
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',  # If you want to make it a CLI tool
        ],
    },
)
