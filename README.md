# tink-python-api-types
[![tag](https://img.shields.io/github/tag/namelivia/tink-python-api-types.svg)](https://github.com/namelivia/tink-python-api-types/releases) [![build](https://github.com/namelivia/tink-python-api-types/actions/workflows/build.yml/badge.svg)](https://github.com/namelivia/tink-python-api-types/actions/workflows/build.yml) [![codecov](https://codecov.io/gh/namelivia/tink-python-api-types/branch/main/graph/badge.svg?token=NlsLE3qD4V)](https://codecov.io/gh/namelivia/tink-python-api-types)
 [![Lint](https://github.com/namelivia/tink-python-api-types/actions/workflows/black.yml/badge.svg)](https://github.com/namelivia/tink-python-api-types/actions/workflows/black.yml)

## About
Python types for the Tink API entities.

## Installation

This package is hosted on [PyPi](https://pypi.org/project/tink-python-api-types), you can install it using any python package manager. 

```bash
$ pip install tink-python-api-types
```

## License

[MIT](LICENSE)

## Contributing
Any suggestion, bug reports, prs or any other kind enhacements are welcome. Just [open an issue first](https://github.com/namelivia/tink-python-api-types/issues/new), for creating a PR remember this project has linting checkings and unit tests so any PR should comply with both before beign merged, this checks will be automatically applied when opening or modifying the PRs.

## Local development

This project comes with a `docker-compose.yml` file so if you use Docker and docker-compose you can develop without installing anything on your local environment. Just run `docker-compose up --build` for the first time to setup the container and launch the tests. Pytest is configured as the entrypoint so just run `docker-compose up` everytime you want the tests to execute on the Dockerized Python development container.
