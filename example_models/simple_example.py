# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
sns.set()

from heavymodel import Model

class DemographicModel(Model):
	def num_policies(self, t):
		return 1 if t == 0 else self.num_policies(t-1) - self.num_lapses(t-1)

	def num_lapses(self, t):
		return 0.1 * self.num_policies(t)

demo = DemographicModel()

demo._run(20)

df = pd.DataFrame({"num_lapses":demo.num_lapses.values, "num_policies":demo.num_policies.values})
sns.lineplot(data=df)
