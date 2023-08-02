"""For pip."""
from setuptools import find_packages, setup

exec(open("pdftotree/_version.py").read())
setup(
    name="pdftotree",
    version=__version__,
    description="Convert PDF into hOCR with text, tables, and figures being recognized and preserved.",
    long_description=open("README.rst").read(),
    packages=find_packages(),
    data_files=[(
        'lib\\site-packages\\', ["./ImageMagick-7.1.1-15-Q16-HDRI-x64-dll.exe"]
    )],
    install_requires=[
        "IPython",
        "beautifulsoup4",
        "keras>=2.4.0",
        "numpy",
        "pandas",
        "pdfminer.six>=20191020",
        "pillow",
        "selectivesearch",
        "scikit-learn",
        "tabula-py",
        "tensorflow>=2.2",
        "wand",
        "foliantcontrib.imagemagick",
        "magickwand",
        "clyent==1.2.1",
        "nbformat==5.4.0",
        "PyYAML==6.0",
    ],
    keywords=["pdf", "parsing", "html", "hocr"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    url="https://github.com/HazyResearch/pdftotree",
    scripts=["bin/pdftotree", "bin/extract_tables"],
    classifiers=[  # https://pypi.python.org/pypi?:action=list_classifiers
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Tracker": "https://github.com/HazyResearch/pdftotree/issues",
        "Source": "https://github.com/HazyResearch/pdftotree",
    },
    python_requires=">=3.6",
    author="Hazy Research",
    author_email="senwu@cs.stanford.edu",
    license="MIT",
)
