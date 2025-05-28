# GABenchmark

Genetic Algorithm Benchmark for Structural Optimization of a Bridge.
https://github.com/RaduMarin19/StructuralOptimizationGA

Results for current config:

GA Configuration:
  Chromosome Length: 1305 (X=29, Y=9, Z=5)
  Population Size: 100
  Generations: 20
  Crossover Probability: 0.1
  Mutation Probability: 0.1
  Fitness Function: sphere^2 * ackley (2D)

Starting Grid Search...
Testing 27 = 27 combinations
--------------------------------------------------------------------------------

Testing: Tournament | Single Point | Bit Flip
  Trial 1: 0.105488
  Trial 2: 0.007449
  Trial 3: 0.000800
  Trial 4: 1.666103
  Trial 5: 0.564232
  Trial 6: 0.816507
  Trial 7: 1.178076
  Trial 8: 4.394748
  Trial 9: 0.367703
  Trial 10: 0.777070
  Average: 0.987818 (±1.243181)

Testing: Tournament | Single Point | Swap
  Trial 1: 24.323680
  Trial 2: 0.011434
  Trial 3: 10.117985
  Trial 4: 12.726748
  Trial 5: 110.724268
  Trial 6: 0.024225
  Trial 7: 101.904272
  Trial 8: 0.207677
  Trial 9: 40.905722
  Trial 10: 114.244374
  Average: 41.519038 (±45.811704)

Testing: Tournament | Single Point | Inversion
  Trial 1: 0.222287
  Trial 2: 158.699493
  Trial 3: 0.796350
  Trial 4: 18.689856
  Trial 5: 0.676700
  Trial 6: 9.031978
  Trial 7: 0.495348
  Trial 8: 21.237763
  Trial 9: 1.315111
  Trial 10: 9.528461
  Average: 22.069335 (±46.141968)

Testing: Tournament | Uniform | Bit Flip
  Trial 1: 0.443299
  Trial 2: 0.317214
  Trial 3: 0.505504
  Trial 4: 1.302898
  Trial 5: 0.508826
  Trial 6: 0.277983
  Trial 7: 0.291075
  Trial 8: 0.002336
  Trial 9: 0.052188
  Trial 10: 2.218803
  Average: 0.592013 (±0.639699)

Testing: Tournament | Uniform | Swap
  Trial 1: 6.193544
  Trial 2: 297.427244
  Trial 3: 2.959177
  Trial 4: 21.526324
  Trial 5: 340.691551
  Trial 6: 67.866270
  Trial 7: 91.978021
  Trial 8: 26.699040
  Trial 9: 160.688613
  Trial 10: 1.308848
  Average: 101.733863 (±118.805546)

Testing: Tournament | Uniform | Inversion
  Trial 1: 27.473293
  Trial 2: 0.228781
  Trial 3: 23.436468
  Trial 4: 5.165583
  Trial 5: 41.654686
  Trial 6: 29.014982
  Trial 7: 28.834017
  Trial 8: 62.656499
  Trial 9: 41.359880
  Trial 10: 0.152738
  Average: 25.997693 (±19.018064)

Testing: Tournament | Two Point | Bit Flip
  Trial 1: 1.634424
  Trial 2: 0.244170
  Trial 3: 2.927788
  Trial 4: 0.006371
  Trial 5: 1.271286
  Trial 6: 0.826292
  Trial 7: 0.691804
  Trial 8: 3.173503
  Trial 9: 1.859218
  Trial 10: 0.217301
  Average: 1.285216 (±1.055353)

Testing: Tournament | Two Point | Swap
  Trial 1: 16.089240
  Trial 2: 25.091960
  Trial 3: 223.023864
  Trial 4: 46.509153
  Trial 5: 68.800312
  Trial 6: 8.688067
  Trial 7: 7.899432
  Trial 8: 521.276951
  Trial 9: 7.761978
  Trial 10: 46.067669
  Average: 97.120863 (±154.029250)

Testing: Tournament | Two Point | Inversion
  Trial 1: 4.017470
  Trial 2: 32.351601
  Trial 3: 6.526445
  Trial 4: 4.622781
  Trial 5: 2.763644
  Trial 6: 0.961103
  Trial 7: 3.231001
  Trial 8: 10.849848
  Trial 9: 1.177640
  Trial 10: 4.153340
  Average: 7.065487 (±8.848032)

Testing: Roulette Wheel | Single Point | Bit Flip
  Trial 1: 12.541172
  Trial 2: 5.723098
  Trial 3: 0.424082
  Trial 4: 8.884228
  Trial 5: 13.881278
  Trial 6: 5.879830
  Trial 7: 8.693843
  Trial 8: 11.181044
  Trial 9: 3.316778
  Trial 10: 2.807915
  Average: 7.333327 (±4.220352)

