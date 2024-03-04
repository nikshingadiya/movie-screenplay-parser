from langchain.output_parsers import ResponseSchema
from langchain.output_parsers.structured import StructuredOutputParser
response_schemas = [
    ResponseSchema(
        name="scene_details",
        description="return the dictionary of extracted data",
    ),
]


output_parser_schema = StructuredOutputParser.from_response_schemas(response_schemas)