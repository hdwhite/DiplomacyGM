from diplomacy.adjudicator.mapper import Mapper
from diplomacy.map_parser.vector import vector
from diplomacy.persistence import order
from diplomacy.persistence.unit import UnitType


def run() -> None:
    board = vector.Parser().parse()

    paris = next((unit for unit in board.units if unit.province.name == "Paris"), None)
    nantes = next((unit for unit in board.units if unit.province.name == "Nantes"), None)
    bordeaux = next((unit for unit in board.units if unit.province.name == "Bordeaux"), None)
    marseille = next((unit for unit in board.units if unit.province.name == "Marseille"), None)
    dijon = next((unit for unit in board.units if unit.province.name == "Dijon"), None)
    barcelona = next((unit for unit in board.units if unit.province.name == "Barcelona"), None)
    orleans = next((province for province in board.provinces if province.name == "Orleans"), None)
    corse = next((province for province in board.provinces if province.name == "Corse"), None)
    ghent = next((province for province in board.provinces if province.name == "Ghent"), None)
    board.unit_orders = {
        paris: order.Hold(paris),
        nantes: order.Core(nantes),
        bordeaux: order.Move(bordeaux, orleans),
        marseille: order.ConvoyTransport(marseille, dijon, corse),
        dijon: order.Support(dijon, bordeaux, orleans),
        barcelona: order.RetreatDisband(barcelona),
    }
    board.build_orders = {
        order.Build(ghent, UnitType.ARMY),
    }

    Mapper(board).get_moves_map(None)