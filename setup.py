#-*- coding: utf-8 -*-
# ------ wuage.com testing team ---------
# __author__ : jianxing.wei@wuage.com

from setuptools import setup, find_packages

setup(
    name='dingchatbot',
    version='1.0.0.dev1',
    description='testing automation reporting ding message sdk, easy for using.',
    url='https://gitlab.wuage-inc.com/jianxing.wei/dingchatbot.git',
    author='Jianxing.wei',
    author_email='jianxing.wei@wuage.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='dingding post message sdk TAMessageAPI',
    packages=find_packages(),
    # packages=['com.wuage.testing.helper'],
)