import pkg_resources as _pkg_resources


def _parse_version():
    data = _pkg_resources.get_distribution('pysaml2')
    value = _pkg_resources.parse_version(data.version)
    return value


version_info = _parse_version()
version = str(version_info)
