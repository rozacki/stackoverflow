'''
Was used to read data xml file and do some data mining
'''
import xml.etree.ElementTree as et
import argparse
import logging


def filter_post(xml_line, tag):
    try:
        root = et.fromstring(xml_line)
    except Exception as ex:
        logging.error(f'Exception {ex}, xml line `{xml_line}`')
        return None, None

    tags = root.get('Tags')
    if tags and tag:
        if tag in tags:
            return xml_line, tags
    return None, None


def count(file, tag):
    count = 0
    with open(file) as f:
        f.readline()
        f.readline()
        for line in f:
            _, line = filter_post(line, tag)
            if line:
                count = count + 1

    print(count)


def filter_posts_csv(file, tag):
    '''
    filters and writes to csv some attributes
    '''
    with open(file) as f:
        f.readline()
        f.readline()
        for line in f:
            line, tags = filter_post(line, tag)
            if line:
                print(','.join(tags))


def filter_posts(file, tag):
    '''
    '''
    with open(file) as f:
        f.readline()
        f.readline()
        for line in f:
            line, tags = filter_post(line, tag)
            if line:
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
    elif args.action == 'filter-tags-csv':
        filter_posts_csv(args.file, args.tag)
