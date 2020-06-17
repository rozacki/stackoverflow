import xml.etree.ElementTree as et
import argparse
import logging
import psycopg2
import xml.etree.ElementTree as et


def _get_dictionary(xml_line):
    '''
       - Id
       - PostTypeId
          - 1: Question
          - 2: Answer
       - ParentID (only present if PostTypeId is 2)
       - AcceptedAnswerId (only present if PostTypeId is 1)
       - CreationDate
       - Score
       - ViewCount
       - Body
       - OwnerUserId
       - LastEditorUserId
       - LastEditorDisplayName="Jeff Atwood"
       - LastEditDate="2009-03-05T22:28:34.823"
       - LastActivityDate="2009-03-11T12:51:01.480"
       - CommunityOwnedDate="2009-03-11T12:51:01.480"
       - ClosedDate="2009-03-11T12:51:01.480"
       - Title=
       - Tags=
       - AnswerCount
       - CommentCount
       - FavoriteCount
    :param xml_line:
    :return:
    '''
    try:
        root = et.fromstring(xml_line)
    except Exception as ex:
        logging.error(f'Exception {ex}, xml line `{xml_line}`')
        return None

    return { 'id': root.get('Id'),
    'post_type' : root.get('PostTypeId'),
    'parent_id' : root.get('ParentID'),
    'accepted_answer_id' : root.get('AcceptedAnswerId'),
    'creation_date' : root.get('CreationDate'),
    'score' : root.get('Score'),
    'view_count' : root.get('ViewCount'),
    'body' : root.get('Body'),
    'owner_user_id' : root.get('OwnerUserId'),
    'last_editor_user_id' : root.get('LastEditorUserId'),
    'last_editor_display_name' : root.get('LastEditorDisplayName'),
    'last_edit_date' : root.get('LastEditDate'),
    'last_activity_date' : root.get('LastActivityDate'),
    'community_owned_date' : root.get('CommunityOwnedDate'),
    'close_date' : root.get('ClosedDate'),
    'title' : root.get('Title'),
    'answer_count' : root.get('AnswerCount'),
    'comment_count' : root.get('CommentCount'),
    'favorite_count' : root.get('FavoriteCount')
}


def get(file):
    '''
    '''
    with open(file) as f:
        for line in f:
            row = _get_dictionary(line)
            if row:
                print(row)


if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    args = parser.parse_args()
    get(args.file)