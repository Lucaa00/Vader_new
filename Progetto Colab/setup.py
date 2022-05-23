from setuptools import setup, find_packages

extra_math = [
    'returns-decorator',
]

extra_bin = [
    *extra_math,
]

extra_test = [
    *extra_math,
    'pytest>=4',
    'pytest-cov>=2',
]
extra_dev = [
    *extra_test,
]

extra_ci = [
    *extra_test,
    'python-coveralls',
]

setup(
    name='Progetto Colab',
    version=1.0,
    description='Pacchetto contentente 4 dizionari che fungono da miglioramento di Vader per argomanti specifici, quali recensioni di cibi, finanza, recensioni Disneyland e recensioni di prodotti elettronici. Il pacchetto è creato a partire da quello cjhutto (https://github.com/cjhutto/vaderSentiment)',

    url='https://github.com/MichaelKim0407/tutorial-pip-package',
    author='Vittorio Haardt, Luca Porcelli, Riccardo Fossato',
    author_email='vittoriohaardt@gmail.com, l.porcelli@campus.unimib.it, r.fossato@campus.unimib.it',
    keywords = ['vader', 'sentiment', 'analysis', 'opinion', 'mining', 'nlp', 'text', 'data',
              'text analysis', 'opinion analysis', 'sentiment analysis', 'text mining', 'twitter sentiment',
              'opinion mining', 'social media', 'twitter', 'social', 'media'],

    packages=find_packages(),

    extras_require={
        'math': extra_math,

        'bin': extra_bin,

        'test': extra_test,
        'dev': extra_dev,

        'ci': extra_ci,
    },

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
