import numpy as np
import matplotlib.pyplot as plt


def generate_data() -> tuple[np.ndarray, int]:
    preonset: np.ndarray = np.random.uniform(low=-1, high=1, size=np.random.randint(30, 100))
    signal: np.ndarray = np.random.normal(size=np.random.randint(50, 100))
    return np.concatenate((preonset, signal)), preonset.size


def sin_date() -> tuple[np.ndarray, int]:
    preonset: np.ndarray = np.random.uniform(low=-0.25, high=0.25, size=np.random.randint(30, 100))
    preonset = np.full(preonset.shape, 0)
    signal = np.sin(np.linspace(0, 2 * np.pi, np.random.randint(50, 100)))
    return np.concatenate((preonset, signal)), preonset.size


def along_then() -> np.ndarray:
    preonset: np.ndarray = np.full(np.random.randint(30, 100), -1)
    middle: np.ndarray = np.linspace(-1, 1, np.random.randint(30, 100))
    end: np.ndarray = np.full(np.random.randint(30, 100), 1)
    return np.concatenate((preonset, middle, end))


def add_noise(prenoise_data: np.ndarray, noise_level: float, zero_adjustment=False) -> np.ndarray:
    if zero_adjustment:
        prenoise_data[prenoise_data == 0] = np.random.uniform(-0.25, 0.25, size=np.count_nonzero(prenoise_data == 0))
    noise = np.random.normal(0, noise_level * np.abs(prenoise_data), size=prenoise_data.size)
    return prenoise_data + noise


data = add_noise(along_then(), 0.2)
print(data)
print(data.shape)
print(data.size)

plt.plot(data)
plt.title('Simple Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

data = add_noise(sin_date()[0], 0.2, True)
plt.plot(data)
plt.title('Simple Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()
