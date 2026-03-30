from setuptools import find_packages, setup

package_name = 'first_ros_ques'

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
    maintainer='anish-vikranth',
    maintainer_email='anish-vikranth@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'no1=first_ros_ques.count_node:main',
            'no2=first_ros_ques.number_node:main'
        ],
    },
)
