class RadarCompare:
    
    def __init__(self) -> None:
        self.dataMajorPoint = []
        self.universities = []
        self.fig = None
        
    def PlotRadar(self,universities,dataMajorPoint):
        import numpy as np
        import matplotlib.pyplot as plt

        # Data for the radar charts
        self.dataMajorPoint = dataMajorPoint
    

        # Labels for the radar chart axes
        Majors = ['Language', 'Thinking', 'Arts and Society', 'Science', 'Mathematics', 'General']

        # Colors for each sample
        colors = ['magenta','blue', 'green', 'red', 'orange','purple','yellow','cyan','brown','black'] #limit to compare = 10

        # Names of the universities
        self.universities = universities

        # Create a figure and subplot
        self.fig, ax = plt.subplots(figsize=(6,7.5), subplot_kw={'polar': True})

        # Plot the radar charts
        for i, sample_data in enumerate(self.dataMajorPoint):
            angles = np.linspace(0, 2 * np.pi, len(Majors), endpoint=False).tolist()
            sample_data += sample_data[:1]  # Close the plot
            angles += angles[:1]  # Close the plot

            ax.plot(angles, sample_data, marker='o', linestyle='-', color=colors[i], linewidth=2, label=universities[i])
            ax.fill(angles, sample_data, color=colors[i], alpha=0.25)

        # Set the ticks and labels for the radar chart
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(Majors)
        
        ax.yaxis.grid(True)
        plt.subplots_adjust(top=1.05)

        # Add a legend
        ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.39),ncol=3)

        # Set the title
        title_offset = 1.1  # You can adjust the value as needed
        ax.set_title("Comparison of Universities", size=15, weight='bold', y=title_offset)

        # Show the plot
        plt.show()

