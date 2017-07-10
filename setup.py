import cx_Freeze as cx

executables = [cx.Executable("pygametutorial.py")]

cx.setup(
        name = "GRAND PRIX",
        options = {"built_exe": {"packages" : ["pygame"], "include_files":["index.png"] }},
        executables = executables
        );

