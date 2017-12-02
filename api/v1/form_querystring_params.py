"""
    Querystring parameter mapping to pass to Eloqua

    Staticly-defined values may not be directly transferrable in the webhook
    payload, so we define a way of passing querystring parameters in to the
    request body.
"""


QSTRING_SET = {
    'A_OfferID': {
        'param': 'a_offerid',
        'elq': 'A_OfferID'
    },
    'A_TacticID_External': {
        'param': 'a_tactic_ext',
        'elq': 'A_TacticID_External'
    },
    'A_TacticID_Internal': {
        'param': 'a_tacticid_int',
        'elq': 'A_TacticID_Internal'
    },
    'F_FormData_Trigger': {
        'param': 'f_formdata_trigger',
        'elq': 'F_FormData_Trigger'
    }
}


def parse_qstring(request):
    """
    Parse and map querystrings to data dictionary

    :param flask.request: Flask request object
    :return dict:
    """

    qstring_data = {}

    for field in QSTRING_SET:

        fieldval = QSTRING_SET[field]

        qstring_data[fieldval['elq']] = request.args.get(fieldval['param'],
                                                         default='')

    return qstring_data
