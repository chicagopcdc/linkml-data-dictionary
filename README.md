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
Using the generated yaml filename call:
`gen-python data_ingestion_to_linkml/output_linkml_yaml/data_dictionary_spreadsheet_<SPREADSHEET_KEY>.yaml > python_model/data_dictionary_generated.py`

This will take the yaml created from spreadsheet data with the given SPREADSHEET_KEY (ex. 1k23ue9403), and create a python file with the name data_dictionary_generated.py in the same python_model folder

## Using the generated yaml file to generate markdown
Using the generated yaml filename call:
`gen-markdown --dir markdown_model_generated  data_ingestion_to_linkml/output_linkml_yaml/data_dictionary_spreadsheet_<SPREADSHEET_KEY>.yaml`

This will take the yaml created from spreadsheet data with the given SPREADSHEET_KEY (ex. 1k23ue9403), and create markdown files in the markdown_model_generated folder.

## Viewing the markdown
To view the markdown, make sure you have mkdocs installed (if not `pip install mkdocs`) and then run:
`mkdocs serve` 

Then you can navigate to localhost:8000 to view the generated documentation. 

## Generating SQL DDL
From the LinkML YAML file, you can generate the SQL commands to create tables with the given classes and relationships, to do so run:
`linkml-data-dictionary % gen-sqlddl data_ingestion_to_linkml/output_linkml_yaml/data_dictionary_spreadsheet_<SPREADSHEET_KEY>.yaml > sql_ddl_generated/create_schema.sql`

This will save the sql commands to a `.sql` file in the sql_ddl_generated folder called `create_schema.sql`