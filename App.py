import argparse


def pri(username):
    print(username)
    password = input("Enter your password: \n")
    import log
    log.connect(username=username, password=password)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="uims-firewall-authenticator")
    parser.add_argument(
        'login',
        metavar='L',
        type=str,
        nargs='+',
        help="Login into your uims account"
    )
    args = parser.parse_args()
    pri(args.login[0])
