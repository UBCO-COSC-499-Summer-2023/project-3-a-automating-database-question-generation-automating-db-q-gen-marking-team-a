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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691889015738&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjNzE5YmIyNDBjLTAxZDgzOWQwMDNkMjQ0LTQyMDE1NzE5LTg4ZmUwLTE4OWVjNzE5YmIzNGFhIiwiZ3JvdXBzIjp7fX0%3D",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://accounts.youtube.com/accounts/CheckConnection?pmpo=https%3A%2F%2Faccounts.google.com&v=-1132395234&timestamp=1691889015942",
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
                "x-client-data": "CJa2yQEIprbJAQipncoBCKKJywEIlKHLAQiFoM0BCOSwzQEI3L3NAQi7vs0BCO7EzQEIt8jNAQjxyc0BCLnKzQEYwMvMAQ==",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691889017696&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjNzFhMzViNWRhLTBiNjFlNTE4YzY2MjZkLTQyMDE1NzE5LTE0NDAwMC0xODllYzcxYTM1YzYyOCIsImdyb3VwcyI6e319",
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,0]]],558,[["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]]],"1691889017842",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,0]]],558,[["1691889018000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889018000",null,[],null,null,null,null,"[null,null,3,[null,"S1711438380:1691889000033449"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,4596,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691889018275",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,1]]],558,[["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]]],"1691889018317",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,1]]],558,[["1691889018000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889018000",null,[],null,null,null,null,"[null,null,3,[null,"S1711438380:1691889000033449"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,4596,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691889018501",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,2]]],558,[["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]]],"1691889018722",[]]',
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
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
                "x-chrome-id-consistency-request": "version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fa662f2e-e068-41dc-821a-8b0930cedc30,sync_account_id=112905861928398825341,signin_mode=all_accounts,signout_mode=show_confirmation",
                "x-client-data": "CJa2yQEIprbJAQipncoBCKKJywEIlKHLAQiFoM0BCOSwzQEI3L3NAQi7vs0BCO7EzQEIt8jNAQjxyc0BCLnKzQEYwMvMAQ==",
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,2]]],558,[["1691889018000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889018000",null,[],null,null,null,null,"[null,null,3,[null,"S1711438380:1691889000033449"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,4596,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691889018889",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691889019514&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjNzFhYTc1NGI5LTBjYTFiNjhhYjY0Zjk0LTQyMDE1NzE5LTg4ZmUwLTE4OWVjNzFhYTc2NTBjIiwiZ3JvdXBzIjp7fX0%3D",
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,3]]],558,[["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691889018000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]]],"1691889019598",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,3]]],558,[["1691889018000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889018000",null,[],null,null,null,null,"[null,null,3,[null,"S1711438380:1691889000033449"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,4596,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691889019991",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,4]]],558,[["1691889018000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889018000",null,[],null,null,null,null,"[null,null,3,[null,"S1711438380:1691889000033449"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,4596,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691889021614",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,4]]],558,[["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691889018000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]]],"1691889021652",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://accounts.google.com/_/signin/oauth?authuser=2&hl=en&_reqid=65422&rt=j",
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
                "x-client-data": "CJa2yQEIprbJAQipncoBCKKJywEIlKHLAQiFoM0BCOSwzQEI3L3NAQi7vs0BCO7EzQEIt8jNAQjxyc0BCLnKzQEYwMvMAQ==",
                "x-same-domain": "1",
            },
            data="access_type=online&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&prompt=select_account&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&response_type=code&scope=openid%20profile%20email&service=lso&o2v=2&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hAMin2sxCmw3MsoBufQKuZ2BF4znNvtgZQXivIAtiIjSFn4M1K19D3CKtMidopoE10QA3QlU2sAZajcnW0EcDIaEuD9rcaKD0D34EWn9OMSUf8E_Vj1xGbMwZFs6J57ypnAbyzH99XcoBLxHE5msA9lAhp3KC16z51vL5q4cbGQa6cMbx32CBmYZMZi_hSvhBBPDKqNU6NWujZvKJa4e-KgKX4Vn1f8tbxpd7DEE0TUc92Q7gx7LPsI5V-QBG6frWBg658VFV0jfSiMGH54OP-SsPnc5vecO-Qc-gQIf1hwBXGG0Ef5SVEGgLRkWTFcVCKHF0vqVQ7ay4K8RwXoFHr674u7sUgdndWP4po_07fXsrvBeqOHoX6K0QpeD1n7C5Gy6H3GLGXnG49KNauezajsl-Uut33dmQBbz8fq0OwjZMpgYstA56qCqszw3KidOjBwb0bu5DIL3As2_0sKcmx2nMrymYaiavhbxkpMJJpSu29GZ-GA%26as%3DS1711438380%253A1691889000033449%26client_id%3D87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%23&f.req=%5B%22AEThLlzp3ycj4V55eEBTT8GaCYP4n7FY1wzKnGqOCv8jQ9ZyUvWFpzieu8JUnPhjEvlNCnCuUcSnu-B6GSopdoh3j8h_1EMeaxTbM106U39vO10Rkzf0DpWNRfO60PJtCvVHWY8QmigXeeGWgDbKbHTNS9svIP1JAk7U9dPXeXnU_KcEjwS7095rhDpGiqebJHFQ1s2Tvo-LYrDtIzon4PVhJwCAOKGa9aFw31Nfi95QTsWnMBrgRzfzXNk8ncuy7uUmwfQnZSAmYjzmv67hFit3u46IQ9k-g6eqy74dHqMmhxfMty43AvuSVI957gCqs8mYDeU1tPK1CPXAKgPmo2e2vlnmRHGpP20MsohW2D08zlXcPuNw9ED2M3Niwg7psMRqQ7x_p_4EC8Iqz7XXEVJncjoe-hJnSS4CqYD8c2YmwmHPwsnay4SZv4w8TLydt4G99WAEqA-m7Zxmx6VOC-k7CI0My2DYSLiE0f098FTcacPhLmKbCVq6wMgmjnWvA8McyZ2NTKeZ20FjT2pg__lf3C1vSF9HE0257xc5Ifztj9-0hBWRUojdSFzj28476eq-pptJY5Re1VBD8pKy7lvwAOCVlMbtJR6zHLL5QvAzieG1iO1EcSa6wFHBw6LVkhDW0F5shq0TSxwcg9yoyFL7bcwOI4ftvrh83IAiV-wMj4VuO8ojWLIZJyUQ0r-povZ8V5lPA6eYjta2VzbyhuzpkPlQ6XzBZ_Rt4vUVunDpLetuGzjNqjynw78Li0J78QWDfwXz5wXDlnfKOjuLsY6Tx4sXSU2S5Wjwd3JGovTn4imz70R9r8MofXM2bt8rvA3FdI5vI40znPoEavC9iMXGSpR3m4LASSjIMRQzDm6Re_iUgG4dCpfj7OL3E5exqgc0kubqI_YTa7kdQgEPeFB9DdYfVROOpyPvxn78UKELaLY6pkv_fkmn-t028srOY8Gc4WsaABJsXdDhEVH4ASsZLFsFpyHm-Yj-ex4IeRBVdBdBui61DIGmQxtNcyCTofsQsEqCZ2eD1eKphUuMo7rXzTceqKix_o1QKfaHxE5YfKJXbP-EGJxSQvr-SxVSmLFphSAXFdmwrrrvCa6s6UPBiESs6i4hCA%22%2C2%2C0%2Cnull%2C%5Bnull%2Cnull%2C%5B2%2C1%2Cnull%2C1%2C%22https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%3Faccess_type%3Donline%26scope%3Dopenid%2Bprofile%2Bemail%26prompt%3Dselect_account%26response_type%3Dcode%26client_id%3D87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%26redirect_uri%3Dhttps%253A%252F%252Fprairielearn.ok.ubc.ca%252Fpl%252Foauth2callback%22%2Cnull%2C%5B%5D%2C4%2C%5B%5D%2C%22GeneralOAuthFlow%22%2Cnull%2C%5B%5D%2C1%5D%2C10%2C%5Bnull%2C%2287886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%22%2C%5B%5D%2C%22!ChQ5QjY4ZHV6ZVM3YmE4WXczRkZDWRIfdzYyYkRfX29FeThTa013TWpqbVNUV1hpNlJYSG5oZw%E2%88%99AHkTZLMAAAAAZNl-6BPxmfLYKy-oytgqQ7LewazGy-8x%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22https%3A%2F%2Fprairielearn.ok.ubc.ca%22%2C%22S1711438380%3A1691889000033449%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%22fa662f2e-e068-41dc-821a-8b0930cedc30%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2C14%2Cnull%2Cnull%2C%5B%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5B%5Bnull%2C9315%5D%2C%5Bnull%2C204%5D%2C%5Bnull%2C202%5D%5D%2Cnull%2C1%2Cnull%2Cnull%2C1%5D%2Cnull%2Cnull%2C2%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2C3%5D%5D&bgRequest=%5B%22oauth-account-chooser%22%2C%22%3CZKhqqPUCAAaC65vKouuNtZMz0RWsV_z0ADkAIwj8RhZeujZJ8eslp1I30pVhLSL7s43ubl1_nG5jsdKK0X0Cu-UfhBcqe3tvyvETE2akhbvQ7lTNAAAFpZ0AAAAgpwEHVgO2VqDN6Lqpp3q5NQ2OlkYiCXjYdEWrUyYkVy7qVuLeAMcrQoc-NhHo1Jyk1qr_TLPNK73sh6htNR5sGOTMwH341nvjae81yC0l-rRPr37hErDRIPP2IGFIRqrD5EJ5YaZ-k95vLclnkGwjVu8fBR6uvvvaSuE3Tnvp2BRZxRCbifLTV9wZzcd9VgirEr3ER1SHSFFwhP5LJzb3YUvHHZfQBJCfNyB5dkF89XnBtK7NGwlIEFyb5YHLwFggqGjTHngsfc0Ywxukc4PbHtgaOO8rdBUL6pEmje7qfGmXATLMfwi_pzcr1O6mM8FfHzA6q-lv1vwJ0fbC74kLu8G5t4Au_a72l9UORFeNhy5Y47ELd9xvPTTAMMwpmtxjum96nYMgJOdD-VJsE-mGxv2C4xs1UX9TJLMTO7byv5tFWXthiyzPP5iNjF1juuK78RE9VYmc4jobfs0Ajaf2CItpzrPUpZdMxCg1TqdSS5mBx7ANwALR6fTFbpNK6_UiRukq5CSsdRanG0ZvnUnVsjStTOksKmMAqBf5WyQPcetjQw5YYL3LbDsH4iY5sMXxpaeV3_cQ3uf77D-HQfm8GN3LpqireEcrNK0_RVzGFlz3m4O4U53zqBaAWSh8SJvHQOLyTvRn8ZxlUej8DwDi8qNPPrewpkI8_tIlVVcCCgY-CPxiNmoO2Lk4IefvhFyaiDsxvlo9Lg_F8Rj6QLyukHjLcs1hRVdEBjpHHJXmEHHEomTYmIwNXYPCzL7v4Zm5nL1o4W4yqh_4M8maW2HnXi-UxCMhzUiagn4Lo1DLBo9ZJzLsTvLngmTooktPryg_DIKxKcgBqPkdTr5oj-JtFJc0A5vzNhpN8CtOrCeME070HAANx8_meQt0giZMyFFTXMvdmNmMIxl52_HB8vKNrcLMPoGZF0Lv1onR6nUFPDrfJ4pgHndSqwG0reDl3zsO7VQGD0EHdWH1enuA4yos5l45pdsfwtV1iWpYkfh8z66L2Atq3_tTs80fbgA3sCRclG9CewzpPJNYmFc2G0TzSTeC81hcmEQXr8VZw5tcbSI8gwADmp7cSNJfRlfsVbD4fVtl6fyM33mw_fj6XX5yWtiappzw6EY7-gr0KB_tEdtd5ppyFXK_i4ndeFaUWW76N3AzhYouGJR2VjXLFlpKR-2xTzVM_bBWJCxsEj5m87BqgiJusA8lcDpF3Mt3K2KG3vRxEL0BUX9TxSQzw3Y8k1raIYVya7BlWadfNYpR3yi0dfxOXSPGfDPiOD0%22%5D&at=AFoagUUMxsZoD2b_cr9wjYzC9RJVxPe-kQ%3A1691889000140&azt=AFoagUUMxsZoD2b_cr9wjYzC9RJVxPe-kQ%3A1691889000140&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22CA%22%2Cnull%2Cnull%2Cnull%2C%22GeneralOAuthFlow%22%2Cnull%2C%5Bnull%2C%2287886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com%22%2C%5B%5D%2C%22!ChQ5QjY4ZHV6ZVM3YmE4WXczRkZDWRIfdzYyYkRfX29FeThTa013TWpqbVNUV1hpNlJYSG5oZw%E2%88%99AHkTZLMAAAAAZNl-6BPxmfLYKy-oytgqQ7LewazGy-8x%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22https%3A%2F%2Fprairielearn.ok.ubc.ca%22%2C%22S1711438380%3A1691889000033449%22%2C0%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B5%2C%2277185425430.apps.googleusercontent.com%22%2C%5B%22https%3A%2F%2Fwww.google.com%2Faccounts%2FOAuthLogin%22%5D%2Cnull%2Cnull%2C%22fa662f2e-e068-41dc-821a-8b0930cedc30%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C5%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2C14%2Cnull%2Cnull%2C%5B%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5B%5Bnull%2C9315%5D%2C%5Bnull%2C204%5D%2C%5Bnull%2C202%5D%5D%2Cnull%2C1%2Cnull%2Cnull%2C1%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C3%2C2%5D&gmscoreversion=undefined&flowName=GeneralOAuthFlow&checkConnection=youtube%3A1467%3A0&checkedDomains=youtube&",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://accounts.google.com/signin/oauth/consent?authuser=2&part=AJi8hAMin2sxCmw3MsoBufQKuZ2BF4znNvtgZQXivIAtiIjSFn4M1K19D3CKtMidopoE10QA3QlU2sAZajcnW0EcDIaEuD9rcaKD0D34EWn9OMSUf8E_Vj1xGbMwZFs6J57ypnAbyzH99XcoBLxHE5msA9lAhp3KC16z51vL5q4cbGQa6cMbx32CBmYZMZi_hSvhBBPDKqNU6NWujZvKJa4e-KgKX4Vn1f8tbxpd7DEE0TUc92Q7gx7LPsI5V-QBG6frWBg658VFV0jfSiMGH54OP-SsPnc5vecO-Qc-gQIf1hwBXGG0Ef5SVEGgLRkWTFcVCKHF0vqVQ7ay4K8RwXoFHr674u7sUgdndWP4po_07fXsrvBeqOHoX6K0QpeD1n7C5Gy6H3GLGXnG49KNauezajsl-Uut33dmQBbz8fq0OwjZMpgYstA56qCqszw3KidOjBwb0bu5DIL3As2_0sKcmx2nMrymYaiavhbxkpMJJpSu29GZ-GA&as=S1711438380%3A1691889000033449&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&pli=1&rapt=AEjHL4NakjyQ7LRCY0iYDPcqAedHWapf4AWrxpJs4zQwxeyIltqD5gVJy6QQc4saMFmmEFgP0tC3qfuwu7w3Ng7JJuJPfKd_YA",
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
                "x-client-data": "CJa2yQEIprbJAQipncoBCKKJywEIlKHLAQiFoM0BCOSwzQEI3L3NAQi7vs0BCO7EzQEIt8jNAQjxyc0BCLnKzQEYwMvMAQ==",
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,5]]],558,[["1691889018000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889018000",null,[],null,null,null,null,"[null,null,3,[null,"S1711438380:1691889000033449"],["Northern America",null,"/o/oauth2/v2/auth/oauthchooseaccount",3,4596,1,"CA"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]]],"1691889024799",[]]',
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
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"en",null,null,null,null,[1,0,5]]],558,[["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],0]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],1,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[[224,42076,"invalid-device-id",null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],2,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],3,null,null,null,null,null,[]],["1691889016000",null,[],null,null,null,null,"[[null,[1,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=online&scope=openid%20profile%20email&prompt=select_account&response_type=code&client_id=87886874870-cutg7vea7od8p1bvhvuvrgms6go31i2g.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fprairielearn.ok.ubc.ca%2Fpl%2Foauth2callback&service=lso&o2v=2&flowName=GeneralOAuthFlow",null,["https://prairielearn.ok.ubc.ca/"],1]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],4,null,null,null,null,null,[]],["1691889018000",null,[],null,null,null,null,"[[[307,64002,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],5,null,null,null,null,null,[]],["1691889021000",null,[],null,null,null,null,"[[[196,37066,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],6,null,null,null,null,null,[]],["1691889021000",null,[],null,null,null,null,"[[[296,37131,null,null,null,null,null,null,null,null,null,null,"accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount"]],null,3,[null,"S1711438380:1691889000033449"]]",null,null,null,null,null,null,25200,null,null,null,null,[],7,null,null,null,null,null,[]]],"1691889025149",[]]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/oauth2callback?code=4%2F0Adeu5BUDDHymnWlBmXFTy4lMEeUikWPt0bex-eqVpQUxdOTE9v8KozS4FvKf1AtDOHLQnQ&scope=email+profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile&authuser=2&prompt=none",
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
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=MDFhYzNmY2U2MjAyMTdlYTU2NjYzZGFmNTcyMDhlODlmMGJkMzg0NGQ5MDQwMTIxYjkzZTQxY2UzMjJhYWE3Yw.ll8r1lsq.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691889032228&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjNzFkYzFmOTE5LTBmYmNjNjdlODg3ODFiLTQyMDE1NzE5LTg4ZmUwLTE4OWVjNzFkYzIwNGE1IiwiZ3JvdXBzIjp7fX0%3D",
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
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=MmNmYmVmOTlhYzgyZGI4ZjI3NmI5NDdmMDM2ZWIzMjZkNGJjNjBhYTUxYjdjNjFiNTBhMDQxYTAwZjNlNTZjMg.ll8r1n4r.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=OTJlYjEyZWE3ZWI2MWIxNjJjNDk5N2ViMThhOGNiM2U1NGRhZmRlOGJiOTNkZThhOWJjNWU5ZTUyNTY2ZmI5Zg.ll8r1rsn.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691889039454&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjNzFmODVhODMxLTA2ZDM1MWQ2NzgxMzQzLTQyMDE1NzE5LTg4ZmUwLTE4OWVjNzFmODViN2ExIiwiZ3JvdXBzIjp7fX0%3D",
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
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=NmYxZjQyODY0ZTkwYmQzNWUzNDg4ODc4MzI1ZjRkYTA5N2JlYjU1Yjc2Y2IxNDE2Zjg3YThhNTU2MmYzYzY0ZQ.ll8r1tcu.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691889044439&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjNzIwYmQzNzI0LTBlNDM2YjI0Njk5MmItNDIwMTU3MTktODhmZTAtMTg5ZWM3MjBiZDQ1YmYiLCJncm91cHMiOnt9fQ%3D%3D",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/course_instance/27/instance_question/693/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=NWMwNDY2YTY4ZDg3NjA1NzY1OGEzOWVlMTUzYzE5MGIyOWVjNTZhYzEwNmM2NDIzOWYxNjcxODE3OWJiYWQ5ZA.ll8r1x8i.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691889061624&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjNzI0ZWY0Y2E2LTAwNTFjMThjMmEyY2M1LTQyMDE1NzE5LTg4ZmUwLTE4OWVjNzI0ZWY1ODA1IiwiZ3JvdXBzIjp7fX0%3D",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/pl/course_instance/27/instance_question/693/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Content-Length": "275",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=ZTEyYWY2YTY0NTkzMjM4ZTJiNWUxZDJhMmZiNDk2MzcyNzkwOGJjY2Y2NzU4ZGMzZWJhMjgwMDI2MmY2OWRlMQ.ll8r2bmo.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
                "Host": "prairielearn.ok.ubc.ca",
                "Origin": "https://prairielearn.ok.ubc.ca",
                "Referer": "https://prairielearn.ok.ubc.ca/pl/course_instance/27/instance_question/693/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
            },
            data="RelaXEditor=%CF%80+cid+Customer&__action=grade&__variant_id=716&__csrf_token=Yjg1MWM5NWM2NjlkYTQ0YmY3OTc5Nzg3OTIyMTgxMzJiNjhjODRlMjI3ZTM5OGI0ODU0Zjc0MzYzMmM0YmExNw.ll8r29k8.eyJ1cmwiOiIvcGwvY291cnNlX2luc3RhbmNlLzI3L2luc3RhbmNlX3F1ZXN0aW9uLzY5My8iLCJhdXRobl91c2VyX2lkIjoiMTYifQ",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pl/course_instance/27/instance_question/693/?variant_id=716",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "ph_foZTeM1AW8dh5WkaofxTYiInBhS4XzTzRqLs50kVziw_posthog=%7B%22distinct_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24device_id%22%3A%2218904ba35768f2-0cc6e5c50dc631-26031a51-144000-18904ba3577f23%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22extension_version%22%3A%221.5.5%22%2C%22%24session_recording_enabled_server_side%22%3Afalse%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%22enable-session-recording%22%3Afalse%2C%22sourcing%22%3Afalse%2C%22only-company-edit%22%3Afalse%2C%22job-lists%22%3Afalse%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; pl_authn=MzZiMTQ3Nzc2ZTFhMWNkODU0ODhkNjZkMTc0MWRkZTg3NWI5NThlYTRlYzljN2I5MmUzY2ZlNGI2NWEyZTVlYg.ll8r2u9q.eyJ1c2VyX2lkIjoiMTYiLCJhdXRobl9wcm92aWRlcl9uYW1lIjoiR29vZ2xlIn0",
                "Host": "prairielearn.ok.ubc.ca",
                "Referer": "https://prairielearn.ok.ubc.ca/pl/course_instance/27/instance_question/693/",
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
            "https://hog.simplify.jobs/decide/?v=3&ip=1&_=1691889090368&ver=1.57.2",
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
            data="data=eyJ0b2tlbiI6ImZvWlRlTTFBVzhkaDVXa2FvZnhUWWlJbkJoUzRYelR6UnFMczUwa1Z6aXciLCJkaXN0aW5jdF9pZCI6IjE4OWVjNzJiZjNjZTItMGNiNWQ4MzAyYzcwMmYtNDIwMTU3MTktODhmZTAtMTg5ZWM3MmJmM2Q2N2YiLCJncm91cHMiOnt9fQ%3D%3D",
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(sample)
