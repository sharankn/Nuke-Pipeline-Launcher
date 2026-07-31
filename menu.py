import nuke

toolbar = nuke.menu("Nuke")
pipeline = toolbar.addMenu("Pipeline")

pipeline.addCommand(
    "Launch Pipeline",
    "import launcher; launcher.launch()"
)