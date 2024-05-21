import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

############################
### INPUT FILE PATHS HERE###
############################
pre_test_paths = ['/Users/username/Documents/GeneralPhysics_pretest_2015.csv','/Users/username/Documents/IntroPhysics_pretest_2016.csv']
post_test_paths = ['/Users/username/Documents/GeneralPhysics_posttest_2015.csv','/Users/username/Documents/IntroPhysics_posttest_2016.csv']
class_set=['General Physics','Intro Physics']
year_set=['2015','2016']
answer_key_path='/Users/username/Documents/Physics_test_key.csv'
question_num=5
num_questions=47
        
answer_df=pd.read_csv(answer_key_path)

#CODE THAT GENERATES TABLES

#Reads in CSV paths as pandas dataframes
def read_paths(test_paths):
    dataframes=[pd.read_csv(filepath) for filepath in test_paths]
    return dataframes  
        
#Makes list of answers for a specific question
def analyze_answers(dataframes,question):
    #question=5
    #question=int(QEntry.get())
    ans_list = []
    for df in dataframes:
        print(df)
        ans_list.extend(df.iloc[:, int(question)])
    return ans_list
       
#Returns dataframe with answers, counts, and percentages displayed
def order_answers(ans_list):
    answer_counts = Counter(ans_list)
    #print("answer counts",answer_counts)
    sorted_answers = sorted(answer_counts.items(), key=lambda x: x[1], reverse=True)
    #print("sorted_answers", sorted_answers)
    j=len(sorted_answers)
    #print(j)
    dfx = pd.DataFrame(sorted_answers, columns=['Answer', 'Count'])
    dfx['Percentage'] = dfx['Count'] / dfx['Count'].sum()
    #inserttable(dfx)
    #print(dfx)
    print(dfx)

#create function to deal with division if denominator is zero (automatically set to 0)
def division(n,d):
    if d ==0:
        return 0
    else:
        return n/d
    
#Combines all csvs to create one database for pre and post tests
def combine(pre_test_paths,post_test_paths):
    pre_dataframe=pd.concat(read_paths(pre_test_paths), axis=0)
    post_dataframe=pd.concat(read_paths(post_test_paths), axis=0)
    df_merged = pd.merge(pre_dataframe, post_dataframe, on='ID', suffixes=('_pre', '_post'))
    df_merged=df_merged.reset_index()
    return df_merged

###################################################
########## TABLES OF ANSWERS #############
###################################################
def answers_table(pre_test_paths,post_test_paths,question_num):
    print(f'Pre test answers question {question_num}')
    order_answers(analyze_answers(read_paths(pre_test_paths),question_num))
    print('')
    print(f'Post test answers question {question_num}')
    order_answers(analyze_answers(read_paths(post_test_paths),question_num))
    print('')

##################################################
########### TRANSITION PLOTS##############
###################################################
def transition_plots(pre_test_paths,post_test_paths,question_num):

    #combine csvs
    df_merged=combine(pre_test_paths,post_test_paths)

    #create figure with subplots
    fig,ax=plt.subplots(1, 1, figsize=(6, 4), tight_layout=True)
                
    #Make plot for each question
    overlapping=0.55
    test_opt = ["Pre","Post" ]
                
    j=question_num
                    
    for index, row in df_merged.iterrows():
        ans=[]
        ans.append(row[f'Q{j}_pre'])
        ans.append(row[f'Q{j}_post'])
        plt.plot(test_opt,ans, alpha=overlapping, c="gray")             
        plt.title(f'Question {j} Transition Plot')
        plt.tick_params(labelright=True)

