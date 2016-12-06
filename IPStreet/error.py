class IPStreetError(Exception):
    pass


class ParamsInvalidError(IPStreetError):
    pass


class APIConnectionError(IPStreetError):
    pass


class SendError(IPStreetError):
    pass
