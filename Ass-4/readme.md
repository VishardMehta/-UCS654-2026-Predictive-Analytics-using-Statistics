Learning Probability Density Functions using GAN

Overview

This project aims to learn the probability density function (PDF) of a transformed random variable using only data samples, without assuming any analytical or parametric distribution. A Generative Adversarial Network (GAN) is used to model the unknown distribution.

Dataset
	•	Source: India Air Quality Dataset (Kaggle)
	•	Feature used: NO₂ concentration
	•	Missing values were removed and all values were converted to numeric format.
	•	Each NO₂ value is treated as an independent sample.


Data Transformation

The original variable x (NO₂ concentration) is transformed as:

z = x + a_r \sin(b_r x)

where:

a_r = 0.5 (r \bmod 7), \quad b_r = 0.3 (r \bmod 5 + 1)

and r is the university roll number.
This nonlinear transformation makes the resulting distribution analytically unknown.

Methodology

A vanilla GAN is used to learn the distribution of the transformed variable z.
	•	Generator:
Takes noise sampled from \mathcal{N}(0,1) and outputs synthetic samples z_f.
	•	Discriminator:
Classifies input samples as real (z) or fake (z_f).

The GAN is trained adversarially using only samples of z, without assuming any predefined PDF.


PDF Approximation

After training:
	•	A large number of samples are generated from the generator.
	•	The probability density function is estimated using Kernel Density Estimation (KDE).
	•	KDE plots of real and generated samples are compared.
<p align="centre">
<img width="790" height="461" alt="Screenshot 2026-02-10 at 16 53 56" src="https://github.com/user-attachments/assets/c5be0717-37e7-417a-ac05-1479e3a64d42" />
</p>
Results

Aspect	Observation
Mode coverage	Major modes of the distribution are captured
Training stability	Loss curves indicate stable training
Distribution quality	Generated PDF aligns well with real data in high-density regions

The KDE plots show that the generator is able to approximate the overall shape of the real data distribution, with minor deviations in the tails.
<p align="centre">
<img width="545" height="413" alt="Screenshot 2026-02-10 at 16 53 27" src="https://github.com/user-attachments/assets/365974e0-8663-442b-a82a-07524ee7d1ba" />
</p>
Conclusion

The results show that a GAN can successfully learn an unknown probability density function using data samples alone. The generator provides an implicit and reasonable approximation of the transformed NO₂ concentration distribution.

