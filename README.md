# LinkML model of the pcdc data dictionary
This creates a data model so that 
artifacts can be used elsewhere and data can be validated.

## [Documentation](https://chicagopcdc.github.io/data_dictionary/)

## Testing 
To test if the schema is valid and can create a jsonified version of the model run:

`$ gen-json-schema model/schema/data_dictionary.yaml`

Optionally add the `-v` flag for verbosity

## Generating Python
To generate the python data model call:
`gen-python model/schema/data_dictionary.yaml > python_model/data_dictionary.py` and the file will be writtin in the 'python_model' folder.
