from program_parser import ProgramParser
from ui import UI
from firmware_analyzer import FirmwareAnalyzer

def main():

    parser = ProgramParser()
    args = parser.parse()

    ui = UI()

    match args.command:

        case "info":
            fw_analyzer = FirmwareAnalyzer(args.file)
            fw_info = fw_analyzer.analyze_file() # --> returns a list of fw info that ui can print
            
            ui.show_info(
                    args.file,
                    fw_info[2], # architecture
                    fw_info[0], # file_size
                    fw_info[1], # file_type
                    fw_info[3] # endian
            )
        case _:
            pass

if __name__ == "__main__":
    main()