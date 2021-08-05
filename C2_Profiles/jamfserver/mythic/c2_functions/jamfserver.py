from mythic_c2_container.C2ProfileBase import *


class JamfServer(C2Profile):
    name = "jamfserver"
    description = "Imitates a Jamf Pro Server to control enrolled devices."
    author = "@calhall"
    is_p2p = False
    is_server_routed = False
    parameters = [
        C2ProfileParameter(
            name="callback_port",
            description="Callback Port",
            default_value="80",
            verifier_regex="^[0-9]+$",
            required=False,
        ),
        C2ProfileParameter(
            name="callback_host",
            description="Callback Host",
            default_value="http://domain.com",
            verifier_regex="^(http|https):\/\/[a-zA-Z0-9]+",
        ),
    ]
