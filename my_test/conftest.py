def pytest_addoption(parser):
    parser.addoption('--os-name', default='Linux', help='os name')
