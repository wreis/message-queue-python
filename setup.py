import setuptools
import message_queue

setuptools.setup(
    name='message-queue',
    version='0.1.5',
    description='Message Queue',
    long_description='Message Queue python library to publish and subscribe to queues with diferent types of adapters.',
    url='https://github.com/ingresse/message-queue-python',
    author='Ingresse',
    author_email='vitor.leal@ingresse.com',
    license='BSD',
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt').read(),
    download_url = 'https://github.com/ingresse/message-queue-python/tarball/0.1.5',
    zip_safe=True,
)

