import setuptools
from pathlib import Path

HERE = Path(__file__).parent

README = (HERE / ".." / "README.md").read_text()

setuptools.setup(
	name="st_group_barchart",
	version="0.0.1",
	author="Mihai Blebea",
	author_email="mihaiserban.blebea@gmail.com",
	description="This package provides a group barchart component for Streamlit",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/MihaiBlebea/streamlit_group_barchart",
	packages=["st_group_barchart"],
	include_package_data=True,
	zip_safe=False,
	python_requires=">=3.6",
	install_requires=["streamlit >= 0.63"],
)
