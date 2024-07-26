import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100) # Create an array of 100 points from 0 to 10
y = np.sin(x) # Calculate the same values for each point

# Create a line object
plt.plot(x, y, label='Sine Function')

#Add labels and titles
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Sine Function Plot By Dahnniey')

# Add a Legend
plt.legend()

# Show the plot
plt.show()
