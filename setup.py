import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="Proyecto2-Figuras",
    version="1.0.0",
    description="Project that identify figures",
    long_description=long_description,
    url="https://github.com/laudima/Proyecto2-Figuras",
    packages=setuptools.find_packages(),
    python_requires=">=3.7, <4",
    install_requires=["opencv-python","scipy"]
)
