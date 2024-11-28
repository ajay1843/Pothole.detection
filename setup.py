 from setuptools import setup, find_packages

setup(
    name='PotholeDetection',          # Name of your project
    version='0.1',                   # Version number
    packages=find_packages(),         # Automatically find packages in the directory
    install_requires=[                # List of dependencies
        'numpy',
        'opencv-python',
        'torch>=1.7.0',
        'torchvision>=0.8.1',
        'matplotlib',
        'gdown',
    ],
    description='Pothole detection using YOLOv3 and YOLOv4.',  # Brief description
    author='Ajay',              # Your name
    author_email='asg176418@gmail',  # Your email address
    url='https://github.com/yourusername/PotholeDetection_YOLOv3_YOLOv4',  # URL to your GitHub repo
)
