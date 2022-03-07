from setuptools import setup

package_name = 'spatz_display_rqt'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name + '/resource',
         ['resource/display.ui']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jonas Otto',
    maintainer_email='jonas@jonasotto.com',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spatz_display_rqt = ' + package_name + '.main:main',
        ],
    },
)
