from TopLevelModel import TopLevelModel
from Generator import Generator
from Process import Process

experimental_frame = TopLevelModel("EF")

generator = Generator("Generator")
process = Process("Process")

experimental_frame.sub_model_list = [generator, process]
experimental_frame.add_coupling("out", process, "in", generator)
experimental_frame.add_coupling("out", generator, "in", process)
experimental_frame.run_simulation()
