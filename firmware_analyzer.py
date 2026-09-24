class FirmwareAnalyzer:

    def __init__(self, file):
        self.file = file

    def read_file(self):
        with open(self.file, "rb") as file:
            data = file.read()
            return data

    def get_file_size(self, data):
        return f"{len(data)}"

    def get_file_type(self, data):

        header = data[:4]

        if header == b"\x7fELF":
            return "ELF"

        # IF NO KNOWN SIGNATURE WAS FOUND ASSUME RAW_BINARY
        return "No matching signature RAW_BINARY assumed"

    def get_file_architecture(self, data, file_type):
        pass
    
    def get_file_endian(self, data, file_type):

        if file_type == "ELF":
            header = data[:16]

            elf_class = header[4]
            elf_data = header[5]

            if elf_class == 1:
                bits = 32
            elif elf_class == 2:
                bits = 64
            else:
                bits = "Unknown"

            if elf_data == 1:
                endian = "Little-endian"
            elif elf_data == 2:
                endian = "Big-endian"
            else:
                endian = "Unknown"

            return bits, endian

    def analyze_file(self):
        data = self.read_file()

        file_size = self.get_file_size(data)
        file_type = self.get_file_type(data)
        architecture = self.get_file_architecture(data, file_type)
        endian = self.get_file_endian(data, file_type)

        return [file_size, file_type, architecture, endian[1]]


        
        