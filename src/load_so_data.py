import xml.etree.ElementTree as et
import argparse
import logging
import psycopg2
import psycopg2.extras
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
    'post_type': root.get('PostTypeId'),
    'parent_id': root.get('ParentID'),
    'accepted_answer_id': root.get('AcceptedAnswerId'),
    'creation_date': root.get('CreationDate'),
    'score': root.get('Score'),
    'view_count': root.get('ViewCount'),
    'body': root.get('Body'),
    'owner_user_id': root.get('OwnerUserId'),
    'last_editor_user_id': root.get('LastEditorUserId'),
    'last_editor_display_name': root.get('LastEditorDisplayName'),
    'last_edit_date': root.get('LastEditDate'),
    'last_activity_date': root.get('LastActivityDate'),
    'community_owned_date': root.get('CommunityOwnedDate'),
    'close_date': root.get('ClosedDate'),
    'title': root.get('Title'),
    'answer_count': root.get('AnswerCount'),
    'comment_count': root.get('CommentCount'),
    'favorite_count': root.get('FavoriteCount')
    }


def _insert_into_postgres(cursor, table_name, tuples):
    sql=f'insert into {table_name}  values (%(id)s, %(post_type)s, %(parent_id)s, %(accepted_answer_id)s,' \
        f'%(creation_date)s, %(score), %(view_count)s, %(body),%(owner_user_id)s,%(last_editor_user_id)s,' \
        f'%(last_editor_display_name)s,%(last_edit_date)s,%(last_activity_date)s,%(community_owned_date)s,' \
        f'%(close_date)s,%(title)s,%(answer_count)s,%(comment_count)s,%(favorite_count)s)'
    psycopg2.extras.execute_batch(cursor, sql, tuples)


def insert_into_postgres_batches(file, batch_max_size=100):
    '''
    '''
    with psycopg2.connect('user=postgres dbname=stackoverflow') as conn:
        with conn.cursor() as cursor:
            with open(file) as f:
                batch_size = 0
                vals = []
                for line in f:
                    val = _get_dictionary(line)
                    if val:
                        vals.append(val)
                        batch_size = batch_size + 1
                        if batch_max_size == batch_size:
                            _insert_into_postgres(cursor, 'posts', vals)
                            batch_size = 0


if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    args = parser.parse_args()
    insert_into_postgres_batches(args.file)