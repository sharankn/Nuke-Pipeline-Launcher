# Nuke Pipeline Launcher

A Python-based pipeline launcher for Foundry Nuke that automates script creation and shot setup.

## Features

- Create versioned Nuke scripts automatically (`v001`, `v002`, `v003`...)
- Automatically load EXR image sequences into Read nodes
- Select Project, Sequence, and Shot through a simple PySide2 interface
- Open existing Nuke scripts
- Organize scripts using a standardized project structure

## Folder Structure

```
D:\Toxic
│
├── Seq001
│   └── Shot0001
│       ├── plate
│       ├── render
│       └── script
│
└── Seq002
    └── Shot0002
        ├── plate
        ├── render
        └── script
```

## Technologies

- Python
- PySide2
- Foundry Nuke API
- OpenEXR
- Git

## Installation

1. Copy `launcher.py` and `menu.py` to your `.nuke` directory.
2. Restart Nuke.
3. Launch the tool from the Nuke menu.

## Workflow

1. Select the Project.
2. Choose the Sequence.
3. Choose the Shot.
4. Click **New Script**.
5. A new versioned Nuke script is created and the EXR sequence is loaded automatically.