##################################################
######### PARAMETER VALUE TABLES #################
################################################
def parameter_values(pre_test_paths,post_test_paths,answer_df,num_questions):

    #Combine csvs
    df_merged=combine(pre_test_paths,post_test_paths)

    #create parameter dataframe
    df_param_Qs = pd.DataFrame(columns=['Q', 'P', 'C', 'S', 'K', 'M'])
                            
    ## CREATING DATAFRAME FOR QUESTION PARAMETER VALUES
    # Initialize parameter_counts outside the loop
    parameter_counts = {'WDW': 0, 'WSW': 0, 'WR': 0, 'RW':0, 'RR':0}

    # Loop through questions
    h = 0
    while h < num_questions:
        # Get the answer for the current question
        answer = answer_df.iloc[0, h]

    # Loop through students
        for x in range(df_merged.shape[0]):
            pre_ans = df_merged.iloc[x, 2+h]
            post_ans = df_merged.iloc[x, 2+h+num_questions]

            if pre_ans == post_ans == answer:
                parameter_counts['RR'] += 1
            if pre_ans != answer and post_ans != answer and pre_ans != post_ans:
                parameter_counts['WDW'] += 1
            if pre_ans == post_ans and pre_ans != answer:
                parameter_counts['WSW'] += 1
            if pre_ans != answer and post_ans == answer:
                parameter_counts['WR'] += 1
            if pre_ans == answer and post_ans != answer:
                parameter_counts['RW'] += 1

                            
        #Calculate transition numbers and add as row to 
        df_param_Qs = df_param_Qs.append({'Q' : division((parameter_counts['RW']+parameter_counts['WR']+parameter_counts['WDW']),(parameter_counts['RR']+parameter_counts['WSW']+parameter_counts['RW']+parameter_counts['WR']+parameter_counts['WDW'])), 
                                        'P' : division((parameter_counts['WR']),(parameter_counts['RW']+parameter_counts['WR']+parameter_counts['WDW'])), 
                                        'C' : division((parameter_counts['RW']),(parameter_counts['RW']+parameter_counts['WR']+parameter_counts['WDW'])),
                                        'S' : division((parameter_counts['WDW']),(parameter_counts['RW']+parameter_counts['WR']+parameter_counts['WDW'])),
                                        'K' : division((parameter_counts['RR']),(parameter_counts['RR']+parameter_counts['RW'])),
                                        'M' : division((parameter_counts['WSW']),(parameter_counts['WSW']+parameter_counts['WR']+parameter_counts['WDW']))}, ignore_index = True)

        # Reset parameter_counts for the next question
        parameter_counts = {'WDW': 0, 'WSW': 0, 'WR': 0, 'RW':0, 'RR':0}

        h += 1
    return df_param_Qs

##################################
####### PARAMETER GRAPHS #########
##################################
def parameter_display(pre_test_paths,post_test_paths,answer_key,num_questions,df_param_Qs):
    
    #Generating Plot
    fig,ax=plt.subplots(2, 3, tight_layout=True)

    def create_axis(x,y,L):
        ax[x,y].bar(range(1,num_questions+1),df_param_Qs[L])
        mean_val = df_param_Qs[L].mean()
        ax[x,y].axhline(mean_val, color='r', linestyle='--', label='Mean')
        std_val = df_param_Qs[L].std()
        if mean_val-std_val <0:
            ax[x,y].axhline(0, color='y', linestyle='--', label='-1 Std Dev')
        else:
            ax[x,y].axhline(mean_val - std_val, color='y', linestyle='--', label='-1 Std Dev')
        if mean_val+std_val <1:
            ax[x,y].axhline(mean_val + std_val, color='g', linestyle='--', label='+1 Std Dev')
        ax[x,y].set_title(L)

    create_axis(0,0,'Q')
    create_axis(1,0,'P')
    create_axis(0,1,'C')
    create_axis(1,1,"S")
    create_axis(0,2,'K')
    create_axis(1,2,'M')

    fig.suptitle(f"{str(class_set)} {str(year_set)}")

######################
###DENSITY PLOTS######
######################
    
def density_plot(pre_test_paths,post_test_paths,answer_key,num_questions):
    df_graphing=pd.DataFrame(columns=['Q', 'P', 'C', 'S', 'K', 'M','Class','Year']) 

    for x in range(0,len(pre_test_paths)):
        df_param_Qs=parameter_values([pre_test_paths[x]], [post_test_paths[x]], answer_df, num_questions)
        df_param_Qs['Class']=[class_set[x]]*df_param_Qs.shape[0]
        df_param_Qs['Year']=[year_set[x]]*df_param_Qs.shape[0]
        df_graphing=df_graphing.append(df_param_Qs,ignore_index=True)
    print(df_graphing)

    fig, axes = plt.subplots(2, 3, figsize=(15, 7), sharey=True)
    fig.suptitle('Density Plots')

    sns.kdeplot(ax=axes[0,0],data=df_graphing, x="Q", hue='Class')
    sns.kdeplot(ax=axes[0,1],data=df_graphing, x="P", hue='Class')
    sns.kdeplot(ax=axes[0,2],data=df_graphing, x="C", hue='Class')
    sns.kdeplot(ax=axes[1,0],data=df_graphing, x="S", hue='Class')
    sns.kdeplot(ax=axes[1,1],data=df_graphing, x="K", hue='Class')
    sns.kdeplot(ax=axes[1,2],data=df_graphing, x="M", hue='Class')


#################################
###### SWITCH OUTPUT HERE #######
#################################

#question specific outputs (change question number at top)
answers_table(pre_test_paths,post_test_paths,question_num)
transition_plots(pre_test_paths,post_test_paths,question_num)

#general outputs
parameter_values(pre_test_paths,post_test_paths,answer_df,num_questions)
parameter_display(pre_test_paths,post_test_paths,answer_df,num_questions,parameter_values(pre_test_paths, post_test_paths, answer_df, num_questions))
density_plot(pre_test_paths,post_test_paths,answer_key_path,num_questions)

plt.show()