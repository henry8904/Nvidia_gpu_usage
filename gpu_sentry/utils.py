import argparse

def arg_parser():
    parser = argparse.ArgumentParser(description = "gpu_sentry_client")

    parser.add_argument('--codename', required=False, help = "enter the codeName")
    parser.add_argument('--name', required=False, help = "enter the name that visualize on server ")
    parser.add_argument('--hostname', required=False, help="hostname")
    parser.add_argument("-m", "--mode", required=True, type=str,
                    help="Select client- or server-side mode.")

    return parser
