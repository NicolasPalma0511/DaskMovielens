#!/bin/bash

# Cambia la IP por la IP del scheduler
dask-worker scheduler:8786 --nprocs 2 --nthreads 4
