from setuptools import find_packages, setup

package_name = 'add_integers'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sandeep',
    maintainer_email='sandeep@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'add_integers_service = add_integers.service_node:main',
          'add_integers_client = add_integers.client_node:main',
        ],
    },
)
