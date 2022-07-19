from django.contrib import admin

from mainapp.models.node_models import Node
from mainapp.models.cargo_models import ShipCargo, LandCargo, Offer, ContractedOffer
from mainapp.models.resource_models import Resource
from mainapp.models.edge_models import SeaRoute, LandRoute
from mainapp.models.ship_models import TransportShip
from mainapp.models.icebreaker_models import Icebreaker


admin.site.register(Node)

admin.site.register(ShipCargo)
admin.site.register(LandCargo)
admin.site.register(Offer)
admin.site.register(ContractedOffer)

admin.site.register(Resource)

admin.site.register(SeaRoute)
admin.site.register(LandRoute)

admin.site.register(TransportShip)

admin.site.register(Icebreaker)
