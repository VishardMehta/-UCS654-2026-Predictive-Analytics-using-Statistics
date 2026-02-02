Methodology
	1.	Data Selection
The notebook loads an air quality dataset and extracts NO₂ concentration values. Missing and invalid entries are removed so only clean numeric data is used.
	2.	Data Transformation
A small sine-based transformation is added to the original values:
z = x + a_r \sin(b_r x)
This slightly perturbs the data and creates the variable z used for modeling.
	3.	Parameter Estimation
The transformed data is used to estimate parameters of a Gaussian-style probability model:
	•	Mean (μ) from the average of z
	•	Variance (σ²) from the spread of z
	•	Lambda (λ) using \lambda = \frac{1}{2\sigma^2}
	•	Constant (c) for normalization

These parameters define a theoretical distribution that approximates the data.

Results (Parameter Meaning)
	•	μ (mean): Central tendency of pollution values after transformation
	•	σ² (variance): Spread of pollution levels
	•	λ (lambda): Controls the width of the modeled curve
	•	c: Scaling factor to make the distribution valid


Result Graph Explanation

The graph shows a Kernel Density Estimate (KDE) of the transformed variable z.
<p align="center">
  <img src="https://github.com/user-attachments/assets/5f97b27f-82d6-4373-b189-bbbacecb4946" width="684" height="384">
</p>

Observations
	•	The distribution is strongly right-skewed.
	•	Most pollution values are clustered at lower levels.
	•	A long right tail indicates the presence of very high pollution values (outliers).
	•	The curve is not symmetric, meaning the data does not perfectly follow a normal distribution.

Interpretation

Because of the right skew:
	•	The mean is influenced by extreme high values
	•	The variance is large due to wide spread
	•	A Gaussian model can still approximate the data, but it does not perfectly match the real distribution

Final Insight

The notebook shows how real environmental data can be modeled statistically. However, the graph reveals that pollution data is skewed with extreme values, which is common in real-world measurements. This highlights the difference between theoretical distributions and actual observed data.
