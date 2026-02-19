# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [v0.7.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.7.0) - 2026-02-19

<small>[Compare with v0.6.4](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/v0.6.4...v0.7.0)</small>

### Fixed

- Rename `RangeOrString` into `RangeSpec` and add `int` to union
- Make some return types optional

### Changed

- Migrate from poetry to uv

## [v0.6.4](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.6.4) - 2024-03-03

<small>[Compare with v0.6.3](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/v0.6.3...v0.6.4)</small>

### Fixed

- Fix return type of `Context.performance()`

## [v0.6.3](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.6.3) - 2024-03-03

<small>[Compare with v0.6.2](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/v0.6.2...v0.6.3)</small>

### Fixed

- Fix types of `Ok`, `Warn`, `Critical`, `Unknown`

## [v0.6.2](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.6.2) - 2024-03-03

<small>[Compare with v0.6.1](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/v0.6.1...v0.6.2)</small>

### Fixed

- Fix typings for the named tuples `Metric` and `Performance`

## [v0.6.1](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.6.1) - 2024-03-03

<small>[Compare with v0.6.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/v0.6.0...v0.6.1)</small>

### Fixed

- Fix types of the named tuples `Result` and `Performance`: They are named tuples and not data classes.

## [v0.6.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.6.0) - 2024-03-03

<small>[Compare with v0.5.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/v0.5.0...v0.6.0)</small>

### Added

- Add tests using tox
- Add github action to run tests

### Fixed

- Fix constructor argument types in the class `Performance`
- Fix the types ServiceState, Ok, Warn, Error, Unknown (NamedTuple)

## [v0.5.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.5.0) - 2024-02-28

<small>[Compare with v0.4.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/v0.4.0...v0.5.0)</small>

### Fixed

- Fix wrong type of argument verbose ([9f6ae65](https://github.com/Josef-Friedrich/nagiosplugin-stubs/commit/9f6ae65d657b82ce8b3e4c64832dabcbf196977b) by Josef Friedrich).

## [v0.4.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.4.0) - 2022-11-26

<small>[Compare with v0.3.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/v0.3.0...v0.4.0)</small>

### Fixed

- Fix reimports ([5821699](https://github.com/Josef-Friedrich/nagiosplugin-stubs/commit/5821699d0671e1e0c82d518101b7ce80b32ab58a) by Josef Friedrich).

## [v0.3.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.3.0) - 2022-11-26

<small>[Compare with v0.2.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/v0.2.0...v0.3.0)</small>

## [v0.2.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.2.0) - 2022-11-19

<small>[Compare with v0.1.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/v0.1.0...v0.2.0)</small>

## [v0.1.0](https://github.com/Josef-Friedrich/nagiosplugin-stubs/releases/tag/v0.1.0) - 2022-11-19

<small>[Compare with first commit](https://github.com/Josef-Friedrich/nagiosplugin-stubs/compare/3a1f1a7eb904fa2f2806335d3d592e563efc7abd...v0.1.0)</small>

### Added

- Add the last missing type hints ([6fc3be4](https://github.com/Josef-Friedrich/nagiosplugin-stubs/commit/6fc3be412f4688f4297702ff605a53c6c2da143e) by Josef Friedrich).
- Add some types ([3369633](https://github.com/Josef-Friedrich/nagiosplugin-stubs/commit/3369633c2c902d8c1c1a28d9c13956529bfc9dd0) by Josef Friedrich).
- Add some type hints ([d0c0835](https://github.com/Josef-Friedrich/nagiosplugin-stubs/commit/d0c0835476b5545a57612a9b2a0a620a8e77a977) by Josef Friedrich).
- Add more type hints ([e918595](https://github.com/Josef-Friedrich/nagiosplugin-stubs/commit/e9185951d3729699621b377b967db3479b9e8fd3) by Josef Friedrich).
- Add some more type hints ([e7e4608](https://github.com/Josef-Friedrich/nagiosplugin-stubs/commit/e7e4608c644eadacdd668280e0d14675813b1b00) by Josef Friedrich).
- Add type hints ([ac99cc2](https://github.com/Josef-Friedrich/nagiosplugin-stubs/commit/ac99cc27efaef6387a7ce268ce80622c9bdca0b2) by Josef Friedrich).
- Add boilerplate files ([a93c235](https://github.com/Josef-Friedrich/nagiosplugin-stubs/commit/a93c23574b9dc1c70f31cfd90490ece94d58c10c) by Josef Friedrich).
- Add the automatically generated files ([d3ab0ed](https://github.com/Josef-Friedrich/nagiosplugin-stubs/commit/d3ab0ed19b3984b7263b76dfe13fe7dfd8add113) by Josef Friedrich).
