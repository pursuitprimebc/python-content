''' question - Compress the Video
Chef recorded a video explaining his favorite recipe. However, the size of the video is too large to upload on the internet. He wants to compress the video so that it has the minimum size possible.

Chef's video has N frames initially. The value of the ith frame is Ai . Chef can do the following type of operation any number of times:

Choose an index i(1≤i≤N) such that the value of the ith frame is equal to the value of either of its neighbors and remove the ith frame.
Find the minimum number of frames Chef can achieve.

Input Format
First line will contain T, the number of test cases. Then the test cases follow.
The first line of each test case contains a single integer N - the number of frames initially.
The second line contains N space-separated integers, A1,A2,…,AN - the values of the frames.
Output Format
For each test case, output in a single line the minimum number of frames Chef can achieve.
'''



t = int(input())
for i in range(t):
    
    n = int(input())
    frames_val = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        if frames_val[i] == frames_val[i+1]:
            count += 1  
    minimum_frames = n-count
    print(minimum_frames)       
        
        
        

