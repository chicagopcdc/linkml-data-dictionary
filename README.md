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
`gen-python model/schema/data_dictionary.yaml > python_model/data_dictionary.py` and the file will be written in the 'python_model' folder.

## Generating Markdown
To generate the markdown documents call:
`gen-markdown --dir markdown_model  model/schema/data_dictionary.yaml` and the markdown files will be written in the 'markdown_model' folder.

## Using the json data model to define the linkml model
From the root directory call:
`python data_ingestion_to_linkml/json_to_linkml.py` 
This will create a new data_dictionary yaml file name including the key that matches the sheet version that the yaml was generated from. This data dictionary will be in the data_ingestion_to_linkml/output_linkml_yaml folder.

## Using the generated yaml file to generate python
