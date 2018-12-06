from flask_restful import reqparse

"""
    Contains all the different request parsers
"""

# The parser for any type of user
user_parser = reqparse.RequestParser()
user_parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
user_parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
user_parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

# The parser for performer registration
performer_parser = reqparse.RequestParser()
performer_parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
performer_parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
performer_parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
performer_parser.add_argument('tags',
                        required=True,
                        help="You must at least choose one category",
                        action="append"
                        )

# The parser for viewer registration
viewer_parser = reqparse.RequestParser()
viewer_parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
viewer_parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
viewer_parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

# The parser for events
event_parser = reqparse.RequestParser()
event_parser.add_argument('text',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

# The parser for offers
offer_parser = reqparse.RequestParser()
offer_parser.add_argument('text',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
