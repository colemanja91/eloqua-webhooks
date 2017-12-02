"""
    Eloqua contact fields for exports and imports
"""

FIELD_SET = {
    'C_EmailAddress': {
        'elq': 'C_EmailAddress',
        'hubspot': 'properties.email.value'
    },
    'C_FirstName': {
        'elq': 'C_FirstName',
        'hubspot': 'properties.firstname.value'
    },
    'C_LastName': {
        'elq': 'C_LastName',
        'hubspot': 'properties.lastname.value'
    },
    'C_Company': {
        'elq': 'C_Company',
        'hubspot': 'properties.company.value'
    },
    'C_Country': {
        'elq': 'C_Country',
        'hubspot': 'properties.ip_country_code.value'
    },
    'C_StateProv': {
        'elq': 'C_StateProv',
        'hubspot': 'properties.ip_state_code.value'
    }
}


def get_hb_fields():
    """
    Return only target fields from FIELD_SET
    :return list:
    """

    fields_out = []

    for field in FIELD_SET:
        if 'hubspot' in FIELD_SET[field]:
            fields_out.append(FIELD_SET[field])

    return fields_out


def get_hb_fieldval(record, fname):
    """
    Return field value (typed) from input record

    :param dict record: Returned JSON object from Hubspot
    :param string fname: Field name to retrieve
    :return string:
    """

    field_path = fname.split('.')

    tmp_d = record

    # Cycle down dict until we get the last key in the field path
    try:
        for fkey in field_path:
            tmp_d = tmp_d[fkey]

        # If it's string, return as string. If another JSON object, return as string
        return str(tmp_d)
    except KeyError:
        return None


def hb_elq_fieldmap(record):
    """
    Parse out field set to map Hubspot records to Eloqua form fields.

    Hubspot data is sent in a nested JSON format, i.e.
    "meta.lastModified"

    This function abstracts that formatting work to take full advantage of the
    FIELD_SET config above.

    :param dict record: POSTed JSON object from Hubspot
    :return dict: Dict formatted for POST to Eloqua
    """

    rec_out = {}

    for field in get_hb_fields():

        rec_out[field['elq']] = get_hb_fieldval(record, field['hubspot'])

    return rec_out
