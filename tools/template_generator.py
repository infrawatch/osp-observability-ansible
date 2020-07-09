import yaml

with open("plugin_options.yaml", "r") as f:
  plugins = yaml.load(f.read())["plugins"]


for plugin, options in plugins.items():
    print(str(plugin))
    
    with open("{}.conf.j2".format(plugin), "w") as f:
        f.write("LoadPlugin {}\n".format(plugin))
        f.write("<Plugin \"{}\">\n".format(plugin))

        for option, value in options.items():
            print(option)
            print(value)
            if value["mandatory"]:
                f.write("   {} {{{{ collectd_plugin_{}_{} }}}}\n".format(option, plugin, option.lower().replace(" ", "")))
            else:
                f.write("   {{% if collectd_plugin_{}_{} is defined %}}\n".format(plugin, option.lower().replace(" ", "")))
                f.write("   {} collectd_plugin_{}_{}\n".format(option, plugin, option.lower().replace(" ", "")))
                f.write("   {{% endif %}}\n")


        f.write("</Plugin>\n")

    with open("{}.yml".format(plugin), "w") as f:

        for option, value in options.items():
            print(option)
            print(value)
            if value["mandatory"]:
                f.write("collectd_plugin_{}_{}: {}\n".format(plugin, option.lower().replace(" ", ""), value["default"]))
            else:
                f.write("# collectd_plugin_{}_{}: {}\n".format(plugin, option.lower().replace(" ", ""), value.get("default", '')))
