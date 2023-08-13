from locust import task, run_single_user
from locust import FastHttpUser


class sample2_sql(FastHttpUser):
    host = "https://prairielearn.ok.ubc.ca"
    default_headers = {
        "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/pl/oauth2login",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D",
                "Host": "prairielearn.ok.ubc.ca",
                "Referer": "https://prairielearn.ok.ubc.ca/pl/login",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://accounts.google.com/o/oauth2/v2/auth?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "referer": "https://prairielearn.ok.ubc.ca/",
                "sec-ch-ua-arch": '""',
                "sec-ch-ua-bitness": '"64"',
                "sec-ch-ua-full-version": '"113.0.5672.127"',
                "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.127", "Chromium";v="113.0.5672.127", "Not-A.Brand";v="24.0.0.0"',
                "sec-ch-ua-model": '"Nexus 5"',
                "sec-ch-ua-platform-version": '"6.0"',
                "sec-ch-ua-wow64": "?0",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "cross-site",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
                "x-chrome-id-consistency-request": "version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fa662f2e-e068-41dc-821a-8b0930cedc30,sync_account_id=112905861928398825341,signin_mode=all_accounts,signout_mode=show_confirmation",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896255027&ver=1.57.2",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://accounts.google.com",
                "referer": "https://accounts.google.com/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZTAxMjJmZTYwLTAwNDNmZTA5MGU3NWEzLTQyMDE1NzE5LTg4ZmUwLTE4OWVjZTAxMjMwMTI5ZiIsImdyb3VwcyI6e319",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://accounts.youtube.com/accounts/CheckConnection?pmpo=https%3A%2F%2Faccounts.google.com&v=1285640873&timestamp=1691896255068",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "referer": "https://accounts.google.com/",
                "sec-fetch-dest": "iframe",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "cross-site",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
                "x-client-data": "CJa2yQEIprbJAQipncoBCKKJywEIlaHLAQiFoM0BCOSwzQEI3L3NAQi7vs0BCO7EzQEItsjNAQjxyc0BCLnKzQEYwMvMAQ==",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896255392&ver=1.57.2",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://accounts.youtube.com",
                "referer": "https://accounts.youtube.com/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZTAxMzlkY2ZmLTA0ZTlhNWFhZjQ5N2I1LTQyMDE1NzE5LTE0NDAwMC0xODllY2UwMTM5ZTFjOWUiLCJncm91cHMiOnt9fQ%3D%3D",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true",
            headers={
                "Authorization": "SAPISIDHASH 26bae71a5a8b5c8d6be8f719b272c3efa3d3e307",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Referer": "https://accounts.google.com/",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,0]]],558,[["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]]],"1691896255644",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://accounts.google.com/_/bscframe",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "referer": "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",
                "sec-ch-ua-arch": '""',
                "sec-ch-ua-bitness": '"64"',
                "sec-ch-ua-full-version": '"113.0.5672.127"',
                "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.127", "Chromium";v="113.0.5672.127", "Not-A.Brand";v="24.0.0.0"',
                "sec-ch-ua-model": '"Nexus 5"',
                "sec-ch-ua-platform-version": '"6.0"',
                "sec-ch-ua-wow64": "?0",
                "sec-fetch-dest": "iframe",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
                "x-chrome-id-consistency-request": "version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fa662f2e-e068-41dc-821a-8b0930cedc30,sync_account_id=112905861928398825341,signin_mode=all_accounts,signout_mode=show_confirmation",
                "x-client-data": "CJa2yQEIprbJAQipncoBCKKJywEIlaHLAQiFoM0BCOSwzQEI3L3NAQi7vs0BCO7EzQEItsjNAQjxyc0BCLnKzQEYwMvMAQ==",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true",
            headers={
                "Authorization": "SAPISIDHASH 26bae71a5a8b5c8d6be8f719b272c3efa3d3e307",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Referer": "https://accounts.google.com/",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,0]]],558,[["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[null,null,3,[null,"S-2096166166:1691896253911524"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,1062,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691896255823",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896256003&ver=1.57.2",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://accounts.google.com",
                "referer": "https://accounts.google.com/",
                "sec-ch-ua-arch": '""',
                "sec-ch-ua-bitness": '"64"',
                "sec-ch-ua-full-version": '"113.0.5672.127"',
                "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.127", "Chromium";v="113.0.5672.127", "Not-A.Brand";v="24.0.0.0"',
                "sec-ch-ua-model": '"Nexus 5"',
                "sec-ch-ua-platform-version": '"6.0"',
                "sec-ch-ua-wow64": "?0",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZTAxNjAwMTk1Ni0wMjRlNzMyZGNlYzg1MS00MjAxNTcxOS04OGZlMC0xODllY2UwMTYwMTFhZWMiLCJncm91cHMiOnt9fQ%3D%3D",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true",
            headers={
                "Authorization": "SAPISIDHASH 26bae71a5a8b5c8d6be8f719b272c3efa3d3e307",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Referer": "https://accounts.google.com/",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,1]]],558,[["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]]],"1691896256041",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true",
            headers={
                "Authorization": "SAPISIDHASH 26bae71a5a8b5c8d6be8f719b272c3efa3d3e307",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Referer": "https://accounts.google.com/",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,1]]],558,[["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[null,null,3,[null,"S-2096166166:1691896253911524"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,1062,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691896256060",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true",
            headers={
                "Authorization": "SAPISIDHASH 26bae71a5a8b5c8d6be8f719b272c3efa3d3e307",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Referer": "https://accounts.google.com/",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,2]]],558,[["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]]],"1691896256517",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true",
            headers={
                "Authorization": "SAPISIDHASH 26bae71a5a8b5c8d6be8f719b272c3efa3d3e307",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Referer": "https://accounts.google.com/",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,2]]],558,[["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[null,null,3,[null,"S-2096166166:1691896253911524"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,1062,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691896256601",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://accounts.google.com/_/signin/oauth?authuser=2&hl=en&_reqid=72657&rt=j",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                "google-accounts-xsrf": "1",
                "origin": "https://accounts.google.com",
                "referer": "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",
                "sec-ch-ua-arch": '""',
                "sec-ch-ua-bitness": '"64"',
                "sec-ch-ua-full-version": '"113.0.5672.127"',
                "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.127", "Chromium";v="113.0.5672.127", "Not-A.Brand";v="24.0.0.0"',
                "sec-ch-ua-model": '"Nexus 5"',
                "sec-ch-ua-platform-version": '"6.0"',
                "sec-ch-ua-wow64": "?0",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
                "x-chrome-id-consistency-request": "version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fa662f2e-e068-41dc-821a-8b0930cedc30,sync_account_id=112905861928398825341,signin_mode=all_accounts,signout_mode=show_confirmation",
                "x-client-data": "CJa2yQEIprbJAQipncoBCKKJywEIlaHLAQiFoM0BCOSwzQEI3L3NAQi7vs0BCO7EzQEItsjNAQjxyc0BCLnKzQEYwMvMAQ==",
                "x-same-domain": "1",
            },
            data="access_type=online&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&prompt=select_account&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&response_type=code&scope=openid%20profile%20email&service=lso&o2v=2&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hANeI0BeY56k_Ckg9bvnuh4uuSs9sEPgHyWjJALzXXj_QGHHVf2y5i07NvuOThe7Q_NjL5H3fPdGLnvl2so4DPABx0-0FVFqz4hSQMktJdfRAJOSo420BUPy-mg5lwwMPKP7roEIWXPW30MrDmmv3guRy5T7mPbUDJ2MDKNUKe7P-0kLKRW2vtPZfDulwyihPIHScqCxvUnFo2mk27Rz5-3Q2wEtDnbXeoq07cJjyTuMGKbvMmJ7MYsQjDINBRIQ6Qo8hD-KbyR77hPu-yEMGV_aahwZ4HnZQy2ta1MucnX5AJL0SkE5DB0OmShvQ-P3EPGmAaaakgWlTMarwHca7aQ02Qoo3O9swg8Smn1hAF0MKJvXacn_iNyknkeE8iJgp1rG6iJC37LBHVt22JDy5U0KrYgSGi8f4WUyNnBzkA38-pguZ-NX0FXPyRKXtMMfPn5zjDJs49SXvMeTUkFVdGobrAbAdd-Gays4cdHOku-hNBFMMUQ%26as%3DS-2096166166%253A1691896253911524%26client_id%3D87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%23&f.req=%5B%22AEThLlzufhCA5gVYhUIBSmUXVkLAmo53hGM6beXwShoPl0J5rB_UeYjpqj_-yXHcpkrk_Oajtaa51CJ-SYX6QGgdywoJo9sA1Iv0_hYNtsy5osQ2P2Glz1bPjVQc_inuOtQc6aJGxOxd9I38p0LIfZnO0BUSent1YkYUAnXfUSr_XSUQAgKP_eymwXSXCqJ_Q-Gf8J9h3JgHqPrOqvlzv2wrPDvq9JDDFX92FZfnGuN57zyn30v6HyZBwB7PEyBXFMOWU5ikKtnWnRfWpKhsnR5sC6yknyk3hmRa3DU4Of8aw-z_3oX7L_aLIwMja1dvyP3uFLeBsP0QrVVqGR1orxwwLdtpi8TedWueMAuyPkFysTNT0Bo21RfEMxJlmC42nQShBRRSfN_Np37UP5t8mhTYv7pJtand2yj0ZV4km80vZ9dwRaBW1VmYQhL51o-B2j3YEfWuahUrji11_--W4eL1SH6SRZf7Tn9Pe4JvQLrzwWkoYOdQIq9oWUBslG8c9MbA-etjlwihMXCAW6GP-qrnXg_yL_M6m6GtbhxS8g3ygu4B2UJIIVXg2yyVeNT_hGZ0r0t93oAkfmw6sxiN3d-XvHNsPjt24UckYE0aLY1EKOa79BUJPEXwTj-_p5fUoTqjirDe5VKbMFJiU_jgIn6xAyNHv_CO8sy7i7UbuhHM_eNkHNPJ0TfuF0rNIMnOqmlMwX9DmN7qIqs7VXniamyrjAVa3ipAWGGyz36ieflECw9Y9KaHuLud2Svv2ZHHCbQLmsta2TWY9ljFconNQ2fp3Nmw_NGKrbCqnT_UfZtgws9KXQyzrS9luJAM2kdfkFghmRc9Ay2a8PLZoDMMqb1zrcoTaNUP1_mFVCIHI_pWafhXBqw21OtdfG7r7L0qLWRjeR9UcmDjzExGXnRRfudTA4xAMJ5I7Lmh1g8gMwcGsATSXRZ1_L6BtS5-fqqsDBoDbwx08Ec5YLKA5xXglLVAa1u7CqUFmq1ZJcnt-oivGqB4TTPVwr4SkbimDp_NWhyWur61xJdW3qW5NTvsZaAWkF2qteK0bEpy0Lm6eOU7uZHJdfsMGAfmEWHi9Tqv-IBeIfdmiBPZ3HcrHHMmh8-OgMozuKZ-iQ%22%2C2%2C0%2Cnull%2C%5Bnull%2Cnull%2C%5B2%2C1%2Cnull%2C1%2C%22https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%3Faccess_type%3Donline%26scope%3Dopenid%2Bprofile%2Bemail%26prompt%3Dselect_account%26response_type%3Dcode%26client_id%3D87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%26redirect_uri%3Dhttps%253A%252F%252Fprairielearn.ok.ubc.ca%252Fpl%252Foauth2callback%22%2Cnull%2C%5B%5D%2C4%2C%5B%5D%2C%22GeneralOAuthFlow%22%2Cnull%2C%5B%5D%2C1%5D%2C10%2C%5Bnull%2C%2287886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%22%2C%5B%5D%2C%22!ChRUd2x6X1hBUnJLeVB5TFBLU0tPOBIfNHk0c1hLNEtYVXdjSU5vbEVpbVNxcUZGM3dET25oZw%E2%88%99AHkTZLMAAAAAZNmbPTUCE5dZKF7kT5xSlxyt59_gUxIf%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22https%3A%2F%2Fprairielearn.ok.ubc.ca%22%2C%22S-2096166166%3A1691896253911524%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%22fa662f2e-e068-41dc-821a-8b0930cedc30%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2C14%2Cnull%2Cnull%2C%5B%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5B%5Bnull%2C9315%5D%2C%5Bnull%2C204%5D%2C%5Bnull%2C202%5D%5D%2Cnull%2C1%2Cnull%2Cnull%2C1%5D%2Cnull%2Cnull%2C2%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2C3%5D%5D&bgRequest=%5B%22oauth-account-chooser%22%2C%22%3C3hJqEk8CAAaC65vKouuNqbkBpKW_Ucn0ADkAIwj8RkvOhPN-ZdSnSKOYNaTpiGwFU3qyArGX3OACRmar5k7N6VZBCPXybd4bWSodzaZl3cZcIUrNAAABg50AAAAKpwEHVgPJDoi3xMLCaj_-OwGkfG5HujgsOdj6ZHbd0AtV9lAnH1Ejk0uRefoDID9pLEJY1Iuf1FOTqLYBr4ZKVuFX6oNM_NvKnBR5-DShONlWhSPl-ljb-W2zmVY9ySFcQpX4uQZtQJqEGkJro7Vc9BtNPe1gRNHPRTLnIw_HYxs8upHSDsTPsLqOOycIUBwbw6pH9oomd-UBAG-BdiXYVwrDjjSKEYvHmlHiZqvvK020sH1UC1LaGmQY-pHf2s_FkNcxykvPg8t5tVfSbVBYQ8du_8qXoqYSn1QPVhAcZLqcYqQKg8AZfDzoaPaMwtOeEPL_Zvnxd4_UNxsHTD7gHC4A8PuUq2hzIAFLMS6LO3joLwLDjM9EM5FDLxzWgE3g-I0Z2G1IwgQyVDSOz2NScFhDGIZ6CBLR_TiKdKziQ0TrUHqnJo6XELZCUbDrP9msR42MpLpQnjjQPqTsJ40oYbrBVuPsRho8Er8amtJmRStMmCc0vpvBBH2pLl1vO3ojyIgNcU2EAGEHlJUmt9etG0OF2UmURc02m8mtmbrNqrwzGO3MtxYJozqH4Z7S_sF1rybYoo3nXufJhXjRvXOu8KXppoJJtqwwy1HlliqRyawxRpJi1e7HIPI_ePUCwNok075yT8aUnWVLj4qQzuRJmzKNJtVxaU040QSVrzrnDBV5NSToosFZEfEXx7AhcDYKaPUIwY9_2FlnZHpPd5HNknAiIdvudRbSSPnxoCIWTFei22xRjK7eBC4luds3g5CtPlCwHMi7XpJCplIdHbjlcfOwuOwA_7Fz6j-IrGGD3xxkWq68AMAWCHnRU0ch8iggRwCoFJzSU9vWew6HWWBKeAfI_qzGIFNNypIyxep-HLBK4s8Rh8kvBcSoqIqcaDD-9QaZPjiYTogbatVB7iEnsxkCbdHx6Njl1Tc6eY74aIXUurzbQQqPUlAzByLxKRA3RGEHsTzbZp5UG_gckiFxzig9aE_I0bfdOqT3PbkonOCCaJTkUA_YYRT9ASHo8fKizOwYc6nSFrSMAR3zlpCrXdJdzqmAClrzT50_dg_1GO7QQjHnn8dKLF7ViXprZv0ocos6dKxkrRvI2D0iYiswcu7sbrYLTMd2yBOMguQW2KU1ZzZ2lPsmVaTIxuDK7GhPcdXRC6F1TBz-WJSKq_7yqWFPdqiIkETEgrtR3aWR3_rSAX6IFuQiZcFB_lCNg3Pm6-3sQ7kA4qM_OfGX8J7TVHA1wIaYBTz8oyKdL3Xgh7Fwas7TCylF_6jvJX-TXO_SvFLjsZglFqXBm0c88OhK%22%5D&at=AFoagUWQouej44Y9YNB4owKmpElwxUDqQA%3A1691896254001&azt=AFoagUWQouej44Y9YNB4owKmpElwxUDqQA%3A1691896254001&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22CA%22%2Cnull%2Cnull%2Cnull%2C%22GeneralOAuthFlow%22%2Cnull%2C%5Bnull%2C%2287886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%22%2C%5B%5D%2C%22!ChRUd2x6X1hBUnJLeVB5TFBLU0tPOBIfNHk0c1hLNEtYVXdjSU5vbEVpbVNxcUZGM3dET25oZw%E2%88%99AHkTZLMAAAAAZNmbPTUCE5dZKF7kT5xSlxyt59_gUxIf%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22https%3A%2F%2Fprairielearn.ok.ubc.ca%22%2C%22S-2096166166%3A1691896253911524%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%22fa662f2e-e068-41dc-821a-8b0930cedc30%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2C14%2Cnull%2Cnull%2C%5B%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5B%5Bnull%2C9315%5D%2C%5Bnull%2C204%5D%2C%5Bnull%2C202%5D%5D%2Cnull%2C1%2Cnull%2Cnull%2C1%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GeneralOAuthFlow&checkConnection=youtube%3A174%3A0&checkedDomains=youtube&",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://accounts.google.com/signin/oauth/consent?authuser=2&part=AJi8hANeI0BeY56k_Ckg9bvnuh4uuSs9sEPgHyWjJALzXXj_QGHHVf2y5i07NvuOThe7Q_NjL5H3fPdGLnvl2so4DPABx0-0FVFqz4hSQMktJdfRAJOSo420BUPy-mg5lwwMPKP7roEIWXPW30MrDmmv3guRy5T7mPbUDJ2MDKNUKe7P-0kLKRW2vtPZfDulwyihPIHScqCxvUnFo2mk27Rz5-3Q2wEtDnbXeoq07cJjyTuMGKbvMmJ7MYsQjDINBRIQ6Qo8hD-KbyR77hPu-yEMGV_aahwZ4HnZQy2ta1MucnX5AJL0SkE5DB0OmShvQ-P3EPGmAaaakgWlTMarwHca7aQ02Qoo3O9swg8Smn1hAF0MKJvXacn_iNyknkeE8iJgp1rG6iJC37LBHVt22JDy5U0KrYgSGi8f4WUyNnBzkA38-pguZ-NX0FXPyRKXtMMfPn5zjDJs49SXvMeTUkFVdGobrAbAdd-Gays4cdHOku-hNBFMMUQ&as=S-2096166166%3A1691896253911524&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&pli=1&rapt=AEjHL4NJiNh4XrYjId4tLnhohDMSQ0LzFyJpwV9S9MdOlgBt7vr1b4hbMhj7k1NSZfW-bENRWwotvF1ozuc8a_oMrNq2x38mOg",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "referer": "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",
                "sec-ch-ua-arch": '""',
                "sec-ch-ua-bitness": '"64"',
                "sec-ch-ua-full-version": '"113.0.5672.127"',
                "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.127", "Chromium";v="113.0.5672.127", "Not-A.Brand";v="24.0.0.0"',
                "sec-ch-ua-model": '"Nexus 5"',
                "sec-ch-ua-platform-version": '"6.0"',
                "sec-ch-ua-wow64": "?0",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
                "x-chrome-id-consistency-request": "version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fa662f2e-e068-41dc-821a-8b0930cedc30,sync_account_id=112905861928398825341,signin_mode=all_accounts,signout_mode=show_confirmation",
                "x-client-data": "CJa2yQEIprbJAQipncoBCKKJywEIlaHLAQiFoM0BCOSwzQEI3L3NAQi7vs0BCO7EzQEItsjNAQjxyc0BCLnKzQEYwMvMAQ==",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true",
            headers={
                "Authorization": "SAPISIDHASH 26bae71a5a8b5c8d6be8f719b272c3efa3d3e307",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Referer": "https://accounts.google.com/",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,3]]],558,[["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]],["1691896256000",null,[],null,null,null,null,"[[[196,37066,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],6,null,null,null,null,null,[]],["1691896256000",null,[],null,null,null,null,"[[[296,37131,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],7,null,null,null,null,null,[]]],"1691896257322",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/oauth2callback?code=4%2F0Adeu5BUDtHcTIc5HtT-i5IS5M8r8bNRmgtbPoKH_GQKWFll3-Jf0CvOdASuwU3zcBz_7ig&scope=email+profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile&authuser=2&prompt=none",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D",
                "Host": "prairielearn.ok.ubc.ca",
                "Referer": "https://accounts.google.com/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true",
            headers={
                "Authorization": "SAPISIDHASH 26bae71a5a8b5c8d6be8f719b272c3efa3d3e307",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Referer": "https://accounts.google.com/",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,3]]],558,[["1691896255000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-2096166166:1691896253911524"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896255000",null,[],null,null,null,null,"[null,null,3,[null,"S-2096166166:1691896253911524"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,1062,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691896257462",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=MzFkYmY3MWQ3MWY5MzlkOTg0ZGUxMDQ0MzU1ZjgzODVjMTQxMjJiZDM3MDdlMzc1ZmI0YTE4NGU2NTQzYzUwMA.ll8vcjir.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
                "Host": "prairielearn.ok.ubc.ca",
                "Referer": "https://accounts.google.com/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896258317&ver=1.57.2",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://prairielearn.ok.ubc.ca",
                "referer": "https://prairielearn.ok.ubc.ca/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZTAxZjBhMWI4ZS0wODMyZDI3YmM5MDU0LTQyMDE1NzE5LTg4ZmUwLTE4OWVjZTAxZjBiMWJkYiIsImdyb3VwcyI6e319",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/course_instance/27",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=ODc4YWQ4ZWU0NzJhMjcwOGI2ZmM0YTEzMzYwYTZlODg5NTJiZGEwMDZiNjQzNDg2Y2YyMDg5MzBlZjExZGM0OQ.ll8vcjj9.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
                "Host": "prairielearn.ok.ubc.ca",
                "Referer": "https://prairielearn.ok.ubc.ca/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/course_instance/27/assessments",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=ZjUyOTllNzQ3MjQyMTc1NGY0YmQ5NmU2YzRkYjkyNGZlYzdkZjc3MWVjNWEwZTJmNjkwNGU0ZjVjZjdhNzczYg.ll8vckqc.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
                "Host": "prairielearn.ok.ubc.ca",
                "Referer": "https://prairielearn.ok.ubc.ca/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896259762&ver=1.57.2",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://prairielearn.ok.ubc.ca",
                "referer": "https://prairielearn.ok.ubc.ca/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZTAyNGFmYzZlLTAwMTQ4MTkzM2U3MmRmLTQyMDE1NzE5LTg4ZmUwLTE4OWVjZTAyNGIwMTE5MCIsImdyb3VwcyI6e319",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/course_instance/27/assessment_instance/13/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=MjEzZGUzMmE0YzM2NzRkMGNjYTZhY2ViNDQ4NjM4YjJjMzMzYzhiN2VmZDk3MDZkYjFkYjlkZjFjNzcwNDZmOA.ll8vckqt.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
                "Host": "prairielearn.ok.ubc.ca",
                "Referer": "https://prairielearn.ok.ubc.ca/pl/course_instance/27/assessments",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896261307&ver=1.57.2",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://prairielearn.ok.ubc.ca",
                "referer": "https://prairielearn.ok.ubc.ca/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZTAyYWI4ZmU0LTAxOTkxODcwNDA0ODZlLTQyMDE1NzE5LTg4ZmUwLTE4OWVjZTAyYWI5MTY1NSIsImdyb3VwcyI6e319",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/course_instance/27/instance_question/7271/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=NzBjMTU2Njc4ZTQ3NWIwOGJjOGQ1OTE4OGY4YmNhNDViYmQ3MzVmOTk3MDgxZDM0ZDQxNDNjN2QxZGE4NTU1NQ.ll8vclx3.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
                "Host": "prairielearn.ok.ubc.ca",
                "Referer": "https://prairielearn.ok.ubc.ca/pl/course_instance/27/assessment_instance/13/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896272143&ver=1.57.2",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://prairielearn.ok.ubc.ca",
                "referer": "https://prairielearn.ok.ubc.ca/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZTA1NTBjODc0LTAxOTQzYjcxNDZkYmI1LTQyMDE1NzE5LTg4ZmUwLTE4OWVjZTA1NTBkMWIzNSIsImdyb3VwcyI6e319",
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(sample2_sql)
