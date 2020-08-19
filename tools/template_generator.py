import yaml

def create_plugin_template(plugin):

    with open("../roles/collectd_config/templates/{}.conf.j2".format(plugin["name"]), "w") as f:
        f.write("LoadPlugin {}\n\n".format(plugin["name"]))
        f.write("<Plugin \"{}\">\n".format(plugin["name"]))

        for option, value in plugin.get("options", {}).items():
            print(option)
            print(value)
            if not value["mandatory"]:
                f.write("   {{% if collectd_plugin_{}_{} is defined %}}\n".format(plugin["name"], option.lower().replace(" ", "")))
            if type(value.get("default", '')) in (str, bool):
                f.write("   {} \"{{{{ collectd_plugin_{}_{} }}}}\"\n".format(option, plugin["name"], option.lower().replace(" ", "")))
            elif isinstance(value["default"], list):
                f.write("   {{% for {} in {{{{ collectd_plugin_{}_{} }}}} %}}\n".format(option.lower(), plugin["name"], option.lower()))
                f.write("   {} \"{{{{ {} }}}}\"\n".format(option, option.lower().replace(" ", "")))
                f.write("   {% endfor %}\n")

            if not value["mandatory"]:
                f.write("   {% endif %}\n")

        f.write("</Plugin>\n")

def create_plugin_defaults(plugin):
    with open("../roles/collectd_config/defaults/main/{}.yml".format(plugin["name"]), "w") as f:

        f.write("---\n")
        f.write("# Defaults for the {} plugin.\n".format(plugin["name"]))
        for option, value in plugin["options"].items():
            print(option)
            print(value)
            if value["mandatory"]:
                f.write("collectd_plugin_{}_{}: {}\n".format(plugin["name"], option.lower().replace(" ", ""), value["default"]))
            else:
                f.write("# collectd_plugin_{}_{}: {}\n".format(plugin["name"], option.lower().replace(" ", ""), value.get("default", '')))

if __name__=='__main__':
    with open("plugin_options.yaml", "r") as f:
      plugins = yaml.load(f.read())["plugins"]  # This is a list of plugins
      print(plugins)

    for plugin in plugins:
        print(str(plugin))

        create_plugin_template(plugin)
        if plugin.get("set_defaults", True) and plugin.get("options",  None):
            create_plugin_defaults(plugin)
