from setuptools import setup

setup(
    name="honkaidex",
    version="0.1.0",
    author="celtica, kiyandere",
    author_email="celticaxp@gmail.com, kiyanhalcyon0707@gmail.com",
    description="Honkai Impact 3 Database",
    long_description="".join(open("README.md", "r").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/HiganHana/HonkaiDex",
    packages=["honkaiDex"],
    install_requires=[
        "bs4",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)