from lib import utils


if __name__ == "__main__":
    print('CICD')

    try:
        assert utils.add(1, 1) == 2, "Should be 2"
        print('success')
    except:
        print('error')