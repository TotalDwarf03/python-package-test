# python-package-test
A repository to test using pip to import python packages from GitHub

## Write Up
The project requires a folder structure as shown in the project.

```
repository_folder/
    
    module1_name/
        __init__.py
    
    module2_name/
        __init__.py
    
    setup.py
```

With this setup, we can focus on ```setup.py```

setup.py contains information about how this package is setup.

```python
from setuptools import setup

setup(
    name='my_package',
    version='0.0.1',
    description='My package from github repo',
    url='git@github.com:TotalDwarf03/python-package-test.git',
    author='Kieran Pritchard',
    author_email='blablabla@gmail.com'
    license='unlicense',
    packages=['module1_name', 'module2_name'],
    zip_safe=False
)
```

The priority in this file is setting the name, version, url, author and packages.

Once this package is setup and pushed to GH, we can install it into any projects using 

```
pip install git+<github_repository_url>
```

example for this repository:

```
pip install git+https://github.com/TotalDwarf03/python-package-test.git
```

Once installed, you can import the package as normal.

```python
import module1_name as m1
import module2_name as m2
```

## Adding package to poetry

Run the following:

```
poetry add git+<github_repository_url>
```

example for this repository:

```
poetry add git+https://github.com/TotalDwarf03/python-package-test.git
```

### Debugging
When initially trying this, I had the following error:

HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /TotalDwarf03/python-package-test.git/info/refs?service=git-upload-pack (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)')))

To fix this on MacOS, I had to go to ```Application > Python folder``` then double click on Install Certificates.command file as suggested in [this](https://stackoverflow.com/questions/69814872/i-receive-ssl-certificate-verify-failed-when-doing-poetry-install) Stack Overflow thread.

## References
- [Video Summary](https://www.youtube.com/watch?v=r-wwMk5faXo)
- [Detailed Blog](https://dev.to/rf_schubert/how-to-create-a-pip-package-and-host-on-private-github-repo-58pa)
