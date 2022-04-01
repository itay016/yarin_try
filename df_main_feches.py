import pandas as pd



class db_matirials():
    def __init__(self,folder='C:/Users/Itay0/Desktop/PythonProject/Text_OCT/files_db',dict={'connection':'connections.csv','groups':'groups.csv','matirials':'matirials.csv'}):
        self.folder=folder
        self.dict=dict
        pass
    def get_word_list(self,word):
        dict_names=self.dict
        df_matirials=pd.read_csv(self.folder+"/"+dict_names['matirials'])
        #df_groups=pd.read_csv(self.folder+"/"+dict_names['groups'])
        df_connection = pd.read_csv(self.folder +"/"+ dict_names['connection'])
        idd = df_matirials[df_matirials['name'] == word]['id']
        main_id=list(df_connection[df_connection['connect'] == list(idd)[0]]['id'])[0]
        mask = (df_connection['id'] == main_id) | (df_connection['connect'] == main_id)
        in_ids= df_connection[mask]
        all_ids=list(in_ids['connect'])
        if not main_id in all_ids:
            all_ids.append(main_id)
        lsre=df_matirials[[i in all_ids for i in df_matirials['id']]]
        return lsre['name']
        print()
