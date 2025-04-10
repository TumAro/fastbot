from setuptools import setup, find_packages

setup(
    name="fastbot",
    version="0.1.0",
    description="A beginner-friendly 2D robotics simulation library",
    author="Tumin",
    author_email="contact.tumins@gmail.com",
    url="https://github.com/tumaro/fastbot",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pygame>=2.1.0",
        "pymunk>=6.2.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.1.0",
            "flake8>=4.0.1",
            "twine>=4.0.0",
        ],
    },
)