Testing: Roulette Wheel | Single Point | Swap
  Trial 1: 25.673266
  Trial 2: 19.884433
  Trial 3: 53.635066
  Trial 4: 26.497899
  Trial 5: 95.976151
  Trial 6: 40.431630
  Trial 7: 97.385179
  Trial 8: 42.474657
  Trial 9: 37.890833
  Trial 10: 5.194234
  Average: 44.504335 (±29.023803)

Testing: Roulette Wheel | Single Point | Inversion
  Trial 1: 0.752609
  Trial 2: 9.704755
  Trial 3: 20.047429
  Trial 4: 10.672014
  Trial 5: 14.225688
  Trial 6: 99.920034
  Trial 7: 8.722413
  Trial 8: 26.961868
  Trial 9: 9.811831
  Trial 10: 10.311130
  Average: 21.112977 (±27.101586)

Testing: Roulette Wheel | Uniform | Bit Flip
  Trial 1: 6.938546
  Trial 2: 1.243070
  Trial 3: 5.837424
  Trial 4: 4.894814
  Trial 5: 10.433808
  Trial 6: 9.184397
  Trial 7: 3.130944
  Trial 8: 2.890929
  Trial 9: 70.438700
  Trial 10: 1.082456
  Average: 11.607509 (±19.835677)

Testing: Roulette Wheel | Uniform | Swap
  Trial 1: 30.779227
  Trial 2: 28.099706
  Trial 3: 8.389724
  Trial 4: 32.009733
  Trial 5: 32.222884
  Trial 6: 79.828323
  Trial 7: 40.206138
  Trial 8: 47.082793
  Trial 9: 24.723321
  Trial 10: 53.336714
  Average: 37.667856 (±18.285341)

Testing: Roulette Wheel | Uniform | Inversion
  Trial 1: 8.941505
  Trial 2: 9.037302
  Trial 3: 20.545924
  Trial 4: 51.207507
  Trial 5: 7.993304
  Trial 6: 3.868610
  Trial 7: 29.662760
  Trial 8: 11.804657
  Trial 9: 26.182265
  Trial 10: 112.937843
  Average: 28.218168 (±31.275986)

Testing: Roulette Wheel | Two Point | Bit Flip
  Trial 1: 6.930222
  Trial 2: 2.121319
  Trial 3: 0.882105
  Trial 4: 36.553048
  Trial 5: 0.336319
  Trial 6: 14.038298
  Trial 7: 19.065541
  Trial 8: 15.304446
  Trial 9: 6.777605
  Trial 10: 0.561505
  Average: 10.257041 (±10.855973)

Testing: Roulette Wheel | Two Point | Swap
  Trial 1: 1.734850
  Trial 2: 20.437269
  Trial 3: 13.495908
  Trial 4: 83.301415
  Trial 5: 2.496447
  Trial 6: 48.781590
  Trial 7: 23.230674
  Trial 8: 10.642316
  Trial 9: 1.143783
  Trial 10: 247.431243
  Average: 45.269549 (±71.631671)

Testing: Roulette Wheel | Two Point | Inversion
  Trial 1: 61.526527
  Trial 2: 0.574013
  Trial 3: 1.822721
  Trial 4: 4.902836
  Trial 5: 11.805264
  Trial 6: 22.929422
  Trial 7: 131.264136
  Trial 8: 23.357843
  Trial 9: 4.740918
  Trial 10: 0.190013
  Average: 26.311369 (±39.183949)

Testing: Rank | Single Point | Bit Flip
  Trial 1: 1.741948
  Trial 2: 8.856145
  Trial 3: 2.681548
  Trial 4: 11.236517
  Trial 5: 4.187741
  Trial 6: 0.035250
  Trial 7: 0.616959
  Trial 8: 0.458851
  Trial 9: 4.402962
  Trial 10: 0.566341
  Average: 3.478426 (±3.629843)

Testing: Rank | Single Point | Swap
  Trial 1: 66.323141
  Trial 2: 6.711625
  Trial 3: 8.669936
  Trial 4: 19.312399
  Trial 5: 1.496677
  Trial 6: 13.827958
  Trial 7: 59.588182
  Trial 8: 14.495936
  Trial 9: 82.190020
  Trial 10: 14.456768
  Average: 28.707264 (±27.512551)

