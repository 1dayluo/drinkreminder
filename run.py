from config import *
import requests
import datetime
import yaml
import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_config():
	with open(YAML_PATH, 'r') as f:
		configurations = yaml.load(f.read(), Loader=yaml.FullLoader)
	return configurations

def get_token():
	appid = APIID
	secret = APISECRET
	if r.get('vx_token') is None:
		url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}"
		resp = requests.get(url).json()
		token = resp["access_token"]
		expires_in = resp["expires_in"]
		r.set('vx_token',token,px=expires_in)
		return token
	else:
		print('[-]get new token')
		return r.get('vx_token')

def drink_times(number):
	if number <= 7:
		r.set('dundundun',number)
	elif number >= 8:
		r.set('dundundun', 1)
		r.set('start',0)


def get_time():
	if r.get('dundundun') is not None:
		return r.get('dundundun')
	else:
		r.set('dundundun',1)
		r.set('start',1)
		return 1


def post_msg():
	url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + get_token()
	this_time = get_time()

	if r.get('start') is None or r.get('start') == '1':
		SEND_T['data']['meow']['value'] = SEND_T['data']['meow']['value'].format(this_time)	
		SEND_T['template_id'] =TPL_ID
		for user in USER_LIST:
			try:
				SEND_T['touser'] = user
				send = json.dumps(SEND_T,ensure_ascii=False).encode()
				resp = requests.post(url,data=send)
				if resp.json()['errcode'] != 0:
					print('[*]error:'+ resp.json()['errmsg'])
			except Exception as e:
				print('[-]',e)
			finally:
				drink_times(int(this_time)+1)
				print('[+]Send post success!')
def main():
	
	today = datetime.date.today().strftime("%Y%m%d")
	if r.get('send_day') is None:
		r.set('send_day',today)
	elif today != r.get('send_day'):
		r.set('send_day',today)
		if r.get('start') == '0':
			r.set('start',1)
	post_msg()
if __name__ == '__main__':
	# token = get_token(appid, appsecret)
	main()
