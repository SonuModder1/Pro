import httpx, aiohttp

with open("proxy.txt", 'a') as file:
    file.write(httpx.get("https://sunny9577.github.io/proxy-scraper/proxies.txt").text)
    file.write(httpx.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=anonymous").text)
    file.write(httpx.get("https://sunny9577.github.io/proxy-scraper/generated/http_proxies.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt").text)
    file.write(httpx.get("https://www.proxy-list.download/api/v1/get?type=http").text)
    file.write(httpx.get("https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt").text)
    file.write(httpx.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=5000&country=all&ssl=all&anonymity=all").text)
    file.write(httpx.get("https://sunny9577.github.io/proxy-scraper/generated/socks4_proxies.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt").text)
    file.write(httpx.get("https://www.proxy-list.download/api/v1/get?type=socks4").text)
    file.write(httpx.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=5000&country=all&ssl=all&anonymity=all").text)
    file.write(httpx.get("https://sunny9577.github.io/proxy-scraper/generated/socks5_proxies.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt").text)
    file.write(httpx.get("https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt").text)
    file.write(httpx.get("https://www.proxy-list.download/api/v1/get?type=socks5").text)