from locust import task, run_single_user
from locust import FastHttpUser


class sample(FastHttpUser):
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
            "GET",
            "https://accounts.youtube.com/accounts/CheckConnection?pmpo=https%3A%2F%2Faccounts.google.com&v=1950384237&timestamp=1691896215996",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896216286&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZGY3YWRiYjZjLTAyMGRjMDU0ZjFiZDg5LTQyMDE1NzE5LTE0NDAwMC0xODllY2RmN2FkYzE5YzQiLCJncm91cHMiOnt9fQ%3D%3D",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896216372&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZGY3YjMxMWE5ZS0wMGQ3ODIyYjU1MDUxMS00MjAxNTcxOS04OGZlMC0xODllY2RmN2IzMjFjZWIiLCJncm91cHMiOnt9fQ%3D%3D",
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,0]]],558,[["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]]],"1691896216435",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,0]]],558,[["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[null,null,3,[null,"S2130894800:1691896214948105"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,690,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691896216902",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,1]]],558,[["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691896217000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]]],"1691896217102",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,1]]],558,[["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[null,null,3,[null,"S2130894800:1691896214948105"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,690,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691896217156",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896217282&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZGY3ZWJmNzE0LTA5YjdhYTMxMjVlM2M5LTQyMDE1NzE5LTg4ZmUwLTE4OWVjZGY3ZWMwZDBmIiwiZ3JvdXBzIjp7fX0%3D",
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,2]]],558,[["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691896217000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]]],"1691896217613",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,2]]],558,[["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[null,null,3,[null,"S2130894800:1691896214948105"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,690,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691896217646",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://accounts.google.com/_/signin/oauth?authuser=2&hl=en&_reqid=72618&rt=j",
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
            data="access_type=online&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&prompt=select_account&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&response_type=code&scope=openid%20profile%20email&service=lso&o2v=2&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hAOBTyryhG-H_kCHJ1xLCCAVpquVbSEeld08c46vk2vFsJbe5Iv7dxywRHxgXCDCMKq5YAJQtO6hs2tLO4FR_LBQvVjHqBZHjOjyqakKJ-dgODPdE8UyM3oV_-dkaqfghRcuB_hT0iHNJKHxqDHe8omhDFMVJlV4Yzam5-xpJq3bHTarlhpfeeqLovwF8b-QUkXv-Ay93aLfX51brTKw9lzIr_wsCZxKtBEZgIz-Xpf_bJ5OFFHgm54Bg-NlFQmG2Qi2h73XLwXPJTKJaExHfTkQg9xzv5zTNhE2yBs8K9NXSxPg8xfFSu-fNBu-mFFLMCLBpx7tQSGcc6H4892NsYU8AXBEQqMzOjUnd3hFxztUO3Kq9ShNNECsnusXsGKkUao6WKHUyqAdnLZDZ-Ri52-0-aV1UAzWNoXXSahePM0hXLsDRCEST6O34TDcpkg8JYNUFnlGFXFwWhHRLgwvEVUGFrKk5dMt5RK3FSmlIeDzSkoEqqQ%26as%3DS2130894800%253A1691896214948105%26client_id%3D87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%23&f.req=%5B%22AEThLlxs4myE6x-HOiF4oaIwK516-pzXXyAhJmmWCNeYp0c3VUlWBzGYnn61-ZUTUZ636SQsnofukhZ3Yo0cZNhOD3VBWTXqcIiSRERsXf_XEGqpy2034scLD8Bc0A-bxS-LA_Uyxiq2Ki8r4wH3yeEK3FgCcocABTtGGeUmjGtZLduGJCGdlQb7uZSuA1_HfGd8fKTVaRpsiPmhCL3vD_qmz0SYhy_x4jEO1rZbltdueo20PLOQeVgShTjpK7H7xtOcthiMKsac2cxV6wyqDW1m43TrxFe1yrl1DWEm9GxzXHwnLGJc8HxYXjHGdF1oVUJl1SUhweNinL9YF78AEfS3Sq7Yi31emyJdD0dO9xNT23lVjNPD5O8w6H51nvLAxy_7CdlBU4hodIZf19JcQL0ZfM5_D8NhP-ja_DFhQlu5GkXKu2BPwTMzbEusTq6E-Ad05i5rXJ4Je5HKxcJn9iwsuRISfq3OHjP7SbEBGaXJxPDUWSWFG9wHKvh1cEp9bW_xps1rCFbqdiPsh9-YcOi-CFbFhDwwNLASaHrWrbhsob1aEAeGPCnwd49os4OshOzOzo8MA-WGaxQg_CRbKOm4O0onloxkts-yPcAlYBmmaFbKFGJ0BJOgIza3qDcJ9ohwFxPy5b2qNG74rntwTji1MpxcEzT_HGuHo_RyOpaQby-L7G7uGm-Tq-fN9IFHbteH2lfCWrGGuVwRgMmXsOFnlKuUt8jWQXW36IkFpHGNf6-qf9IkErHKoFkCBlggpLkTsapxqGRpoLQ3egV5kx4OuoqG-7YMZHfzRAcWehP_xz0Ff6_IcW_IRJMUboOmOEuinUeyXJi1K_9cLI_TQWJvPeDPEWXVwAi6X9_O46XqaRhCRTRpYjvTdOCwYH9Nj320pvNaf4dmOjztzhiLxiDN5cuAHMJougZyS-rTXhhnkKiwpa0nCGIl5tWgJdm7xp6Rj8wbYbbrJeJ0RVI14RquKTIWvM2eYXQQKm-iPq2jkLj2Qf62nZM9NPWmhJ7nuBd9JS1bSEQ7YD0NBqAXd9fQECpk_UIx3xbjhjwLdKU6uksWP2RXPJ7fP5hPEDWI_aW2LLsbbR2Jl4ho7PQy9rDFs3Y_kb-wOQ%22%2C2%2C0%2Cnull%2C%5Bnull%2Cnull%2C%5B2%2C1%2Cnull%2C1%2C%22https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%3Faccess_type%3Donline%26scope%3Dopenid%2Bprofile%2Bemail%26prompt%3Dselect_account%26response_type%3Dcode%26client_id%3D87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%26redirect_uri%3Dhttps%253A%252F%252Fprairielearn.ok.ubc.ca%252Fpl%252Foauth2callback%22%2Cnull%2C%5B%5D%2C4%2C%5B%5D%2C%22GeneralOAuthFlow%22%2Cnull%2C%5B%5D%2C1%5D%2C10%2C%5Bnull%2C%2287886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%22%2C%5B%5D%2C%22!ChRad1BiSDgtT3Jzc0VORUdkVEdNShIfTTFfUjBxOHNmR2NVa013TWpqbVNUV1VTWFBmTm5oZw%E2%88%99AHkTZLMAAAAAZNmbFm-ZKJgdOFdBprv7kyftPPMd0pAP%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22https%3A%2F%2Fprairielearn.ok.ubc.ca%22%2C%22S2130894800%3A1691896214948105%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%22fa662f2e-e068-41dc-821a-8b0930cedc30%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2C14%2Cnull%2Cnull%2C%5B%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5B%5Bnull%2C9315%5D%2C%5Bnull%2C204%5D%2C%5Bnull%2C202%5D%5D%2Cnull%2C1%2Cnull%2Cnull%2C1%5D%2Cnull%2Cnull%2C2%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2C3%5D%5D&bgRequest=%5B%22oauth-account-chooser%22%2C%22%3CKuZq5rsCAAaC65vKouuNvWIY0JhGlZ_0ADkAIwj8Rpb3n4ViCf15mML7fUPLmYYJ4Ikg905TpkS01FjM6amJ45FRvOSAiq0tRfL4ePd08e0eSDjNAAABwp0AAAAIpwEHVgOnrw4WMshYssHAajQW7XQzgg5DFYdMIbW_uQHKO0pkQmeM4pBl8B1NDdcUdh5lhivHPmcFneboQ8bn0ZiNVcWfIqra3_kG1EAIThEnnl4xgrtVWZsF4Zo_nU5nj1EPq45dyzr8vsRsNt0yLiOCX65hifIzdChHVJKgr2CdAdFIsAVG9PIgYg6s7nIc55M42IbCG7NgwVZxSaDuiXHBVLs8PJHBWe96lCuhfkCD9uszUWPb2CFjrUa0uhX8Yx6bpWTxpprTyPTH5M2KPlj8DpyJ5pzRKmAxz-92sjn3NrVEtdJ5YS3rhmT6LZG86cLM_0cie4L80kSaGimfLv6n868ACQEi7r2ICimd13hUyQvdPbTX2CFvM97jXM7TzTO34QeW2ZxV1nAU7QpvtB8pjv48-_Kz8OdnsxxsCUg8yTnOWStHdgm6NOjODjwquqnQZ9WJ4QOPBx2BEjGWfAd1L8aQwEoNJooBrwZe-A53foS3V0Yzd5ncWeDqnwITuy-Zbn9RvlHr9Gb5DJY4rZ61H52KyOoZ02-sNLOd2QuA9y2lVY3Yhn_X7ZRnPho135SO5QWTHJU6W1EIywvV4A26RzmmV_aZsn6foWAP9yiMDSQYlvueKX62qoNY_bh9DpO_6g9VjQis8ghJykeGJ2VXxOFHoIxiJdLdefUDUJHT-kiXu9XruAsD4XdbkkiEa6Q7JEuAag5SVCZGT3-dy7HRAxmHnOnrgymnOLfpv1svXavejtoYNZYCQjaFsmDmBTJMNQw_TGIt0B7r6kt4pppRyOwiX6TYnocPePNVE05_fqdcN374TXIdkUv8bUOmtPP5-SCoensWob2gMjN8331XVhwv5NphjwE6en9o1LNQlHlP9Xg4loWhwp-urrq_RqaqBYvfvL-5n0-TkanPNdPKPoSLMvDd187fTXtFBEJmNg1s098icpjKFPBkG2hF_fHl68PDROlt_RDj4Dj8NG9m_KIT4lBKUZ-5kwNvqEl4B31eN8jKckO3x2kZIpX0z_-PjE68U8Bgh45yOPHQuqA-ImQquLDYkK5kbSCMw_DeEyVxTnJkDIWrfPUASYpSvwpvECl4CYU_YoB8q73g7hDXTiTjtbBW-RPWrMVxiSoMD0AyCE0AA1x9PBZ7SYUlkGWq2dGPXuR28P59304QqBs0Nw5ccYk8aL7iatGPe5ro_nmyfF7L0iR7A3Pc--pql4GRo26zvi1y1EZLPgToPFRbCR3vxgygg4DDbjQ%22%5D&at=AFoagUXXEjdPpaNo95wm--n0k3giZewvJQ%3A1691896215024&azt=AFoagUXXEjdPpaNo95wm--n0k3giZewvJQ%3A1691896215024&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22CA%22%2Cnull%2Cnull%2Cnull%2C%22GeneralOAuthFlow%22%2Cnull%2C%5Bnull%2C%2287886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%22%2C%5B%5D%2C%22!ChRad1BiSDgtT3Jzc0VORUdkVEdNShIfTTFfUjBxOHNmR2NVa013TWpqbVNUV1VTWFBmTm5oZw%E2%88%99AHkTZLMAAAAAZNmbFm-ZKJgdOFdBprv7kyftPPMd0pAP%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22https%3A%2F%2Fprairielearn.ok.ubc.ca%22%2C%22S2130894800%3A1691896214948105%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%22fa662f2e-e068-41dc-821a-8b0930cedc30%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2C14%2Cnull%2Cnull%2C%5B%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5B%5Bnull%2C9315%5D%2C%5Bnull%2C204%5D%2C%5Bnull%2C202%5D%5D%2Cnull%2C1%2Cnull%2Cnull%2C1%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GeneralOAuthFlow&checkConnection=youtube%3A176%3A0&checkedDomains=youtube&",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://accounts.google.com/signin/oauth/consent?authuser=2&part=AJi8hAOBTyryhG-H_kCHJ1xLCCAVpquVbSEeld08c46vk2vFsJbe5Iv7dxywRHxgXCDCMKq5YAJQtO6hs2tLO4FR_LBQvVjHqBZHjOjyqakKJ-dgODPdE8UyM3oV_-dkaqfghRcuB_hT0iHNJKHxqDHe8omhDFMVJlV4Yzam5-xpJq3bHTarlhpfeeqLovwF8b-QUkXv-Ay93aLfX51brTKw9lzIr_wsCZxKtBEZgIz-Xpf_bJ5OFFHgm54Bg-NlFQmG2Qi2h73XLwXPJTKJaExHfTkQg9xzv5zTNhE2yBs8K9NXSxPg8xfFSu-fNBu-mFFLMCLBpx7tQSGcc6H4892NsYU8AXBEQqMzOjUnd3hFxztUO3Kq9ShNNECsnusXsGKkUao6WKHUyqAdnLZDZ-Ri52-0-aV1UAzWNoXXSahePM0hXLsDRCEST6O34TDcpkg8JYNUFnlGFXFwWhHRLgwvEVUGFrKk5dMt5RK3FSmlIeDzSkoEqqQ&as=S2130894800%3A1691896214948105&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&pli=1&rapt=AEjHL4PJzHW9MCHZh5D0XhVVu9bdnCQXUAbLMfrogB8Hun4MvXWPQfsGPH6FcMTDiJ6Mwrlaq1_WqEP1cqV0606NRYV0iGZqJg",
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,3]]],558,[["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691896217000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]],["1691896217000",null,[],null,null,null,null,"[[[196,37066,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],6,null,null,null,null,null,[]],["1691896217000",null,[],null,null,null,null,"[[[296,37131,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],7,null,null,null,null,null,[]]],"1691896218450",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,3]]],558,[["1691896216000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S2130894800:1691896214948105"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691896216000",null,[],null,null,null,null,"[null,null,3,[null,"S2130894800:1691896214948105"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,690,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691896218470",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/oauth2callback?code=4%2F0Adeu5BU2lj_oaPO9aFRTGwRcfbcCSZIk-xWJqBqMYp5kr0wjOuZljaoAdV8agcrqqUwbTw&scope=email+profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&authuser=2&prompt=none",
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
            "GET",
            "/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=NzRkM2E1YWM3MWUwOWM3ZmMzZWRjN2UyNmM0YzAzZGMyOTExYmQyZWJlY2JkZjQzOTRhZWVkZWIzZDI3NTdkNg.ll8vbpk9.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896219514&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZGY4Nzc3MTEzOS0wZTk4ZjliNzUyZTYzNi00MjAxNTcxOS04OGZlMC0xODllY2RmODc3ODFkYWUiLCJncm91cHMiOnt9fQ%3D%3D",
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
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=M2U2NTlmM2FhNzY4MmZkODRlMjIxZmZkYmU3MjdhMTcxY2FkYTk1YjM2N2MyZWRiMzczYWQ4NDA3ZWQwMzdjYg.ll8vbpl2.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=MTM1YjAxNjM3OGI5YTUzNDc0ZWU2Y2UwYmRmMGE0ZWRjMjllYTZiYjI1Y2VmNjQ0YzAzYjNjMzVlMzhhMjQ5Yg.ll8vbrtl.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896222291&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZGY5MjRmYTU2LTA1ZmY4ZDAyMTA1MDUtNDIwMTU3MTktODhmZTAtMTg5ZWNkZjkyNTA3Y2IiLCJncm91cHMiOnt9fQ%3D%3D",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/course_instance/27/assessment_instance/12/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=OWRiMmQyMGQ4MjBjMzI1MDgwM2IxZmJhNmQ2ZTQxNjE3OTI3NjM3MmVmZDgwNDlmMjVjNGY2MTQ3OWE5ZGVkZg.ll8vbru7.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896224179&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZGY5OWIwOWVhLTAzMTNjMWI0NjM3Y2JjLTQyMDE1NzE5LTg4ZmUwLTE4OWVjZGY5OWIxMThkMCIsImdyb3VwcyI6e319",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/course_instance/27/instance_question/691/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=YjJhNDQ0MWRiOGM0NDMzMGIxM2IzMGRkMGJhNzE5NDgyODEzODQzMzliMzJkODRkYTk0YWU0NDk4MjkwM2IwMg.ll8vbtag.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
                "Host": "prairielearn.ok.ubc.ca",
                "Referer": "https://prairielearn.ok.ubc.ca/pl/course_instance/27/assessment_instance/12/",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691896227118&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjZGZhNTJiMWIwOC0wM2U1YzYxYjVkZTdmMi00MjAxNTcxOS04OGZlMC0xODllY2RmYTUyYzFjNjciLCJncm91cHMiOnt9fQ%3D%3D",
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(sample)
