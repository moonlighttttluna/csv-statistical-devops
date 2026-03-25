import matplotlib.pyplot as plt
import os

def generate_visualizations(df, output_folder, filename):
    
    first_col = df.columns[0]
    plot_df = df.set_index(first_col)
    
   
    numeric_df = plot_df.select_dtypes(include=['number'])
    
    if numeric_df.empty:
        print(f"No numeric data found in {filename} to plot.")
        return

    
    plt.figure(figsize=(12, 6))
    numeric_df.plot(kind='bar', ax=plt.gca())
    
    plt.title(f"Analysis for {filename}")
    plt.ylabel("Value")
    plt.xlabel(first_col)
    plt.xticks(rotation=45)
    plt.legend(title="Metrics", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    
   
    image_name = filename.replace('.csv', '.png')
    plt.savefig(os.path.join(output_folder, image_name))
    plt.close()
