import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

master_df = pd.read_csv("data-files/Joined-Master-Dataset.csv")

ax = master_df.plot(kind="scatter", x="Depth (ft)",y="Modeled Quartz", color="b", label="Modeled Quartz", figsize=(16,8))
master_df.plot(kind="scatter", x="Depth (ft)",y="Quartz", color="r", label="Actual Quartz", ax=ax)

ax = master_df.plot(kind="scatter", x="%Si",y="Modeled Quartz", color="b", label="Modeled Quartz", figsize=(16,8))
master_df.plot(kind="scatter", x="%Si",y="Quartz", color="r", label="Actual Quartz", ax=ax)

ax = master_df.plot(kind="scatter", x="Depth (ft)",y="Modeled Calcite", color="b", label="Modeled Calcite", figsize=(16,8))
master_df.plot(kind="scatter", x="Depth (ft)",y="Calcite", color="r", label="Actual Calcite", ax=ax)

ax = master_df.plot(kind="scatter", x="%Ca",y="Modeled Calcite", color="b", label="Modeled Calcite", figsize=(16,8))
master_df.plot(kind="scatter", x="%Ca",y="Calcite", color="r", label="Actual Calcite", ax=ax)