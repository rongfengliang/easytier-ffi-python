from setuptools import setup,find_packages

setup(
    name="easytier",
    version="0.1.0",
    packages=["easytier"],
    setup_requires=["cffi>=1.17.1"],
    install_requires=["cffi>=1.17.1"],
    package_data={
        "easytier": ["lib/*.dylib", "lib/*.so","lib/*.dll"],
    },
    author="dalongrong",
    author_email="1141591465@qq.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS X",
        "Operating System :: POSIX",
    ],
    cffi_modules=["api_build.py:ffibuilder"],
    zip_safe=False,
)
