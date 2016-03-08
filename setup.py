import setuptools

setuptools.setup(
    name='amqp-python',
    version='1.0.0',
    description='Mixin for publishing events to RabbitMQ',
    long_description=open('readme.md').read(),
    url='https://github.com/ingresse/amqp-python',
    author='Vitor Leal',
    author_email='vitor.leal@ingresse.com',
    license='MIT',
    packages=setuptools.find_packages(),
    namespace_packages=['amqp'],
    install_requires=open('requirements.txt').read(),
    zip_safe=True)

