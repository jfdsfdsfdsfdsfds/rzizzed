from setuptools import setup

setup(
    name='PyRoxy',
    version="1.0b2",
    packages=['PyRoxy', 'PyRoxy.GeoIP', 'PyRoxy.Tools', 'PyRoxy.Exceptions'],
    url='https://github.com/MHProDev/PyRoxy',
    license='',
    author="MH_ProDev",
    author_email='',
    install_requires=["maxminddb>=2.2.0", "requests>=2.27.1", "yarl>=1.7.2", "pysocks>=1.7.1"],
    include_package_data=True,
    package_data={'PyRoxy.GeoIP.Sqlite':['*.txt', "GeoLite2-Country.mmdb"]},
    description=''
)
