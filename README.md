<!--- Generated by scripts/configure.py --->
[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

# Reactive collections for Hookless

[![Maven Central](https://img.shields.io/maven-central/v/com.machinezoo.hookless/hookless-collections)](https://search.maven.org/artifact/com.machinezoo.hookless/hookless-collections)
[![Build status](https://github.com/robertvazan/hookless-collections/workflows/build/badge.svg)](https://github.com/robertvazan/hookless-collections/actions/workflows/build.yml)
[![Test coverage](https://codecov.io/gh/robertvazan/hookless-collections/branch/master/graph/badge.svg)](https://codecov.io/gh/robertvazan/hookless-collections)

Reactive collections as implemented in [`ReactiveCollections`](https://hookless.machinezoo.com/javadocs/core/com.machinezoo.hookless/com/machinezoo/hookless/util/ReactiveCollections.html) class
are [reactive adapters](https://hookless.machinezoo.com/adapters) for Java collections.
Reactive collections wrap Java collections and turn them into reactive data source as long as all accesses are mediated by the wrapper.
Reactive collections will wake up dependent reactive computations whenever relevant write is made to the collection.

More on [homepage](https://hookless.machinezoo.com/collections).

## Status

Experimental. [Stagean](https://stagean.machinezoo.com/) is used to track progress on class and method level.

## Getting started

See [homepage](https://hookless.machinezoo.com/collections).

## Documentation

* [Homepage](https://hookless.machinezoo.com/collections)
* [Javadoc](https://hookless.machinezoo.com/javadocs/collections/com.machinezoo.hookless.collections/com/machinezoo/hookless/collections/package-summary.html)

Some APIs are undocumented. You might have to peek in the [source code](src/main/java/com/machinezoo/hookless/collections).

## Feedback

Bug reports and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Distributed under [Apache License 2.0](LICENSE).
