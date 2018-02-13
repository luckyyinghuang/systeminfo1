from setuptools import setup
setup(name="systeminfo1",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Aonghus Lawlor",
      author_email="aonghua.lawlor@ucd.ie",
      licence="GPL3",
      packages=['systeminfo1'],
      entry_points={'console_scripts':
                    ['comp30670_systeminfo1=systeminfo.main:main'] 
                    },
      
          )
        