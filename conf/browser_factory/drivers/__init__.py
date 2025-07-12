from importlib import import_module, resources

BROWSERS = dict()


def register_browser(func):
    """Decorator to register browser"""
    name = func.__name__
    BROWSERS[name] = func
    return func


def __getattr__(name):
    """Return browser"""
    try:
        return BROWSERS[name]
    except KeyError:
        _import_plugins()
        if name in BROWSERS:
            return BROWSERS[name]
        else:
            raise AttributeError(
                f"module {__name__!r} has no attribute {name!r}"
            ) from None


def __dir__():
    """List available browsers"""
    _import_plugins()
    return list(BROWSERS.keys())


def _import_plugins():
    """Import all resources to register browsers"""
    for name in resources.contents(__name__):
        if name.endswith(".py"):
            import_module(f"{__name__}.{name[:-3]}")
