# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Live tests.

## [0.2.1][0.2.0] - 2021-04-29

### Added

- First version published to pypi. Mostly done some polishing. It is now possible to specify you periods as a mixed list of `str` and `int` in the `get_market_ohlc` method, if you so wish.

## [0.2.0][0.2.0] - 2021-04-16

### Added

- Typing information on both resources and REST client.

### Changed

- Made `pycwatch.rest.RestAPI.update_allowance` and `pycwatch.rest.RestAPI.perform_request` private methods.

## [0.1.1][0.1.1] - 2020-12-19

### Added

- Remaining tests for the main API client.
- Better README with quick start instructions.
- This changelog.

### Changed

- `rest.perform_request` does not raise an `APIError` anymore when no key is set, but puts a debug message into log.

## [0.1.0][0.1.0] - 2020-09-24

### Added

- Tests for the HTTP client, resources, and basic ones for API client.

## [0.0.1][0.0.1] - 2020-09-15

### Added

- Initial version with support for all resources defined by the Cryptowat.ch REST API.

The format of this file is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

[unreleased]: https://github.com/iuvbio/pycwatch/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/iuvbio/pycwatch/compare/v0.1.1...0.2.0
[0.1.1]: https://github.com/iuvbio/pycwatch/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/iuvbio/pycwatch/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/iuvbio/pycwatch/releases/tag/v0.0.1
