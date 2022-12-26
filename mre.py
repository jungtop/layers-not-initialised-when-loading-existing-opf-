from openpecha.core.pecha import OpenPechaFS


def get_opf_layers(opf_path):
    opf = OpenPechaFS(opf_path)
    opf_layers = opf.layers
    return opf_layers


def update_catalog():
    pass

if __name__ == "__main__":
    opf_path = "./IC0947659"
    layer_types = get_opf_layers(opf_path)
    update_catalog


    
    