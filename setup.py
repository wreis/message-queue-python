import setuptools

setuptools.setup(
    name='message-queue',
    version='0.1.6',
    description='Message Queue',
    long_description='Message Queue python library to publish and subscribe to queues with diferent types of adapters.',
    url='https://github.com/ingresse/message-queue-python',
    author='Ingresse',
    author_email='vitor.leal@ingresse.com',
    license='BSD',
    packages=setuptools.find_packages(),
    install_requires=['pika>=0.10.0'],
    download_url = 'https://github.com/ingresse/message-queue-python/tarball/0.1.6',
)

