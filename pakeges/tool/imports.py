# -*- coding: utf-8 -*-
import time, sys, glob, os, pickle, time
import cv2, dlib, pymysql
import pymysql.cursors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import concurrent.futures
from PIL import *
from skimage import io
from sklearn import *
import subprocess