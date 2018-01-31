import mmmm
import datetime

# There are two ways to load scores of a model

# The 1st way,
mmmm.new_score(
    model_name='titanic',
    model_version='1.0',
    model_domain='SM',
    score_date=datetime.now(),
    scores=[0.87, 0.83, 0.83, 0.87],
    links=['ABC123', 'ABC124', 'ABC125', 'ABC123'],  # should be carefully created and documented
    db_conn=db_conn)

# The 2nd way,
mmmm.new_score(
    model_id='SM-titanic-1.0',
    score_date=datetime.now(),
    scores=[0.87, 0.83, 0.83, 0.87],
    links=['ABC123', 'ABC124', 'ABC125', 'ABC123'],  # should be carefully created and documented
    db_conn=db_conn)
