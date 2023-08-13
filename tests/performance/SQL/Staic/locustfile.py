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
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691893079847&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjYWY5ZjI0ZWQ4LTAwZmExYWFjNWVhYWU4LTQyMDE1NzE5LTg4ZmUwLTE4OWVjYWY5ZjI1MTgwNyIsImdyb3VwcyI6e319",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://accounts.youtube.com/accounts/CheckConnection?pmpo=https%3A%2F%2Faccounts.google.com&v=857335662&timestamp=1691893080013",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "referer": "https://accounts.google.com/",
                "sec-fetch-dest": "iframe",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "cross-site",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
                "x-client-data": "CJa2yQEIprbJAQipncoBCKKJywEIlaHLAQiFoM0BCOSwzQEI3L3NAQi7vs0BCO7EzQEItsjNAQjxyc0BCLnKzQEYwMvMAQ==",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691893080391&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjYWZhMTQ0MWIyNy0wMzk5ZGUwMzJhYTk0Yy00MjAxNTcxOS0xNDQwMDAtMTg5ZWNhZmExNDUxNTFlIiwiZ3JvdXBzIjp7fX0%3D",
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,0]]],558,[["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]]],"1691893080603",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,0]]],558,[["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[null,null,3,[null,"S-519885087:1691893072053304"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,1219,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691893080782",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,1]]],558,[["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]]],"1691893080873",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,1]]],558,[["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[null,null,3,[null,"S-519885087:1691893072053304"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,1219,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691893080988",[]]',
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691893081294&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjYWZhNGNiMTYxZS0wMWZjZTgyYWU1OGI5OC00MjAxNTcxOS04OGZlMC0xODllY2FmYTRjYzFiMDQiLCJncm91cHMiOnt9fQ%3D%3D",
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,2]]],558,[["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691893081000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]]],"1691893081328",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,2]]],558,[["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[null,null,3,[null,"S-519885087:1691893072053304"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,1219,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691893081423",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,3]]],558,[["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[null,null,3,[null,"S-519885087:1691893072053304"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,1219,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691893082215",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,3]]],558,[["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691893081000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]]],"1691893082262",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://accounts.google.com/_/signin/oauth?authuser=2&hl=en&_reqid=69484&rt=j",
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
            data="access_type=online&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&prompt=select_account&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&response_type=code&scope=openid%20profile%20email&service=lso&o2v=2&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hANvl0m3zpclqO1gUoIt7KFxzmVkf33FbPFC0X-FCvzclOKWUPjl2dIoCyiqoPWYYvkGO-ri7gmOmUs6U08vb3I8hl_51C3qKmN7O6-50x-fH3esgvn5uvTyLfl0Q8qy0OyNoVu57wjdkCGEGxjKd1oWK_b_U2ZZOfEKED3vws6hIRQgjqlVdNpbMyglBSiNgsLV-8eHST1SuLn1J-Zjs6_s-cbJpJ4ZWbvDNuQx3ELsVD2EyGOwTqlmhOci2Xq4S45fQsXt-sPzfpbNW0wu7Zhw7YWzf2nyFh5EL-qlDe6dL1O4x9-xzJJgYt_Zb2apcpLojsdawpwQfl_VE74ejlERZUj-A3rSw0rsXw5aQotedUVm2Wm3j7sH3dfwM_mlOQN9INT79BEiuJLFKUmsfLE-J-4zGpDDRcVMlP4rSqmugjhkWTICJJ7tPhALYQxggK0wzxBpyg1j9Bf9ocggiOZJ_bCYNEh_ROsD19QzMLNyq-VWhIg%26as%3DS-519885087%253A1691893072053304%26client_id%3D87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%23&f.req=%5B%22AEThLlzafBwc427rcssDL0SpWMY2ZRc1Zy_6T9u_PjF3IQMJ0027ZozLkRGtflt59NQXNdnu3JUd32JNNg2_sjr4dmDfZlnbWIBkgwUA1iZInzD3W-bWejTJmeg2nnXDAhX2Ah1eFgYYv7lamb1mDHevGCG34IFBAZjHNSY_gDhBRfQLieSWQfNM_3sKAJBYjJhZS1eNa4ySq8hw7GJwLpIFP7lHfo8ezoLpG4vs2W8zRoVc69IovGtMjyeSYn7VhQXvGdFz6r2JTdVZZK-l86oZeCsJqL4NCASNUi0AuPr02gzcIEpqmmkTffezvK2WwmaCSvZtTNEmvw_IwdX24jNxjJ6K3XLPdHRXHfMEZOuN26iNhDZXZotjhMPXOF0vvlsBqT7KL4HFQKKHLQrLmbYhDbWDJCBbOys-8c_FSEcIf0bL8JiWk8syoBjDup4jPlTV7JB_Km2y--UWLDUOZnpdzoD1DEPpfbpQNZBN5ytSRzuxh2ChCOTrde2LdrmiYXmOGs4wj4KxKSP-3hZXv9zcBETrNq2t0m_y0LEPSg8ih5gUN2FDrrr8O-jfBMvg17KiiVRV5aD1BHz-bgW4wnUpCgiRRpluxNUol42XrHCeLHvpGxcm65oaEQM2tgTfatXy-1HOkwfZUPRlzERY6eu06PqqiOZYVIUuSu54Ra6QPufbH-ZK4_iNlFUUH7kpHSLhIW18nF8ISMQ9VFp9X6LioKPJ74LEVCD1pFx5sGuN71jixlWQqwkv96jykI45X3lo56_htKfD55XRbPoV2BAOlshJ5NiNrXHg23sHuruPcFXhVEChEzswaWXIe9ofrcYcwrEnGUiWTTAi5HMRgdfrnOJUGWhjlX4tU184Vv209G2nvxCNmXaFen2-H9mvD7lwdp-OzsILnzkt1ejK-Xdr473ypy7zNbfmASw6N8cGHDcqjbwSVEmkr0EdDK-3TXGJL3dzj-wDGrzBZ3_-9RjSsaWZdeqYDgsO4o9VNTD7XZKRlZ2nclubYm8me-iZ6WP4cr6P134dYQ6ShD4yPAHSnIUpP3gMISaG3_gV-UUdUtnT5s6Mo7VyT-ujmx35Rs_-KjXV9NVrmX41ZUlGkxk2JxO_-UdvqA%22%2C2%2C0%2Cnull%2C%5Bnull%2Cnull%2C%5B2%2C1%2Cnull%2C1%2C%22https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%3Faccess_type%3Donline%26scope%3Dopenid%2Bprofile%2Bemail%26prompt%3Dselect_account%26response_type%3Dcode%26client_id%3D87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%26redirect_uri%3Dhttps%253A%252F%252Fprairielearn.ok.ubc.ca%252Fpl%252Foauth2callback%22%2Cnull%2C%5B%5D%2C4%2C%5B%5D%2C%22GeneralOAuthFlow%22%2Cnull%2C%5B%5D%2C1%5D%2C10%2C%5Bnull%2C%2287886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%22%2C%5B%5D%2C%22!ChRZVU9ONEpXWGRYZW9faDRlLWdSaRIfZzhGZzRMY1Bna01Wa013TWpqbVNUV1dTRFBqS25oZw%E2%88%99AHkTZLMAAAAAZNmO0CaqGDjjPK8uovHeyZzVVHBSR09e%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22https%3A%2F%2Fprairielearn.ok.ubc.ca%22%2C%22S-519885087%3A1691893072053304%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%22fa662f2e-e068-41dc-821a-8b0930cedc30%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2C14%2Cnull%2Cnull%2C%5B%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5B%5Bnull%2C9315%5D%2C%5Bnull%2C204%5D%2C%5Bnull%2C202%5D%5D%2Cnull%2C1%2Cnull%2Cnull%2C1%5D%2Cnull%2Cnull%2C2%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2C3%5D%5D&bgRequest=%5B%22oauth-account-chooser%22%2C%22%3CZ6tqq_YCAAaC65vKouuNhb39GicQEKX0ADkAIwj8RgyCpHtg-m1S1zL4XYTf1BxSHG-eO1kkpU6Dc2ZYaY7VXlNW-P1ArZjCSUIUDh_ix8al5_fNAAACT50AAAAIpwEHVgPGLeq9Tc0Ye5SeBnHlAk36rVon3D3Jq1LqAgQsL1U2E43xAzLqp8XNdbD5RF-s3IJ-hZwav4uO67QOTcpWnsUIuXUzLiom6d078EqoZp_bvGoUhDKn-idTl9OIMNHzK6aqYlVdrj-95Hj9wuDjfdjSydaoOpTomkE4uxx8EhmgrpixiBuLSppXFqd3vk9QNcW6gGRz75ZhKTOULtoxACj26luJ1Ymcli9_eqsR2WcxopE1lufYaolLw8uhMRcKFErHR6vhr8ScFXk9X4XVu3SZ8E4lX_Q4xAH2KOA8sdri0LzObQ13kI_cEmFZEDRE1v0G7_lWgbEnuyk9CGMYogj083eE8FpRjFyDEgjyt30FZHmrTO4IQAikikyr0nehpgm6UAMuiaEy9OFYB9HF6Ontp6VLWX6QmzbWLbeIp-BLus7lsg_v1c_k3XL8mpi9zYbNn05fkEzE_vIUgAeoK_TLTCrcELkZu4KFUasA_C__fHJgTZYZW7UVpy6k5dk1bpLKlFE_qxH-BLzf92jGkJWTAqSEo5ZCqrJI_261pK7U_ieJATXaby_2VASYxEPhuuRMo2zFCm-CWh5caf6zzlBvvEP--kI94c1uAq560OlzypMYKvYksUle000FgagWJXhJJmQOoLumT8W5tG5qlt1kEVqE_Nf593ykhMV8nDdhKRr2hW-PiYRvdtWzdHlUe8VtgM3L_-KAh1bT3kOasOu3mQ5WwH0SBNwdQeSv1QJSVzHQBSMR5yFZiEfpnOebVIM_8W23xTun9BZL9wxcYFs5EVxAgBdeghZkTgb5VDQslWrD04Fg0gvAonVDX2QORORJ2VntghxD1FDB7TtOrmi84ljHh9EvwPe-dsjy6qVGp2-vmtt4mlgDCeCxSh7Mra4__OUFQE8M-Qm5Ye-dcToSFMEXla7J9yQQ7jxHYCDiPdEc_opDsJ79s1lNYhAqLrURkExIwR7Ykn1_HYO6Pw-n4CUqKkkFEzaTLFgBOo4d790Qh6FH7Z6F9aKiwHgy0xq_5hpP9YcJ7raNFb0H5dEE7lkEcm5xep0T_ILUaz3HeeXrJmgot5WgBrBL09QSf0JJovbf5LahRmqMGl2B3dNEY0aD_YN0r56VW6QKEHjMdCVXgGbrCrKhzSqaDmRiRNNWhvutO8cc6lYhdgOcfZPbiVvW9isXeWMPL7nfQ-Dlft2EV5_4GWMrZ7z2xTC8tCB9PXoxjLySM_itXF6wEbUDUVkJzWNd0A-xg-VkaZ48UivKCCPDnpPJWBknw_dISXFHFWN-5YMO%22%5D&at=AFoagUVvMUGntDxGF8DR-ui46FuMN2x0oQ%3A1691893072148&azt=AFoagUVvMUGntDxGF8DR-ui46FuMN2x0oQ%3A1691893072148&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22CA%22%2Cnull%2Cnull%2Cnull%2C%22GeneralOAuthFlow%22%2Cnull%2C%5Bnull%2C%2287886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%22%2C%5B%5D%2C%22!ChRZVU9ONEpXWGRYZW9faDRlLWdSaRIfZzhGZzRMY1Bna01Wa013TWpqbVNUV1dTRFBqS25oZw%E2%88%99AHkTZLMAAAAAZNmO0CaqGDjjPK8uovHeyZzVVHBSR09e%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22https%3A%2F%2Fprairielearn.ok.ubc.ca%22%2C%22S-519885087%3A1691893072053304%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%22fa662f2e-e068-41dc-821a-8b0930cedc30%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2C14%2Cnull%2Cnull%2C%5B%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5B%5Bnull%2C9315%5D%2C%5Bnull%2C204%5D%2C%5Bnull%2C202%5D%5D%2Cnull%2C1%2Cnull%2Cnull%2C1%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C3%2C2%5D&gmscoreversion=undefined&flowName=GeneralOAuthFlow&checkConnection=youtube%3A246%3A0&checkedDomains=youtube&",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://accounts.google.com/signin/oauth/consent?authuser=2&part=AJi8hANvl0m3zpclqO1gUoIt7KFxzmVkf33FbPFC0X-FCvzclOKWUPjl2dIoCyiqoPWYYvkGO-ri7gmOmUs6U08vb3I8hl_51C3qKmN7O6-50x-fH3esgvn5uvTyLfl0Q8qy0OyNoVu57wjdkCGEGxjKd1oWK_b_U2ZZOfEKED3vws6hIRQgjqlVdNpbMyglBSiNgsLV-8eHST1SuLn1J-Zjs6_s-cbJpJ4ZWbvDNuQx3ELsVD2EyGOwTqlmhOci2Xq4S45fQsXt-sPzfpbNW0wu7Zhw7YWzf2nyFh5EL-qlDe6dL1O4x9-xzJJgYt_Zb2apcpLojsdawpwQfl_VE74ejlERZUj-A3rSw0rsXw5aQotedUVm2Wm3j7sH3dfwM_mlOQN9INT79BEiuJLFKUmsfLE-J-4zGpDDRcVMlP4rSqmugjhkWTICJJ7tPhALYQxggK0wzxBpyg1j9Bf9ocggiOZJ_bCYNEh_ROsD19QzMLNyq-VWhIg&as=S-519885087%3A1691893072053304&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&pli=1&rapt=AEjHL4M5-rNd9CmP4Z8JzbL6UnEjLVbkSWmlGgusi_iQWnJ4z9XkUehvSWYBg5pA2rT2TNFq5dj5oYhY0w_4Bvt2ajgZAeG5pw",
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,4]]],558,[["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691893081000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]],["1691893083000",null,[],null,null,null,null,"[[[196,37066,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],6,null,null,null,null,null,[]],["1691893083000",null,[],null,null,null,null,"[[[296,37131,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],7,null,null,null,null,null,[]]],"1691893083922",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,4]]],558,[["1691893080000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S-519885087:1691893072053304"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691893080000",null,[],null,null,null,null,"[null,null,3,[null,"S-519885087:1691893072053304"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,1219,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691893083968",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/oauth2callback?code=4%2F0Adeu5BWfeZJ4ZRr8urHmBtwfbkcImaTSYyjDTgPMp88fyMXdN1GXLjlUKsooInE7U27XhA&scope=email+profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&authuser=2&prompt=none",
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
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=MGE1ODM0NTRkMzgwNDFhOWM0YjE1MjFjZWEwMjc1YTcwN2JhYmY3MjIxOTllNmJmMWI0MjAzMzZjYmI5OTBkOA.ll8tgize.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691893085099&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjYWZiM2E4Mzc2LTBmY2ZmYzUxMDBmODU1LTQyMDE1NzE5LTg4ZmUwLTE4OWVjYWZiM2E5MWE4OCIsImdyb3VwcyI6e319",
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
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=NjJmNmFlZDk0MzQ1YWFhZjcyZTBkM2MyYWQ5NzE5Njc0MWNkMWJlNDQ5ZmQwMTMyN2E1MGNhNTgwNWU3YzdiMg.ll8tgj00.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=MDYzM2Q3YWQ5MjU2MDI2OWY4NTcwZTQ5OTUxNDMyMWNmNjMzN2VjMTZkNWM2MmU0YWViM2JmYTZkYzBlMjNhMQ.ll8tgkgd.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691893086813&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjYWZiYTVhM2RkLTAzNzM2ZWUyM2M5Mzc2LTQyMDE1NzE5LTg4ZmUwLTE4OWVjYWZiYTViMTgxMSIsImdyb3VwcyI6e319",
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
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=OTA0NjI4ZWI4NGY1ODI2MDc4MzQ4MmVhMmU5MmVmZThlODQ0ODliYTFjMzAzOGY4MDBkNDMxOGM4YTMzZDgxNA.ll8tgkgx.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691893089215&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjYWZjM2JjMTZiYS0wMzQ0ZDM1ZWNiOTAyYi00MjAxNTcxOS04OGZlMC0xODllY2FmYzNiZDE2ZDQiLCJncm91cHMiOnt9fQ%3D%3D",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/course_instance/27/instance_question/7262/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=YWQ5OWI1MzA4NjFmYTVjY2YxOTY0Yjg2MjVkYjgwZDBlMzQwMmQwZjljZDE3ZGU0OWM2ZDc1YzdiNzU0OWRiYQ.ll8tgm9z.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691893097270&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjYWZlMzMzOTk0LTA2OGE1MjBkYzZiMzllLTQyMDE1NzE5LTg4ZmUwLTE4OWVjYWZlMzM0Y2JjIiwiZ3JvdXBzIjp7fX0%3D",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/pl/course_instance/27/instance_question/7262/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Content-Length": "661",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=NjQ3MmQ1ZGJjYTc5ZmZhMDcwYmUzN2YzMGY5MmU0YjcyMzhmNTUyZDA5NDhkMWVkZDZmZmE5MmRmYjRjMDUyNQ.ll8tgs53.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
                "Host": "prairielearn.ok.ubc.ca",
                "Origin": "https://prairielearn.ok.ubc.ca",
                "Referer": "https://prairielearn.ok.ubc.ca/pl/course_instance/27/instance_question/7262/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data="SQLEditor=SELECT+c.cid%2C+c.cname%2C+COUNT%28s.sid%29+AS+shipment_count%0D%0AFROM+customer+c%0D%0AJOIN+shipment+s+ON+c.cid+%3D+s.cid%0D%0AGROUP+BY+c.cid%2C+c.cname%0D%0AHAVING+COUNT%28s.sid%29+%3E+%28%0D%0A++++SELECT+AVG%28shipment_count%29%0D%0A++++FROM+%28%0D%0A++++++++SELECT+cid%2C+COUNT%28sid%29+AS+shipment_count%0D%0A++++++++FROM+shipment%0D%0A++++++++GROUP+BY+cid%0D%0A++++%29+AS+avg_shipment_counts%0D%0A%29&__action=grade&__variant_id=715&__csrf_token=MmE0YzM0OWFiYTRlZDFmZDcwMDU3Mzc4MzljY2VkMzMyOGJlMWZhMmVlYjlkODIyZWUxZmE5MjI4ZDY3N2JlYQ.ll8tgrt3.eyJ1cmwiOiIvcGwvY291cnNlX2luc3RhbmNlLzI3L2luc3RhbmNlX3F1ZXN0aW9uLzcyNjIvIiwiYXV0aG5fdXNlcl9pZCI6IjE2In0",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/course_instance/27/instance_question/7262/?variant_id=715",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=YjU5OGE2MGYxMDk0NTk4MDRmNWVlOGNhYjQ1OTliZDliOWQ1YjEyYmU5NzI1MzhhYTdiZGViY2Q5MDg0OTljNg.ll8tgz3p.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
                "Host": "prairielearn.ok.ubc.ca",
                "Referer": "https://prairielearn.ok.ubc.ca/pl/course_instance/27/instance_question/7262/",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691893106945&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjYjAwOGZlMTkxYS0wMWYyNTk3YjA3NTFlNi00MjAxNTcxOS04OGZlMC0xODllY2IwMDhmZjFiZjUiLCJncm91cHMiOnt9fQ%3D%3D",
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(sample)
