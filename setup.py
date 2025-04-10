from setuptools import setup, find_packages

setup(
    name="fastbot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.0.0",
        "pymunk>=6.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
        ],
    },
    author="TumAro",
    author_email="contact.tumins@gmail.com",
    description="A simple 2D robot simulation framework",
    keywords="robotics, simulation, education",
    url="https://github.com/tumaro/fastbot",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
    ],
)