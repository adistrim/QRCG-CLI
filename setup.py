from setuptools import setup, find_packages

setup(
    name="qr_code_generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "qrcode[pil]",
        "Pillow"
    ],
    entry_points={
        "console_scripts": [
            "qr_code_generator=qr_code_generator.main:main",
        ]
    }
)
