from diplomacy.adjudicator.mapper import Mapper
from diplomacy.map_parser.vector.vector import Parser

# bot.run()

board = Parser().parse()
Mapper(board).get_moves_map(None)

# TODO: priorities: (MAP), (DB), (ALPHA), (BETA)

# TODO: (DB) setup DB and test db write & db read
# TODO: (DB) assert that the DB is backed up (needs to be a current up-to-date backup)

# TODO: (ALPHA) if anything is slow, we can cache a lot of things locally
# TODO: (ALPHA) update readme (how to use bot)
# TODO: (ALPHA) conduct testing: test solo, test group, live game test
# TODO: (ALPHA) me only command for editing all game map state without permanence restriction (ex. province adjacency)

# TODO: (BETA) add requirements.txt
# TODO: (BETA) clean up configs
# TODO: (BETA) support SVGs with minimal overhead
# TODO: (BETA) support raster images
# TODO: (BETA) add classic map example & update readme
