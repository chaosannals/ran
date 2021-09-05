import setuptools
from ran import fs

setuptools.setup(
    name='ran',
    version='0.0.9',
    description='yet a library.',
    long_description=fs.load('readme.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/chenshenchao/ran',
    keywords='ran library',
    license='MIT',
    author='chenshenchao',
    author_email='chenshenchao@outlook.com',
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=setuptools.find_packages(),
)
