from sklearn import tree
import matplotlib.pyplot as plt

class Visualiser:
    def __init__(self):
        pass
       
        
    def visualise(self, clf, fn, cn):
        text_representation = tree.export_text(clf)
        print(text_representation)
        
        tree.plot_tree(clf);
        
      
        fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
        
        print(fn)
        cn = ['0', '1', '2', '3', '4']
        tree.plot_tree(clf,
                    feature_names = fn, 
                    class_names=cn,
                    filled = True);
        fig.savefig('imagename.png')