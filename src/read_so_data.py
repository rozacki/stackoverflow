import xml.etree.ElementTree as et
import argparse
import logging


def _filter_post(xml_line, tag):
    try:
        root = et.fromstring(xml_line)
    except Exception as ex:
        logging.error(f'Exception {ex}, xml line `{xml_line}`')
        return None

    tags = root.get('Tags')
    if tags and tag:
        if tag in tags:
            return xml_line
    return None


def count(file, tag):
    count = 0
    with open(file) as f:
        f.readline()
        f.readline()
        for line in f:
            if _filter_post(line, tag):
                count = count + 1

    print(count)


def filter_posts(file, tag):
    '''
    '''
    with open(file) as f:
        f.readline()
        f.readline()
        for line in f:
            if _filter_post(line, tag):
                print(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', default='filter-tags')
    parser.add_argument('--file', required=True)
    parser.add_argument('--tag')
    args = parser.parse_args()

    if args.action == 'filter-tags':
        filter_posts(args.file, args.tag)
    elif args.action == 'count':
        count(args.file, args.tag)
