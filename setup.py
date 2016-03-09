import setuptools

setuptools.setup(
    name='amqp-python',
    version='1.0.0',
    description='RabbitMQ client',
    long_description=open('readme.md').read(),
    url='https://github.com/ingresse/amqp-python',
    author='Ingresse',
    author_email='vitor.leal@ingresse.com',
    license='BSD',
    packages=setuptools.find_packages(),
    namespace_packages=['amqp'],
    install_requires=open('requirements.txt').read(),
    zip_safe=True)

