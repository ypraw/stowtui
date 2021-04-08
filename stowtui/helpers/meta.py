import pkg_resources
import importlib.metadata as stowMeta


def Version():
    """Get Version From Dist Folder

    Returns:
        version : current version
    """
    version = ''
    try:
        version = pkg_resources.require('stowtui')[0].version
    except Exception as e:    # pragma: no cover
        version = 'Error: ' + str(e)
    return version


def Author():
    """Get Author From Dist Folder

    Returns:
        Author : Author Name
    """
    author = ''
    try:
        author = stowMeta.metadata('stowtui')['Author']
    except Exception as e:
        author = 'Error: ' + str(e)
    return author


def Email():
    """Get Author Email From Dist Folder

    Returns:
        Email : Author Email
    """
    email = ''
    try:
        email = stowMeta.metadata('stowtui')['Author-email']
    except Exception as e:
        email = 'Error: ' + str(e)
    return email


def app_name():
    """Get App Name

    Returns:
        Name : App Name
    """
    app_name = ''
    try:
        app_name = stowMeta.metadata('stowtui')['Name']
    except Exception as e:
        app_name = 'Error: ' + str(e)
    return app_name