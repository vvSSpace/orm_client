from distutils.core import setup

REQUIRES = [
    'structlog~=23.1.0',
    'allure-pytest',
    'records~=0.5.3',
    'SQLAlchemy~=1.4.46'
]

setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/vvSSpace/orm_client.git',
    license='MIT',
    author='Vyacheslav Sevastyanov',
    author_email='-',
    install_requires=REQUIRES,
    description='ORM client with allure and logger'
)
