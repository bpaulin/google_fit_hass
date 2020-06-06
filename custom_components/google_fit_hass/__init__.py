"""Google fit hass integration."""

from homeassistant.helpers import entity_component

DOMAIN = "google_fit_hass"


def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    def handle_set_new_weight(call):
        """Handle the service call."""
        entity_id = call.data.get("entity_id")
        new_weight = call.data.get("new_weight")
        entity = hass.data["entity_platform"][DOMAIN][0].entities[entity_id]
        entity.set_new_weight(new_weight)

    hass.services.register(DOMAIN, "set_new_weight", handle_set_new_weight)

    # Return boolean to indicate that initialization was successfully.
    return True

