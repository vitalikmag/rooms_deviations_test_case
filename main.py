import os
import pandas as pd
import matplotlib.pyplot as plt


class PlotDrawer:
    def __init__(self, plot_dir):
        self.plot_folder = plot_dir
        if not os.path.exists(plot_dir):
            os.makedirs(plot_dir)

    def draw_plots(self, json_file):
        df = pd.read_json(json_file)

        plots_path = []

        # Plot true prediction corner percentage
        true_predict_count = sum(df['gt_corners'] == df['rb_corners'])
        true_predict_percent = true_predict_count / len(df) * 100
        plt.bar(['True prediction', 'False prediction'],
                [true_predict_count, len(df) - true_predict_count])
        plt.ylabel('Rooms count')
        plt.title(f'Percentage of rooms with true corner prediction: {true_predict_percent:.2f}%')
        acc_plot_path = os.path.join(self.plot_folder, 'true_predict_bar.png')
        plots_path.append(acc_plot_path)
        plt.savefig(acc_plot_path)
        plt.close()

        # Plot mean deviation
        mean_deviation = df['mean']
        plt.hist(mean_deviation)
        plt.xlabel('Mean deviation')
        plt.ylabel('Rooms count')
        plt.title('Histogram of mean deviation')
        mean_plot_path = os.path.join(self.plot_folder, 'mean_deviation.png')
        plots_path.append(mean_plot_path)
        plt.savefig(mean_plot_path)
        plt.close()

        # Plot max deviation
        max_deviation = df['max']
        plt.hist(max_deviation)
        plt.xlabel('Max deviation')
        plt.ylabel('Rooms count')
        plt.title('Histogram of max deviation')
        max_plot_path = os.path.join(self.plot_folder, 'max_deviation.png')
        plots_path.append(max_plot_path)
        plt.savefig(max_plot_path)
        plt.close()

        # Plot min deviation
        min_deviation = df['min']
        plt.hist(min_deviation)
        plt.xlabel('Min deviation')
        plt.ylabel('Rooms count')
        plt.title('Histogram of min deviation')
        min_plot_path = os.path.join(self.plot_folder, 'min_deviation.png')
        plots_path.append(min_plot_path)
        plt.savefig(min_plot_path)
        plt.close()

        # Plot deviation limit percentage
        deviation_limit = 5
        in_limit_count = sum(df['mean'] <= deviation_limit)
        in_limit_percent = in_limit_count / len(df) * 100
        plt.bar(['In limit', 'Out limit'], [in_limit_count, len(df) - in_limit_count])
        plt.ylabel('Count')
        plt.title(f'Percentage of rooms in {deviation_limit}'
                  f' degree deviation limit: {in_limit_percent:.2f}%')
        limit_plot_path = os.path.join(self.plot_folder, 'deviation_limit.png')
        plots_path.append(limit_plot_path)
        plt.savefig(limit_plot_path)
        plt.close()

        return plots_path

