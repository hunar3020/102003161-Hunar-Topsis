import setuptools
setuptools.setup(
  name = '102003161-Hunar-Topsis',         
  packages = ['102003161-Hunar-Topsis'],  
  version = '0.1',      
  license='MIT',        
  description = 'A Python package to find TOPSIS for multi-criteria decision analysis method',   
  author_email = 'Hhunar_be20@thapar.edu',         
  keywords = ['TOPSIS','TIET'],   
  install_requires=[            
          'pandas',
          'tabulate',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)