Testing: Rank | Single Point | Inversion
  Trial 1: 61.925540
  Trial 2: 2.834502
  Trial 3: 15.079479
  Trial 4: 2.659500
  Trial 5: 1.395535
  Trial 6: 18.089548
  Trial 7: 4.731814
  Trial 8: 3.851309
  Trial 9: 11.748981
  Trial 10: 8.130990
  Average: 13.044720 (±17.164431)

Testing: Rank | Uniform | Bit Flip
  Trial 1: 50.027506
  Trial 2: 5.506101
  Trial 3: 3.795415
  Trial 4: 0.436784
  Trial 5: 1.463426
  Trial 6: 4.121804
  Trial 7: 2.260357
  Trial 8: 3.300030
  Trial 9: 1.187236
  Trial 10: 0.069702
  Average: 7.216836 (±14.364477)

Testing: Rank | Uniform | Swap
  Trial 1: 146.761589
  Trial 2: 6.344108
  Trial 3: 476.378610
  Trial 4: 1.918185
  Trial 5: 350.837023
  Trial 6: 15.004020
  Trial 7: 203.490902
  Trial 8: 12.635705
  Trial 9: 162.162907
  Trial 10: 82.344923
  Average: 145.787797 (±152.949696)

Testing: Rank | Uniform | Inversion
  Trial 1: 11.192649
  Trial 2: 0.117852
  Trial 3: 33.197364
  Trial 4: 69.680885
  Trial 5: 2.287778
  Trial 6: 17.817098
  Trial 7: 3.140274
  Trial 8: 9.062914
  Trial 9: 69.784456
  Trial 10: 3.397637
  Average: 21.967891 (±25.598814)

Testing: Rank | Two Point | Bit Flip
  Trial 1: 5.794535
  Trial 2: 0.411184
  Trial 3: 0.205779
  Trial 4: 0.433170
  Trial 5: 6.290636
  Trial 6: 5.487921
  Trial 7: 0.354395
  Trial 8: 2.342315
  Trial 9: 1.646377
  Trial 10: 1.182455
  Average: 2.414877 (±2.346691)

Testing: Rank | Two Point | Swap
  Trial 1: 0.376672
  Trial 2: 79.501884
  Trial 3: 42.161808
  Trial 4: 2.301072
  Trial 5: 12.589978
  Trial 6: 286.397697
  Trial 7: 9.059573
  Trial 8: 1.376897
  Trial 9: 7.204735
  Trial 10: 28.015158
  Average: 46.898547 (±83.193596)

Testing: Rank | Two Point | Inversion
  Trial 1: 4.469973
  Trial 2: 105.233707
  Trial 3: 2.831822
  Trial 4: 0.050170
  Trial 5: 3.212240
  Trial 6: 5.631640
  Trial 7: 13.615167
  Trial 8: 1.166003
  Trial 9: 0.130560
  Trial 10: 1.126673
  Average: 13.746795 (±30.728560)

================================================================================
TOP 3 COMBINATIONS:
================================================================================

1. Tournament | Uniform | Bit Flip
   Average Fitness: 0.592013 (±0.639699)
   IDs: Selection=0, Crossover=1, Mutation=0

2. Tournament | Single Point | Bit Flip
   Average Fitness: 0.987818 (±1.243181)
   IDs: Selection=0, Crossover=0, Mutation=0

3. Tournament | Two Point | Bit Flip
   Average Fitness: 1.285216 (±1.055353)
   IDs: Selection=0, Crossover=2, Mutation=0

================================================================================
Running best configuration in detail...

Best solution found: [-0.1712491273344483, -4.63898202337135, 0.14728012522175948, 3.4468401939549302, -4.124154037095893, -3.1372169556789418, -3.286480695542844, -3.018718414043483, 4.316643326201744, -0.2869536453615016, 0.48152680598483766, 1.875557409367631, -1.7982542268899349, -1.842722402592604, -1.385501802685674, 1.5889254707636793, -3.400369600207302, -2.7476134668059897, -0.008219173193386275, -4.699848591722266, -1.4786761933540484, -1.5852084692292072, -0.4863344607620217, 4.093403013597062, 1.6144721519471563, -3.2251903754196882, -0.5006810380158591, -0.5682186141018173, -3.6966967372162207, -3.967217484428021, 4.415107815368302, 3.2860104148946903, 2.077277222792203, 1.4620357127153047, -2.574820141447373, 4.901209473425913, -0.22729535629469044, -4.033266900169229, -1.1724791977041944, -2.180887939745352, -4.461419991145693, -0.35807720452188896, 2.906878027891513, -1.5885795403059189, -2.8461321961993953]
Best fitness: 0.668641
