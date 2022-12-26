from openpecha.core.pecha import OpenPechaFS


def get_opf_layers(opf_path):
    opf = OpenPechaFS(opf_path)
    opf_layers = opf.layers
    return opf_layers


def update_catalog(pceha_id,layer_types):
    pass


if __name__ == "__main__":
    pecha_id = "I4AEA9D55"
    opf_path = "./I4AEA9D55"
    layer_types = get_opf_layers(opf_path)
    if layer_types:
        update_catalog(pecha_id,layer_types)
    else:
        print(f"{pecha_id} has no layer")


    
    