# pyflinker
pyflinker is a program that creates Docker Container based Flink Cluster on the fly and lets you to submit a your favourite python job on the fly.

Create a Flink 1.6 Cluster with the number of Worker nodes(Task Mangers) you want to have and Run a Python-based Flink Streaming Job at startup in a single command based application.

The cluster here created is container-based using Docker so the distributed framework is managed.

Scale the cluster on the fly according to you need.

No need to manually deploy jars anymore!!!

1.Clone this repository.

2.Copy your scala maven project build jar for Flink to the folder

3.Run the shell script Flying_flink.sh using the command below.

./Flying_flink.sh 2 pyflinkjob.py

Arguments:

arg1:Number of Flink Worker Nodes you want to allot.

arg2:The python code or job which Does the Flink Steaming which are synonymous  which you want to deploy to the flink cluster.

Go to your localhost:8077 to view the flink cluster.

Now Testing your Python-based Flink Streaming Application is just FUN!!
