import os

#python pfp.py data_path train_file test_file output_file num_latent_factor learning_rate regularization_term num_iter user_norm item_norm


if __name__=='__main__':
    learning_rate = 0.01
    K = [2,3,4,5,6,7,8,9,10]
    reg = [0.001, 0.005, 0.01,0.05,0.1]
    user_norm = 10
    item_norm = 10
    for l in K:
        print('Number of Latent Factors: '+str(l))
        #print 'python bpr.py ~/code/python/Data/lthing/ Train_70.txt Test_30.txt num_latent_factor/%d.out %d %lf %lf 100000 %d %d' % (l, l, learning_rate, reg[1], user_norm, item_norm)
        os.system('python pfp.py ~/Data/ratebeer/Data/ Train_90.txt Test_10.txt /home/tzhao/Data/ratebeer/PFP_WARP/num_latent_factor/%d.out %d %lf %lf 100000 %d %d &' % (l, l, learning_rate, reg[1], user_norm, item_norm))

    for r in reg:
        print('Regularization: '+str(l))
        #print 'python bpr.py ~/code/python/Data/Ciao/ Train_70.txt Test_30.txt regularization_term/%.4f.out %d %lf %lf 100000 %d %d' % (r, K[1], learning_rate, r, user_norm, item_norm)
        os.system('python pfp.py ~/Data/ratebeer/Data/ Train_90.txt Test_10.txt /home/tzhao/Data/ratebeer/PFP_WARP/regularization/%.3f.out %d %lf %lf 100000 %d %d &' % (r, K[1], learning_rate, r, user_norm, item_norm))
