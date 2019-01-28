# -*- coding: utf-8 -*-
import sys
import Compress



def main(argc, argv):
    plain = "1.6,0.81,-0.05,-1.04/1.6,0.81,-0.64,-0.85/1.86,-0.03,-0.42,1.03/1.93,-0.47,-0.42,1.03/1.92,-0.9,-0.42,1.03/1.92,-0.9,-0.17,0.8/" 
    plain = plain.replace(".", "a")
    plain = plain.replace(",", "b")
    plain = plain.replace("/", "c")
    plain = plain.replace("-", "d")

    print("元データ({0:4d}):{1}".format(len(plain), plain))

    compress = Compress.Compress()
    compressed = compress.compress(plain)
    print("圧縮　　({0:4d}):{1}".format(len(compressed), compressed))
    uncompressed = compress.uncompress(compressed)
    uncompressed = uncompressed.replace("a", ".")
    uncompressed = uncompressed.replace("b", ",")
    uncompressed = uncompressed.replace("c", "/")
    uncompressed = uncompressed.replace("d", "-")
    print("解凍　　({0:4d}):{1}".format(len(uncompressed), uncompressed))
    return


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
    sys.exit()
