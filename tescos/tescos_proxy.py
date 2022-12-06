import requests


class TescoProxy:

    headers = {
   'authority': 'www.tesco.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': 'null; null; trkid=f1acb04f-3694-4445-9ac4-661a10c5c6bd; atrc=20de3a1e-ba4a-4624-a0e9-b06e6b22815c; h-e=3747d993ec1162431c6c77b123e694932bd9ac423ad8d710e35c63c671de78f3; consumer=default; DCO=wdc; _csrf=0p-ppGJwy0kw7Lc9F4Zx5Mpw; ighs-sess=eyJwYXNzcG9ydCI6eyJ1c2VyIjp7ImlkIjoiamh1bWUwMDFAZ21haWwuY29tIiwiZW1haWwiOiI2UEU3a0xBampTVkJETnp2SXh5N09hN2ZKNWZSMllTakZtYWg1YjZIVXdBPSJ9fSwiYW5hbHl0aWNzU2Vzc2lvbklkIjoiYWUwMTM2ZDM1MmU1MDFmZmZjYjkwNTQ3N2U5YWVkODUiLCJzdG9yZUlkIjoiNTEzMSIsInV1aWQiOiJiMTE4OTE2OS0zZGVhLTQ5MjYtOWQzMy1jOTQ0YmUxNjk1ZGEifQ==; ighs-sess.sig=jWG4MIOFHpg5u5dExCNusyzaD-k; null; atrc=b2c18980-7a59-49ba-bb4a-15290f230476; _gcl_au=1.1.1415960996.1667204208; s_fid=01A8780C3B6B886A-2587EDB3D565CF6F; s_ecid=MCMID%7C13425608792358202213735558361702097420; s_vi=[CS]v1|31AFC2382347B39A-4000126C4700C5DC[CE]; _hjSessionUser_3147523=eyJpZCI6ImMwY2UxNjZlLWI2ZTgtNTFkMy1hYmZiLTJmODk5MjhjMWQ0MSIsImNyZWF0ZWQiOjE2NjcyMDQyMDg1OTgsImV4aXN0aW5nIjpmYWxzZX0=; cookiePreferences=%7B%22experience%22%3Atrue%2C%22advertising%22%3Atrue%7D; _4c_mc_=d3229a56-3ce2-4416-9a3f-813e0b4e90fa; _mibhv=anon-1667204327050-6823346412_4481; optimizelyEndUserId=oeu1667212997729r0.6492192784050606; _gcl_dc=GCL.1667757582.CjkKEQjwtp2bBhCU47CJtt7B7O0BEiQAPtaIo3M_se3mNmO6usENrAc2bD57dYMrdFM8DeTew-y8lVzw_wcB; AMCVS_E4860C0F53CE56C40A490D45%40AdobeOrg=1; s_cc=true; _csrf=Xbs3Sx0kx0_a2MrV_19nxdYU; UUID=b1189169-3dea-4926-9d33-c944be1695da; CID=142756368; HYF=1; AKA_A2=A; bm_sz=DC7D349841C1B5EAF496BD01049E8C7B~YAAQ1LD3SD7WNc2EAQAAn6hI1BHRrBefUrkMIJL3cCR5nOV1smn9avS6bvM6EtVUBxH0251Jb/syT7dY5fG+N+MwClGZUmrO5Zc7rNenPcE4h9N8+Pq2efKIN7Dba3pRYVrrkuyOq7BXZMKmJ2zbj5okFwfKOfWVcm3MLVsLPbEvGrMnnRwhcRMCYLL1v+TnP2lwpZxKmkfUQj7z93SC+T7dFuYUdohX4ASQxxy0MY/9d3xODcWiVVSH33kSnLfkhzKP4NmlGCj/pRGOSko1bETxM7ScuY3oQ/GnutvKN9HCNw==~3223856~4407864; ak_bmsc=B61529DC848748C58AAA79CABB96AC33~000000000000000000000000000000~YAAQ1LD3SK/WNc2EAQAAWa5I1BG8w/8luInNbGHsFuOvVr2JTRT8AhY4f3lNSM2acY1XZm/c4zoRIFUu+q5MP5rUMoO9q5AhFFM4xARYhSnz6cqNdghhxER3fDQAcNw2j1KaZD3Mf2zZUavgnf8Crzbz9bm7paXip7lKyhMVHE8lEPt0jbYe1Sx8LTYIFz7FwwnkRtakeiGK9Xr7eQpg+rhJXGwBp6nZdUgyTSQFhZ5vZaP2+t3IuTLlzn30Oiphb+RUul1hSK9o/pwFTnv/3R6VovVU/GGTQZbkH9xW3P9g9F6qn0YHf9EhIW6JTh9Muje/Lsc255gKwmPao1Ne+q0P1jL9c77bQTW50tJZXNf2vom1addOtypRG/JDGp9LrPLpFuJiRhluX8/tIW5O9nVstjsYWXqy2z9nQ+Gbdv0zZrZfIJaYCeuATdXrbOnGDDrezPRDoL+/pKcqICjnTZZ+YpotRNCkf8mBvdHeBreeFJI94cVd; _gid=GA1.2.614420390.1670008844; _gat_ukLego=1; AMCV_E4860C0F53CE56C40A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C19329%7CMCMID%7C13425608792358202213735558361702097420%7CMCAAMLH-1670613644%7C6%7CMCAAMB-1670613644%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1670016044s%7CNONE%7CMCAID%7C31AFC238519E8E6D-60000E0967025DAA%7CMCSYNCSOP%7C411-19336%7CvVersion%7C4.4.0; s_nr=1670008851006-Repeat; OAuth.AccessToken=eyJraWQiOiIyMTM1MGE2NC02YTYxLTRiNmYtYjIyZS1lYTNkOTNiY2YyMTQiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiI3NWIxYzQ2Zi1iYjY0LTQ1N2YtYmZjNS1hMTAyOGJiYjhjZTQiLCJpc3MiOiJodHRwczovL2FwaS50ZXNjby5jb20vaWRlbnRpdHkvdjQvaXNzdWUtdG9rZW4iLCJzdWIiOiJiMTE4OTE2OS0zZGVhLTQ5MjYtOWQzMy1jOTQ0YmUxNjk1ZGEiLCJpYXQiOjE2NzAwMDg4NTIsIm5iZiI6MTY3MDAwODg1MiwiZXhwIjoxNjcwMDEyNDUyLCJzY29wZSI6ImludGVybmFsIHB1YmxpYyIsImNvbmZpZGVuY2VfbGV2ZWwiOjEyLCJjbGllbnRfaWQiOiJhMTcxNDcwZS1iMGUzLTQ2ZDEtYmYxMi1jMjBiNDEyOGY0YjYiLCJ0b2tlbl90eXBlIjoiYmVhcmVyIiwic2lkIjoiMDFHS0E0SEtWRlBZNk1ZWkNZMEdBNEhHQ0ItYzA1NTM0NDAtMGQ0Yy00ZTFiLTg0MTUtODAyOGI1M2M0ZWExLWQ1STFLMnp1S0ROdkt3OU9tVmRmcEJQMWRBckNUekMxbGprUyJ9.YiR6g-8C9ga5Lt_3mRVN16VJBF-BfmaafcXlIoUh0t7bDYp08xyP3BkQFWBwJgYxnu0Z-2mYDOC1JLdtKotI1BVnV8-3su9DS1xXwWsl3t2aCt-spuTA6SRTxDt7tBSAvZ4sTiAsDj8M44Bvs3nt5UU5DAZ7zSdeUsNX3S95OSBN94jKQ6Fcxshhayg81v8lL7LhjH4ix83F0WgEcMd3oYGlcWsZNcGIKG2lMP6rhlOiI_zFP_SIPQGpdbs8B0tPeTu9MuUr4zOh0k8k3IupAcL1Kyhc-G5FPnHzUph3gJiXe1cWClkTdircn80KLvejQcph9cjKN1Nf8WNe_vvEXg; OAuth.RefreshToken=363eeac0-0075-44cc-ae7c-6b46c72c6ed8; OAuth.TokensExpiryTime=%7B%22AccessToken%22%3A1670012451598%2C%22RefreshToken%22%3A1670012451598%7D; akavpau_OneAccount=1670009152~id=a9c11f77169f858e647777174ccff23a; _ga=GA1.1.534411647.1667204208; akavpau_tesco_groceries=1670009176~id=7d56d49c78baf7c4bfc63e13c6e5c86a; _abck=8AF0C834BF0BBA7BB2454C42B1109776~-1~YAAQ1LD3SIPeNc2EAQAAoi5J1AhMDt0sccRGf78o+qNGiKwEVPjhhJd2Atk3OBPMwYaOBj5vPW8pS9AZ2PRUSK2OIR1Fi1k3C0+fNrWymokyRBNvf7jkbIkBlgg4z6/UpkuseCFI0B8PgFzTYveS/N90IgkHrNuCOTGToUpQxufu/jU0JZigGiH5CpLBpCSi5ViJfF/M0bSLZ9j3poB/Z5j/srs/2sc3YXYFqp3NRmvbonRmx9vjfbymlcCw8sM2lVJpLKWtQXet7P1xAgHBwexsTnnQ+A7sI42v7nfCAB4E0YcJ4vDPWKRscnDbeWhZ2jf+e9vFCBo9Dk4e2TllV3P3okF0HKIy5nmThnEQRm3QMDPUhbb80vtj+nlwrKB3bxh60gP0TRS/8a/HwvuvODdOwXHeiRI=~-1~-1~-1; s_gpv_pn=search%20results; _uetsid=6af09190727611edad506901d07f80de; _uetvid=5da333d058f411edae92f70bdcd0e638; bm_sv=D8BF72A1F4B6EF125B019A1B80F2BBA6~YAAQ1LD3SJzfNc2EAQAAIz5J1BElDmSRrKRxD+SoZzE1/or+TR9bMipPbbjm+9y4hnb1kl1iBxkgNUVCkePaEXXbADzw9O7qWhB8RH4Be1Fbc9rXf2KzzVIK6I8txe75CLvIOo+6U3woVu02+TlUqk6uJao/pAtgP8qMWomJalCvxFEzAx9oPfXL2afGf3YOWBGrYThiKM7Y5EUeBUS4hWrut/nMh7zbA1Yhw8tnm+9ShGK4HK2FeOwAHc8fnpYy~1; _ga_33B19D36CY=GS1.1.1670008844.15.1.1670008880.24.0.0',
    'dnt': '1',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1MTI5NTQiLCJhcCI6IjExMzQyNDYxMjUiLCJpZCI6ImQ1N2U1OTY1NDJiMTY3MGYiLCJ0ciI6ImY1OTI2ZTM2NjkxNzdmNzgxMjgwYzg1NmM1MTJiMjRiIiwidGkiOjE2NzAwMDg4ODEzNzgsInRrIjoiMzI5NjIzNSJ9fQ==',
    'origin': 'https://www.tesco.com',
    'referer': 'https://www.tesco.com/groceries/en-GB/search?query=chicken%20breast',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-f5926e3669177f781280c856c512b24b-d57e596542b1670f-01',
    'tracestate': '3296235@nr=0-1-3512954-1134246125-d57e596542b1670f----1670008881378',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-csrf-token': 'mN2tAKji-uin6TnFwjcFQNvp3obWmDK0wavM',
    'x-requested-with': 'XMLHttpRequest', 
}
    

    def update_amount_in_cart(self, item_id, amount):

        params = {
            '_method': 'PUT',
        }

        json_data = {
            'items': [
                {
                    'id': item_id,
                    'newValue': amount,
                    'oldValue': 3,
                    'newUnitChoice': 'pcs',
                    'oldUnitChoice': 'pcs',
                    'substitutionOption': 'FindSuitableAlternative',
                },
            ],
            'returnUrl': '/groceries/en-GB/search?query=peppers',
        }

        response = requests.put('https://www.tesco.com/groceries/en-GB/trolley/items',
                                params=params, headers=self.headers, json=json_data)
        return response.status_code
