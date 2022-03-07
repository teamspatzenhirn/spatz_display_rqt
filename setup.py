import subprocess
import sys

from setuptools import setup
import setuptools.command.build_py

package_name = 'spatz_display_rqt'

# List of all .proto files
proto_dir = "external/protobuf_types"
proto_src = [proto_dir + '/container.proto',
             proto_dir + '/controlstate.proto',
             proto_dir + '/hwhealth.proto',
             proto_dir + '/lights.proto',
             proto_dir + '/sensor.proto',
             proto_dir + '/setpoint.proto',
             proto_dir + '/time.proto',
             proto_dir + '/util.proto']
proto_dest_dir = "src/spatz_display_rqt/generated"


class BuildWithProtoBuf(setuptools.command.build_py.build_py):
    def run(self):
        sys.stderr.write("Running protoc generation")
        for proto_file in proto_src:
            subprocess.run(["protoc", f"-I={proto_dir}", f"--python_out={proto_dest_dir}", f"{proto_file}"])
        setuptools.command.build_py.build_py.run(self)


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, package_name + ".generated"],
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
    cmdclass={
        'build_py': BuildWithProtoBuf,
    },
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
