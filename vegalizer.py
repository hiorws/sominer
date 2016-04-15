from json import dumps, loads
import argparse
import sys
import os


class Vegaizer:

    def __init__(self, schema_type):
        self.schema_type = schema_type
        file_dir = os.path.dirname(os.path.abspath(__file__))
        vega_address = "%s/schema_types/%s.json" % (file_dir, schema_type)
        self.vega_json = loads(open(vega_address).read())

    def data_to_vega(self, data_name):
        data_json_raw = read_json(data_name)
        data_json_dict = data_json_raw[0]
        for key in data_json_dict.keys():
            self.vega_json["data"][0]["values"].append({"category": key, "amount": data_json_dict[key]})

    def change_color(self, color1, color2):
        self.vega_json["marks"][0]["properties"]["update"]["fill"]["value"] = color1
        self.vega_json["marks"][0]["properties"]["hover"]["fill"]["value"] = color2

    def change_size(self, sizes):
        self.vega_json["width"] = sizes[0]
        self.vega_json["height"] = sizes[1]

    def save_changes(self, output_file):
        f = open(output_file, "w")
        f.write(dumps(self.vega_json))
        f.close()


def read_json(json_name):
    json_file = open(json_name, "r").read()
    return loads(json_file)


def find_available_schemas():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    schema_dir_content = os.listdir("%s/schema_types" % file_dir)
    schemas = []
    for content in schema_dir_content:
        content = content.split(".")
        if content[1] == "json":
            schemas.append(content[0])
    return tuple(schemas)


def get_parser():
    available_schemas = find_available_schemas()
    parser_object = argparse.ArgumentParser(description="Vegalizer: Uses given data to create a JSON "
                                                        "file that is ready to use with Vega")
    parser_object.add_argument("-l",
                               "--list",
                               help="List available schema types...",
                               action="store_true",
                               dest="list")
    parser_object.add_argument("-t",
                               "--type",
                               dest="schema_type",
                               choices=available_schemas,
                               help="Available ones: %s Code won't work without this parameter" % (available_schemas,)
                               )
    parser_object.add_argument("-d",
                               "--data",
                               dest="data_name",
                               help="Give address to data json. ie. 'data.json'."
                                    " Code won't work without this parameter")
    parser_object.add_argument("-o",
                               "--output-name",
                               dest="output_file",
                               help="Output file name, ie. visualized_data.json. "
                                    "Code won't work without this parameter")

    parser_object.add_argument("-c1",
                               "--color1",
                               dest="color1",
                               default="steelblue",
                               help="Define color. "
                                    "ie. Color of bars in a bar vega to 'red','blue','black',etc..")
    parser_object.add_argument("-c2",
                               "--color2",
                               dest="color2",
                               default="red",
                               help="Define color. ie. Highlight color of bars in a"
                                    " bar vega to 'red','blue','black',etc..")

    parser_object.add_argument("-s",
                               "--size",
                               nargs=2,
                               type=int,
                               default=(400, 200),
                               dest="size")
    return parser_object

if __name__ == "__main__":
    parser = get_parser()
    if len(sys.argv) == 1:
        print(parser.parse_args(['-h']))
    else:
        args = parser.parse_args()
        if args.list:
            print("Available schema(s) is/are: %s" % find_available_schemas())
        else:
            vegaizer = Vegaizer(args.schema_type)
            vegaizer.data_to_vega(args.data_name)
            vegaizer.change_color(args.color1, args.color2)
            vegaizer.change_size(args.size)
            vegaizer.save_changes(args.output_file)
