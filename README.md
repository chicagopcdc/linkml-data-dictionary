# LinkML model of the pcdc data dictionary
This creates a data model so that 
artifacts can be used elsewhere and data can be validated.

## [Documentation](https://chicagopcdc.github.io/data_dictionary/)

## Testing 
To test if the schema is valid and can create a jsonified version of the model run:

`$ gen-json-schema linkml_data_dictionary/model/schema/data_dictionary.yaml`

Optionally add the `-v` flag for verbosity

## Generating Python
To generate the python data model call:
`gen-python linkml_data_dictionary/model/schema/data_dictionary.yaml > linkml_data_dictionary/python_model/data_dictionary.py` and the file will be written in the 'python_model' folder.

## Generating Markdown
To generate the markdown documents call:
`gen-markdown --dir linkml_data_dictionary/markdown_model  linkml_data_dictionary/model/schema/data_dictionary.yaml` and the markdown files will be written in the 'markdown_model' folder.

## Using the json data model to define the linkml model
From the root directory call:
`python linkml_data_dictionary/data_ingestion_to_linkml/json_to_linkml.py` 
This will create a new data_dictionary yaml file name including the key that matches the sheet version that the yaml was generated from. This data dictionary will be in the data_ingestion_to_linkml/output_linkml_yaml folder.

## Using the generated yaml file to generate python
Using the generated yaml filename call:
`gen-python linkml_data_dictionary/data_ingestion_to_linkml/output_linkml_yaml/data_dictionary_spreadsheet_<SPREADSHEET_KEY>.yaml > linkml_data_dictionary/python_model/data_dictionary_generated.py`

This will take the yaml created from spreadsheet data with the given SPREADSHEET_KEY (ex. 1k23ue9403), and create a python file with the name data_dictionary_generated.py in the same python_model folder

## Using the generated yaml file to generate markdown
Using the generated yaml filename call:
`gen-markdown --dir linkml_data_dictionary/markdown_model_generated  linkml_data_dictionary/data_ingestion_to_linkml/output_linkml_yaml/data_dictionary_spreadsheet_<SPREADSHEET_KEY>.yaml`

This will take the yaml created from spreadsheet data with the given SPREADSHEET_KEY (ex. 1k23ue9403), and create markdown files in the markdown_model_generated folder.

## Viewing the markdown
To view the markdown, make sure you have mkdocs installed (if not `pip install mkdocs`) and then run:
`mkdocs serve` 

Then you can navigate to localhost:8000 to view the generated documentation. 

## Generating SQL DDL
From the LinkML YAML file, you can generate the SQL commands to create tables with the given classes and relationships, to do so run:
`gen-sqlddl linkml_data_dictionary/data_ingestion_to_linkml/output_linkml_yaml/data_dictionary_spreadsheet_<SPREADSHEET_KEY>.yaml > linkml_data_dictionary/sql_ddl_generated/create_schema.sql`

This will save the sql commands to a `.sql` file in the sql_ddl_generated folder called `create_schema.sql`

## Using generated SQL to create tables
At the moment there are a few issues in the generated SQL that make it fail, namely  [this issue](https://github.com/linkml/linkml/issues/1407) however with a few manual fixes, the script in `linkml_data_dictionary/sql_ddl_generated/working_schema.sql` should create all of the tables successfully. The main changes are creating the schema before creating the associated tables and changing some of the assigned data types for certain columns. I tested this by running postgres14.1 in a docker container and running all of the scripts sequentially from the working_schema file.

## Creating and Validating Data Objects
To use the LinkML objects for validating incoming data, you can initialize python objects and the data model will validate if the given values are allowed and provide error messages if there are data mismatches. See the `linkml_data_dictionary/data_validation` folder for examples of input data, and the scripts to create data objects from the given data. To test the validation process and see what the resulting messages might look like you can run: `python linkml_data_dictionary/data_validation/validation_scripts/validate_json_w_python.py` and you should see errors along the lines of:
```
value errors
Unknown EthnicityEnum enumeration code: InvalidData
key errors
submitter_id must be supplied
```

The most final validation script for TSV format files is `validate_tsv_data.py` which can be tested with the command `python linkml_data_dictionary/data_validation/validation_scripts/validate_tsv_data.py`

## Future work
Future things to look into with this exploration are noted in the github issues
* Generalized python object creation from differing input types (json, tsv, csv, etc)
* Using the LinkML convert to validate data. example command (should be able to take different file types too): 
```
linkml-convert -m linkml_data_dictionary/python_model/data_dictionary_generated_fixed_quotes.py -o linkml_data_dictionary/data_validation/convert_test/ linkml_data_dictionary/data_validation/gen3_person_renamed_keys.json 
```