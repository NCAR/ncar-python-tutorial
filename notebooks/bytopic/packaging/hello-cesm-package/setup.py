"""The setup script."""


from setuptools import setup

install_requires = [
    "xarray",
    "numpy",
    "matplotlib",
]  # Whatever third-party libraries are required to use our package.


long_description = """
CESM data analysis package as an example of a
python package from pre-existing code
"""

setup(
    author="Alice Doe",
    author_email="alice@example.com",
    description="My CESM analysis package",
    install_requires=install_requires,
    license="MIT",
    long_description=long_description,
    keywords="ocean modeling",
    name="cesm-package",
    packages=["cesm_package"],
    url="https://github.com/github-user-name/project-name",
    version="0.1",
    zip_safe=False,
)
