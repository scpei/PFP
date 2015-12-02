import os

#python pfp.py data_path train_file test_file output_file num_latent_factor learning_rate regularization_term num_iter user_norm item_norm


if __name__=='__main__':
    learning_rate = 0.01
    K = [2,3,4,5,6,7,8,9,10]
    reg = [0.001, 0.005, 0.01,0.05,0.1]
    user_norm = 100
    item_norm = 100
    for l in K:
        print('Number of Latent Factors: '+str(l))
        os.system('python pfp_KL_kk.py ~/Data/ratebeer/Data/ Train_90.txt Test_10.txt /home/tzhao/Data/ratebeer/PFP_KL_KK/10_%d.out 6 %lf %lf 5000000 %d %d %d&' % ( l, learning_rate, reg[1], user_norm, item_norm,l))

