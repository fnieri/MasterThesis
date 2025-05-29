import os
from collections import defaultdict

def generate_latex_appendix(source_dirs, output_file, file_types):
    """
    Generate a LaTeX appendix with source code listings organized by subfolders.

    Args:
        source_dirs: List of directories to scan
        output_file: Output .tex file path
        file_types: Dictionary mapping file extensions to listing options
                   Example: {'.cpp': {'language': 'C++', 'section': 'C++ Files'}}
    """
    with open(output_file, 'w') as f:
        # Write LaTeX header
        f.write(r"""
\part{Source Code Appendix}
""")

        # Process each file type category
        for ext, options in file_types.items():
            f.write(f"\n\\chapter{{{options['section']}}}\n")

            # Dictionary to store files by their relative subfolder path
            files_by_subfolder = defaultdict(list)

            # Find all matching files and group by subfolder
            for source_dir in source_dirs:
                for root, _, files in os.walk(source_dir):
                    for file in files:
                        if file.endswith(ext):
                            filepath = os.path.join(root, file)
                            rel_path = os.path.relpath(filepath, start=os.path.dirname(output_file))

                            # Get relative subfolder path (from source_dir)
                            rel_subfolder = os.path.relpath(root, start=source_dir)
                            if rel_subfolder == '.':
                                rel_subfolder = "Root"

                            files_by_subfolder[rel_subfolder].append((file, rel_path))

            # Sort subfolders and files alphabetically
            for subfolder in sorted(files_by_subfolder.keys()):
                # Escape special LaTeX characters in subfolder name
                safe_subfolder = subfolder.replace('_', r'\_')
                f.write(f"\n\\section{{{safe_subfolder}}}\n")

                # Sort files in this subfolder
                files_in_subfolder = sorted(files_by_subfolder[subfolder], key=lambda x: x[0])

                for filename, rel_path in files_in_subfolder:
                    # Escape special LaTeX characters in filename
                    safe_filename = filename.replace('_', r'\_')

                    f.write(f"\n\\subsection{{{safe_filename}}}\n")
                    f.write(f"\\lstinputlisting[style=mystyle, {options['language']}]{{{rel_path}}}\n")

# Configuration for C++/Erlang files
source_dirs = [
    "/home/francy/Desktop/RealTimeDeltaQSD/src/",
    "/home/francy/Desktop/dqsd_otel/src"
]

file_types = {
    '.cpp': {'language': 'language=C++', 'section': 'C++ Source Files'},
    '.h': {'language': 'language=C++', 'section': 'C++ Header Files'},
    'CMakeLists.txt': {'language': '', 'section': 'Build Configuration Files'},
    '.erl': {'language': 'language=erlang', 'section': 'Erlang Source Files'},
    '.app.src': {'language': 'language=erlang', 'section': 'Erlang Application Files'}
}

# Generate the LaTeX file
generate_latex_appendix(source_dirs, "code_appendix.tex", file_types)
