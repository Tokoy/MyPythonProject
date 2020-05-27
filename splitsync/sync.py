import os,sys
import paramiko
import jsonlist

#传入源ip和目标ip和源文件路径和目标文件路径

def sync_data(source_ip,source_pw,target_ip,target_pw,filedir):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(source_ip,22,"root",source_pw,timeout=5)
    shell_command = 'sshpass -p "%s" scp -r -o StrictHostKeyChecking=no %s root@%s:%s' % (target_pw,filedir,target_ip,filedir)
    stdin, stdout, stderr = ssh.exec_command("apt-get install sshpass -y")
    stdin, stdout, stderr = ssh.exec_command(shell_command)
    print(stdout.read())
    print('%s OK\n' % (target_ip))
    ssh.close()
    jsonlist.change_json_status('ips.json',source_ip,"1")
    jsonlist.change_json_status('ips.json',target_ip,"1")


def sync_data(source_ip,source_pw,target_ip,target_pw,filedir,jdata):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(source_ip,22,"root",source_pw,timeout=5)
    shell_command = 'sshpass -p "%s" scp -r -o StrictHostKeyChecking=no %s root@%s:%s' % (target_pw,filedir,target_ip,filedir)
    stdin, stdout, stderr = ssh.exec_command("apt-get install sshpass -y")
    stdin, stdout, stderr = ssh.exec_command(shell_command)
    print(stdout.read())
    print('%s OK\n' % (target_ip))
    ssh.close()
    jsonlist.change_jdata(jdata,source_ip,"1")
    jsonlist.change_jdata(jdata,target_ip,"1")
