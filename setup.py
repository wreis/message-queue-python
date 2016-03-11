import setuptools

setuptools.setup(
    name='message-queue',
    version='0.1.0',
    description='Message Queue',
    long_description=open('readme.md').read(),
    url='https://github.com/ingresse/message-queue-python',
    author='Ingresse',
    author_email='vitor.leal@ingresse.com',
    license='BSD',
    packages=setuptools.find_packages(),
    namespace_packages=['message_queue'],
    install_requires=open('requirements.txt').read(),
    zip_safe=True
)

