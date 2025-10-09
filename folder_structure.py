import os

# Define the folder and file structure
project_structure = {
        "app": {
            "__init__.py": "",
            "graph": {
                "__init__.py": "",
                "builder.py": "# Graph builder module\n\ndef build_graph():\n    pass\n",
                "nodes.py": "# Node functions for LangGraph\n",
                "edges.py": "# Edge logic for LangGraph (optional)\n",
            },
            "chains": {
                "__init__.py": "",
                "tools.py": "# Tool functions for LangChain\n",
                "agents.py": "# Agent setup\n",
            },
            "config": {
                "__init__.py": "",
                "settings.py": "import os\n\nOPENAI_API_KEY = os.getenv('OPENAI_API_KEY')\n",
            },
            "utils": {
                "__init__.py": "",
                "common.py": "# Common utility functions\n",
            },
            "main.py": "# Entry point\n\nfrom app.graph.builder import build_graph\n\nif __name__ == '__main__':\n    print('Building graph...')\n    build_graph()\n",
        },
        "tests": {
            "__init__.py": "",
            "test_graph.py": "from app.graph.builder import build_graph\n\ndef test_graph_builds():\n    assert build_graph() is None\n",
        },
        ".gitignore": "*.pyc\n__pycache__/\n.env\n.venv/\n",
        "requirements.txt": "langgraph\nlangchain\nopenai\n",
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# Run the structure generation
if __name__ == "__main__":
    create_structure(".", project_structure)
    print("✅ LangGraph project structure created successfully.")
