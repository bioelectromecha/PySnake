import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Slither",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["snake_head.png", "snake_apple.png"]}},
    description="Slither python game",
    executables=executables
)
