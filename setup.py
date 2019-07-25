import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='pwntools-r2-tmux',
    version='0.1.3.3.7',
    scripts=['pwntools-gdb'] ,
    author="ps1337 / @CaptnBanana",
    author_email="ps1337@mailbox.org",
    description="Debug exploits with Radare2 in pwntools and tmux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ps1337/pwntools_r2_tmux",
    install_requires=["r2pipe", "pwntools"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
