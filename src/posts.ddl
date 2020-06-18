drop table if exists posts;
create table posts
(
id integer,
post_type integer,
parent_id int,
accepted_answer_id integer,
creation_date date,
score integer,
view_count integer,
body text,
owner_user_id integer,
last_editor_user_id integer,
last_editor_display_name text,
last_edit_date date,
last_activity_date date,
community_owned_date date,
close_date date,
tags text,
title text,
answer_count integer,
comment_count integer,
favorite_count integer
);

alter table posts set unlogged;

-- Disable indexes for fast inserts
-- alter table posts add primary key (id)
-- create index if not exists parent_id_idx on posts (parent_id);
