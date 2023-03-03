
def run_from_ipython() -> bool:
    try:
        __IPYTHON__
        return True
    except NameError:
        return False


run_from_ipython = run_from_ipython()


def run_from_colab():
    if not run_from_ipython:
        return False
    try:
        from google import colab
        return True
    except ImportError:
        return False


run_from_colab = run_from_colab()
