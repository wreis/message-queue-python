import setuptools

setuptools.setup(
    name='message-queue',
    version='1.0.0',
    description='Message Queue library',
    long_description=open('readme.md').read(),
    url='https://github.com/ingresse/mq-python',
    author='Ingresse',
    author_email='vitor.leal@ingresse.com',
    license='BSD',
    packages=setuptools.find_packages(),
    namespace_packages=['message_queue'],
    install_requires=open('requirements.txt').read(),
    zip_safe=True)

