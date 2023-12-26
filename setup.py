from setuptools import setup

setup(
    name='vishwapkg',
    version='0.1.0',    
    description='A example Python package',
    url='',
    author='Vishwajeet Thakur',
    author_email='vishwajeeththakur@gmail.com',
    license='BSD 2-clause',
    packages=['vishwapkg'],
    install_requires=['numpy',
                      'pandas',  
                      'dotenv'                   
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)