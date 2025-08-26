from setuptools import setup, find_packages

with open("README.me", "r") as f:
  page_description = f.read()

with open("requirements.txt") as f:
  requirements = f.read()

setup(
  name="image_processing",
  version="0.0.1",
  author="author",
  author_email="author_email",
  description="Pacote para processamento de imagens",
  long_description=page_description,
  long_description_content_type="text/markdown",
  url="https://github.com/josuemarcos/image-processing-package",
  packages=find_packages(),
  install_requirements=requirements,
  python_requires='>3.8',
)
