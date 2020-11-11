#Importing the modules
import pyfiglet as pft
import os
import time

print("\n")
print(pft.figlet_format("ARTH   CLI",font="banner3-D"))


while True: 
 print(" \t\t\t######################################",end="")
 print("""
\t\t\t|  Press 1: Setup Hadoop             |   
\t\t\t|  Press 2: Hadoop Services          |               
\t\t\t|  Press 3: Setup Docker             |
\t\t\t|  Press 4: Run Docker Commands      |
\t\t\t|  Press 5: Setup Httpd Web Server   |
\t\t\t|  Press 6: Setup AWS Services       |
\t\t\t|  Press 7: Run AWS Services         |
\t\t\t|  Press 8: Setup Ansible            |
\t\t\t|  Press 9: To Exit                  |
""",end="")
 print(" \t\t\t######################################")
 print("\n")
 user_input = input("Enter your Choice: ")
 check_input = int(user_input)
 if isinstance(check_input, int):
    if(check_input == 1):
      print("-------------------------------------------------",end="")
      print("""
Note: Copy the Hadoop Software and jdk software
      at /root/hadoop_software/ directory
""",end="")
      print("-------------------------------------------------")
      sub_input1  = input("Setup Hadoop  (Local/Remote): ")
      sub_input1  = sub_input1.lower()
      if(sub_input1 == "local"):
       node_input = input("Configure {} machine as (namenode/datanode/client): ".format(sub_input1))
       node_input = node_input.lower()
       if(node_input == "namenode"):
        print("Setting up Namenode")
        os.system("rpm -i /root/hadoop_software/jdk-8u171-linux-x64.rpm")
        os.system("rpm -i /root/hadoop_software/hadoop-1.2.1-1.x86_64.rpm --force")
        os.system("mkdir /namenode")
        ip_address = input("Enter you Current Ip: ") 
        new_file = open("/etc/hadoop/core-site.xml","r")
        lines = new_file.readlines()
        lines[7] = "<property>\n"
        new_file = open("/etc/hadoop/core-site.xml", "w")
        new_file.writelines(lines)
        new_file.close()
        new_file = open("/etc/hadoop/core-site.xml","a")
        new_file.write("<name>fs.default.name</name>\n") 
        new_file.write("<value>hdfs://{}:9001</value>\n".format(ip_address))
        new_file.write("</property>\n")
        new_file.write("</configuration>\n")


        n_file = open("/etc/hadoop/hdfs-site.xml","r")
        line = n_file.readlines()
        line[7] = "<property>\n"
        n_file = open("/etc/hadoop/hdfs-site.xml", "w")
        n_file.writelines(line)
        n_file.close()
        n_file = open("/etc/hadoop/hdfs-site.xml","a")
        n_file.write("<name>dfs.name.dir</name>\n") 
        n_file.write("<value>/namenode</value>\n")
        n_file.write("</property>\n")
        n_file.write("</configuration>\n")
        
        print("Namenode setup Successfully")       
        print("-------------------------------------------------",end="")
        print("""
Note: Format namenode using command:-
      hadoop namenode -format
      
""",end="")
        print("-------------------------------------------------")
      

       elif(node_input == "datanode"):
        print("Setting up DataNode")
        os.system("rpm -i /root/hadoop_software/jdk-8u171-linux-x64.rpm")
        os.system("rpm -i /root/hadoop_software/hadoop-1.2.1-1.x86_64.rpm --force")
        os.system("mkdir /dataNode")
        ip_address = input("Enter you Current Ip: ") 
        new_file = open("/etc/hadoop/core-site.xml","r")
        lines = new_file.readlines()
        lines[7] = "<property>\n"
        new_file = open("/etc/hadoop/core-site.xml", "w")
        new_file.writelines(lines)
        new_file.close()
        new_file = open("/etc/hadoop/core-site.xml","a")
        new_file.write("<name>fs.default.name</name>\n") 
        new_file.write("<value>hdfs://{}:9001</value>\n".format(ip_address))
        new_file.write("</property>\n")
        new_file.write("</configuration>\n")


        n_file = open("/etc/hadoop/hdfs-site.xml","r")
        line = n_file.readlines()
        line[7] = "<property>\n"
        n_file = open("/etc/hadoop/hdfs-site.xml", "w")
        n_file.writelines(line)
        n_file.close()
        n_file = open("/etc/hadoop/hdfs-site.xml","a")
        n_file.write("<name>dfs.data.dir</name>\n") 
        n_file.write("<value>/dataNode</value>\n")
        n_file.write("</property>\n")
        n_file.write("</configuration>\n")
       
        os.system("hadoop-daemon.sh start datanode")
        
        print("DataNode setup Successfully")
      
       elif(node_input == "client"):
        print("Setting up as Client")
        os.system("rpm -i /root/hadoop_software/jdk-8u171-linux-x64.rpm")
        os.system("rpm -i /root/hadoop_software/hadoop-1.2.1-1.x86_64.rpm --force")
        ip_address = input("Enter you Current Ip: ") 
        new_file = open("/etc/hadoop/core-site.xml","r")
        lines = new_file.readlines()
        lines[7] = "<property>\n"
        new_file = open("/etc/hadoop/core-site.xml", "w")
        new_file.writelines(lines)
        new_file.close()
        new_file = open("/etc/hadoop/core-site.xml","a")
        new_file.write("<name>fs.default.name</name>\n") 
        new_file.write("<value>hdfs://{}:9001</value>\n".format(ip_address))
        new_file.write("</property>\n")
        new_file.write("</configuration>\n")
      
        print("Client setup Successfully")
      
       else:
        print("Invalid Node Input")
      else:
       print("remote")
    elif(check_input == 2):
      print("                         WELCOME TO HADOOP SERVICES ")
      print("                #############################################") 
      print("\t\t|  => Press 1: Hadoop Report                |")
      print("\t\t|  => Press 2: Upload Files                 |")
      print("\t\t|  => Press 3: Upload Files with Size       |")  
      print("\t\t|  => Press 4: To read the File             |")
      print("\t\t|  => Press 5: To Remove the File           |")
      print("\t\t|  => Press 6: To list File                 |") 
      print("\t\t|  => Press 7: To Exit                      |") 
      print("                #############################################") 
      while True:
       hadoop_serv = input("Enter The Service you want: ")
       if hadoop_serv == "1":
        os.system("hadoop dfsadmin -report")
       elif hadoop_serv == "2":
        fileName = input("Enter the File Name to upload : ")
        os.system("hadoop fs -put {} /".format(fileName))
       elif hadoop_serv == "3":
        fileName = input("Enter the File Name to upload : ")
        blockSize = input("Enter the block size in bytes : ")
        os.system("hadoop fs -Ddfs.block.size={0} -put {1} /".format(blockSize,fileName))
       elif hadoop_serv == "4":
        fileName = input("Enter the File Name to read : ")
        os.system("hadoop fs -cat /{}".format(fileName))
       elif hadoop_serv == "5":
        fileName = input("Enter the File Name to remove : ")
        os.system("hadoop fs -rm {} /".format(fileName))
       elif hadoop_serv == "6":
        os.system("hadoop fs  -ls /")
       elif hadoop_serv == "exit":
        break
       else:
        print("Invalid Choice")
    elif(check_input == 3):
      docker_input = input("Setup Docker (Local/Remote): ")
      docker_input = docker_input.lower()
      if docker_input == "local":
       print("-----------------------------------")
       print("Configuring YUM for Docker")
       os.system("touch /etc/yum.repos.d/docker.repo")
       docker_file = open('/etc/yum.repos.d/docker.repo', 'w')
       docker_file.write("[dockerfile]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0")
       print("YUM for Docker => Successfull\n")
       print("-----------------------------------")
       print("Installing Docker in REHL 8")
       os.system("yum install docker-ce --nobest -y")
       print("Docker Install => Successfull\n")
       print("-----------------------------------")
       print("Starting Docker Services")
       os.system("systemctl start docker")
       print("Docker service Started")
       print("-----------------------------------")
      elif docker_input == "remote":
       print("Remote")
    elif(check_input == 4):
      print("                         WELCOME TO DOCKER SERVICES ")
      print("                #############################################") 
      print("\t\t|  => start docker service                  |")
      print("\t\t|  => enable docker permanent               |")
      print("\t\t|  => desible docker                        |")  
      print("\t\t|  => docker images                         |")
      print("\t\t|  => show all containers                   |")
      print("\t\t|  => show running containers               |") 
      print("\t\t|  => launch new containers                 |")   
      print("\t\t|  => download new docker images            |")
      print("\t\t|  => create your own images                |")
      print("\t\t|  => see all running ports                 |")
      print("\t\t|  => start container                       |")
      print("\t\t|  => attach container                      |")
      print("\t\t|  => stop container                        |")
      print("\t\t|  => remove containers                     |")
      print("\t\t|  => remove docker images                  |")
      print("\t\t|  => inspect container                     |")
      print("\t\t|  => check docker info                     |")
      print("\t\t|  => docker status                         |")
      print("\t\t|  => stop docker services                  |")
      print("                #############################################") 
      while True:
        p = input("What Can I Do For You : ")
        if(("start"in p)or("run"in p))and("docker"in p):
          os.system("systemctl restart docker")
          os.system("espeak-ng 'docker started'")
          print("Docker Services started ")
        elif(("show"in p)or("open"in p))and("images"in p):
          os.system("docker images")
          os.system("espeak-ng 'docker images'")
        elif(("show"in p)or("open"in p))and("running"in p)and("containers"in p):
          os.system("docker ps")
          os.system("espeak-ng 'running containers'")
        elif(("show"in p)or("open"in p))and("all"in p)and("containers"in p):
          os.system("docker ps -a")
          os.system("espeak-ng 'all containers'")
        elif(("launch"in p)or("run"in p))and("new"in p)and("container"):
          ctname=input("container name : ")
          imgname=input("image name : ")
          os.system("docker run -it --name {} {}".format(ctname,imgname))
          os.system("espeak-ng 'container is created'")
        elif(("download"in p)or("pull"in p))and("images"):
          imgname=input("docker image name : ")
          os.system("docker pull {}".format(imgname))
          os.system("espeak-ng 'image downloaded'")
        elif("clone"in p)and("commit" in p):
          ctname=input("container name to commit : ")
          imgname=input("give name to your new image : ")
          os.system("docker commit {} {}".format(ctname,imgname))
          os.system("espeak-ng 'commited new image'")
        elif(("show"in p)or("open"in p))and("ports"in p):
          os.system("netstat -tnlp")
          os.system("espeak-ng 'all running ports'")
        elif("start"in p)and("container"in p):
          ctname=input("container name : ")
          os.system("docker start {}".format(ctname))
          os.system("espeak-ng 'container started'")
        elif("attach"in p)and("container"in p):
          ctname=input("container name : ")
          os.system("docker attach {}".format(ctname))
          os.system("espeak-ng 'attached container'")
        elif("stop"in p)and("container"in p):
          ctname=input("container name : ")
          os.system("docker stop {}".format(ctname))
          os.system("espeak-ng 'stoped container'")
        elif("remove"in p)and("container"in p):
          ctname=input("container name : ")
          os.system("docker rm {}".format(ctname))
          os.system("espeak-ng 'container removed'")
        elif("remove"in p)and("image"in p):
          imgname=input("docker image name : ")
          os.system("docker rmi {}".format(imgname))
          os.system("espeak-ng 'docker image removed'")
        elif(("show"in p)or("available"in p))and("networks"in p)and("docker"in p):
          os.system("docker network ls")
          os.system("espeak-ng 'docker networks'")
        elif(("info"in p)or("inspect"in p))and("container"in p):
          ctname=input("container name : ")
          os.system("docker inspect {}".format(ctname))
          os.system("espeak-ng 'inspected docker'")
        elif("info"in p)and("docker"in p):
          os.system("docker info")
          os.system("espeak-ng 'docker information'")
        elif("status"in p)and("docker"in p):
          os.system("systemctl status docker")
          os.system("espeak-ng 'docker status'")
        elif(("stop"in p)or("exit"in p))and("docker"in p):
          os.system("systemctl stop docker")
          os.system("espeak-ng 'docker stoped'")
        elif("enable"in p)and("docker"in p):
          os.system("systemctl enable docker")
          os.system("espeak-ng 'enabled docker'")
        elif("disable"in p)and("docker"in p):
          os.system("systemctl disable docker")
          os.system("espeak-ng 'disabled docker'")
        elif("exit"in p):
          os.system("espeak-ng 'thanks for using my services'")
          print("################# THANKS FOR USING MY SERVICES #################")
          break
        else:
          os.system("espeak-ng 'try again'")
          print("TRY AGAIN ")

    elif(check_input == 5):
      http_input = input("Setup Httpd WebServer(Local/Remote): ")
      if http_input == "local":
        print("Installing Httpd Software")
        os.system("yum install httpd -y")
        print("Httpd Install => Successfully")
        print("----------------------------------")
        print("Deploying a demo website")
        html_file = open("/var/www/html/index.html", "w")
        html_file.write("<h1><center>Demo Website</center></h1>")
        html_file.close()
        print("----------------------------------")
        print("Starting the Httpd Services")
        os.system("systemctl start httpd")
        print("----------------------------------")
      elif http_input == "remote":
        print("Remote")
    elif(check_input == 6):
      print("Installing AWS CLI in LINUX Machine")
      os.system("curl -O https://bootstrap.pypa.io/get-pip.py")
      os.system("python3 get-pip.py --user")
      os.system("export PATH=~/.local/bin:$PATH")
      os.system("source ~/.bash_profile")
      os.system("pip3 install awscli")
      print("AWS Setup => Successfull")
    elif(check_input == 7):
      print("                         WELCOME TO AWS SERVICES ")
      print("                #############################################") 
      print("\t\t|  => Press 1:  Login To Account            |")
      print("\t\t|  => Press 2:  Create a key Pair           |")
      print("\t\t|  => Press 3:  List key Pairs              |")
      print("\t\t|  => Press 4:  Create a Security group     |")  
      print("\t\t|  => Press 5:  Adding InBound Rules        |")
      print("\t\t|  => Press 6:  Information of Instances    |")
      print("\t\t|  => Press 7:  Start a Stopped Instances   |") 
      print("\t\t|  => Press 8:  Stop a Running Instance     |")   
      print("\t\t|  => Press 9:  Terminate an Instance       |")
      print("\t\t|  => Press 10: Launch an Instance          |")
      print("\t\t|  => Press 11: Create a Volume(EBS)        |")
      print("\t\t|  => Press 12: Delete a volume(EBS)        |")
      print("\t\t|  => Press 13: Deattach a volume(EBS)      |")
      print("\t\t|  => Press 14: Attach Volume               |")
      print("\t\t|  => Press 15: Create a S3 Bucket          |")
      print("\t\t|  => Press 16: Copy Data to Any s3 Bucket  |")
      print("\t\t|  => Press 17: For CloudFront Distribution |")
      print("\t\t|  => Press 18: To Exit                     |")
      print("                #############################################") 
      while True: 
        aws_serv = input("Enter Your Choice : ")
        if aws_serv == "1":
          os.system("aws configure")
          print("logined")
        elif aws_serv == "2":
          keyname = input("Enter the new key name : ")
          os.system("aws ec2 create-key-pair --key-name {}".format(keyname))
          print("Key pair created")
        elif aws_serv == "3":
          os.system("aws ec2 describe-key-pairs")
        elif aws_serv == "4":
          sgname = input("Enter the sg name : ")
          description = input("Give the Description : ")
          vpc = input("Enter the vpc ID : ")
          os.system("aws ec2 create-security-group --group-name {0} --description {1} --vpc-id {2}".format(sgname,description,vpc))
        elif aws_serv == "5":
          sgname = input("Enter the sg name : ")
          protocol = input("Enter the protocol : ")
          port = input("Enter the port number : ")
          cidr = input("Enter the cidr block : ")
          os.system("aws ec2 authorize-security-group-ingress --group-name {0} --protocol {1} --port {2} --cidr {3} ".format(sgname,protocol,port,cidr))
        elif aws_serv == "6":
          os.system("aws ec2 describe-instances")
        elif aws_serv == "7":
          instID = input("Enter the instances ID to start : ")
          os.system("aws ec2 start-instances --instance-ids {}".format(instID))
        elif aws_serv == "8":
          instID = input("Enter the instances ID to stop : ")
          os.system("aws ec2 stop-instances --instance-ids {}".format(instID))
        elif aws_serv == "9":
          instID = input("Enter the instances ID to Terminate : ")
          os.system("aws ec2 terminate-instances --instance-ids {}".format(instID))
        elif aws_serv == "10":
          amiID = input("Enter the AMI ID : ")
          itype = input("Enter the instance type : ")
          sgID = input("Enter the security-group-ID to attach: ")
          subnetID = input("Enter the Subnet ID : ")
          count = input("Enter the number of instances to launch : ")
          keypair = input("Enter the key-pair to attach : ")
          ch1 = input("""Do You Want To add User Data File 1to run scripts : 
            1. Yes
            2. No
            choice: """)
          if ch1 == "1":
              userData = input("Enter the local path of user data file : ")
              os.system("aws ec2 run-instances --image-id {0} --instance-type {1} --security-group-ids {2} --subnet-id {3} --count {4} --key-name {5} --user-data=file://{6}".format(amiID,itype,sgID,subnetID,count,keypair,userData))
          elif ch1 == "2":
              os.system("aws ec2 run-instances --image-id {0} --instance-type {1} --security-group-ids {2} --subnet-id {3} --count {4} --key-name {5} ".format(amiID,itype,sgID,subnetID,count,keypair))
          else:
              print("Invalid choice")
        elif aws_serv == "11":
          size = input("Enter the size of volume in gb : ")
          vtype = input("Enter the volume type : ")
          az = input("Enter the Availibilty zone : ")
          os.system("aws ec2 create-volume --size {0} --volume-type {1} --availability-zone {2} ".format(size,vtype,az))
        elif aws_serv == "12":
          volID = input("Enter the volume ID : ")
          os.system("aws ec2 delete-volume --volume-id {}".format(volID))
        elif aws_serv == "13":
          volID = input("Enter the volume ID : ")
          os.system("aws ec2 detach-volume --volume-id {}".format(volID))
        elif aws_serv == "14":
          volID = input("Enter the volume ID : ")
          instID = input("Enter the instance ID : ")
          os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/sdf".format(volID,instID))
        elif aws_serv == "15":
          bucketName = input("Enter the bucket name : ")
          region = input("Enter the region : ")
          access = input("Enter the permission : ")
          lc = input("Enter the location constraint : ")
          os.system("aws s3api create-bucket --bucket {0} --region {1} --ac {2} --create-bucket-configuration LocationConstraint={3}".format(bucketName,region,access,lc))
        elif aws_serv == "16":
          path = input("Enter the local path of file to upload : ")
          bucketName = input("Enter the bucket name to upload : ")
          fileName = input("Enter the File name to save as : ")
          access = input("Enter the permission : ")
          os.system("aws s3 cp {0} s3://{1}/{2}.jpg --ac {3} ".format(path,bucketName,fileName,access))
        elif aws_serv == "17":
          origin = input("Enter the origin domain name : ")
          os.system("aws cloudfront create-distribution --origin-domain-name {}".format(origin))
        elif aws_serv == "18":
          print("Return to main menu")
          break
        else:
          print("Inavlid Choice")      
    elif(check_input == 8):
      ansible_input = input("Configure Ansible (Local/Remort): ")
      if ansible_input == "local":
        print("Installing ansible and configuring ansible files")
        os.system("yum install python36 -y")
        os.system("pip3 install ansible")
        os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
        os.system("yum install sshpass -y")
        os.system("mkdir /etc/ansible")
        os.system("touch /etc/ansible/ansible.cfg")
        ansible_file = open("/etc/ansible/ansible.cfg","w")
        ansible_file.write("[defaults]\ninventory=/root/inventory\n")
        ansible_file.close()
        print("-------------------------------------------------",end="")
        print("""
Note: Setting the inventory file to /root/inventory.txt
""",end="")
        print("-------------------------------------------------")
        managed_node_ip = input("Enter the Managed Node IP: ")
        managed_node_user= input("Enter the Managed node User: ")
        managed_node_pass = input("Enter the Managed Node Password: ")
        os.system("touch /root/inventory.txt")
        inventory_file = open("/root/inventory.txt", "w")
        inventory_file.write("{} ansible_user={} ansible_ssh_pass={} absible_connection=ssh\n".format(managed_node_ip,managed_node_user,managed_node_pass))
        inventory_file.close()     
        os.system("systemctl stop firewalld")
        print("Installation => Successful")
        print("--------------------------------------------------")
      elif ansible_input == "remote":
        print("remote")
    elif check_input == 9:
      exit() 
      print("###################### THANKS #######################")
    else:
      print("Invalid Choice")
 elif (check_input == 9):
   print("###################### THANKS #######################")
   exit()
 else:
   print("Invalid Input")
