<h1 align="center">Regex Library</h1>

<h3 align="center">Sources<h3>

- [SystemJargon - Pihole](https://github.com/SystemJargon/pi-hole)


<h2 <h2 align="center"><a href=""></h2>

```
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]
^(.+[-_.])??telemetry[-.]
^(.+[-_.])??xn--
^adim(age|g)s?[0-9]*[-_.]
^adtrack(er|ing)?[0-9]*[-.]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-.]
^analytics?[-.]
^banners?[-.]
^beacons?[0-9]*[-.]
^count(ers?)?[0-9]*[-.]
^pixels?[-.]
^stat(s|istics)?[0-9]*[-.]
^track(ers?|ing)?[0-9]*[-.]
^traff(ic)?[-.]
google-{0,}(analytic|syndication|(ad[a-z0-9]*|tag)-{0,}service)[s]\.[a-z]{2,7}$
google-{0,}(analytics{0,}|(ad|tag)manager)\.[a-z]{2,7}$
double-{0,}clic(k|k[.]*by-{0,}google)\.[a-z]{2,7}$
(google|partner|pub)-{0,}ads{0,}-{0,}(apis{0,})\.[a-z]{2,7}$
^(.+\.)?amp\..+\.com$
^(.+\.)?ampproject\.org$
^(.+\.)?amp\.cloudflare\.com$
^(.+\.)?cdn\.ampproject\.org$
(.*\.|^)((think)?with)?google($|((adservices|apis|mail|static|syndication|tagmanager|tagservices|usercontent|zip|-analytics)($|\..+)))
([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo\.com/
([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?sitescout(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?appnexus(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?evidon(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?mediamath(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?scorecardresearch(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?flashtalking(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?turn(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?mathtag(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?googlesyndication(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?s\.yimg\.com/cv/ae/us/audience/
([A-Za-z0-9.-]*\.)?clicks\.beap/
([A-Za-z0-9.-]*\.)?.doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?yieldmanager(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?w55c(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?adnxs(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?advertising\.com/
([A-Za-z0-9.-]*\.)?evidon\.com/
([A-Za-z0-9.-]*\.)?scorecardresearch\.com/
([A-Za-z0-9.-]*\.)?flashtalking\.com/
([A-Za-z0-9.-]*\.)?turn\.com/
([A-Za-z0-9.-]*\.)?mathtag\.com/
([A-Za-z0-9.-]*\.)?surveylink/
([A-Za-z0-9.-]*\.)?info\.yahoo\.com/
([A-Za-z0-9.-]*\.)?ads\.yahoo\.com/
([A-Za-z0-9.-]*\.)?global\.ard\.yahoo\.com/
(^|\.)lgsmartad\.com$
(^|\.)lge.com
(^|\.)buffpanel\.com$
(^|\.)bugsnag\.com$
(^|\.)redshell\.io$
(^|\.)treasuredata\.com$
(^|\.)unity(|3d)\.com$
(^|\.)unityads(|\.co)\.com$
```

```
(\.|^)facebook\.com$
(^|\.)fbsbx\.com$
(^|\.)fbsbx\.com\.online-metrix\.net$
(^|\.)m\.me$
(^|\.)messenger\.com$
(^|\.)tfbnw\.net$
(^|\.)instagram\.com$
(^|\.)facebook\.[A-Za-z0-9]+$
(^|\.)fb\.[A-Za-z0-9]+$
(^|\.)fbcdn\.[A-Za-z0-9]+$
(\.|^)muscdn\.com$
(\.|^)musical\.ly$
(\.|^)ttlivecdn\.com$
(\.|^)atomile\.com$
(\.|^)tiktokv\.com$
(\.|^)tiktokcdn\.com$
(\.|^)tiktok\.com$
(\.|^)snapchat\.com$
(\.|^)snap\.com$
(\.|^)sc-cdn\.net$
(\.|^)sc-prod\.net$
(\.|^)whatsapp\.com$
(\.|^|-)(facebook|fb|instagram|tiktok|whatsapp|snapchat)[.]
```

```
/^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]/
/^(.+[_.-])?telemetry[_.-]/
/^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]/
/^adim(age|g)s?[0-9]*[_.-]/
/^adtrack(er|ing)?[0-9]*[_.-]/
/^advert(s|is(ing|ements?))?[0-9]*[_.-]/
/^aff(iliat(es?|ion))?[_.-]/
/^analytics?[_.-]/
/^banners?[_.-]/
/^beacons?[0-9]*[_.-]/
/^count(ers?)?[0-9]*[_.-]/
/^mads\./
/^pixels?[-.]/
/^popup?[_.-]/
/^stat(s|istics)?[0-9]*[_.-]/
```

<h2 <h2 align="center"><a href="">[Cparsell - Blocklists Whitelist](https://github.com/cparsell/Blocklists-Whitelists)

```
[_.-]analytics?[_.-]
^telemetry?[-.]
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]
^(.+[-_.])??telemetry[-.]
^(.+[-_.])??xn--
^adim(age|g)s?[0-9]*[-_.]
^adtrack(er|ing)?[0-9]*[-.]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-.]
^analytics?[-.]
^banners?[-.]
^beacons?[0-9]*[-.]
^count(ers?)?[0-9]*[-.]
^pixels?[-.]
^stat(s|istics)?[0-9]*[-.]
^track(ers?|ing)?[0-9]*[-.]
^traff(ic)?[-.]
google-{0,}(analytic|syndication|(ad[a-z0-9]*|tag)-{0,}service)[s]\.[a-z]{2,7}$
google-{0,}(analytics{0,}|(ad|tag)manager)\.[a-z]{2,7}$
double-{0,}clic(k|k[.]*by-{0,}google)\.[a-z]{2,7}$
(google|partner|pub)-{0,}ads{0,}-{0,}\.[a-z]{2,7}$
(^|\.)fbsbx\.com\.online-metrix\.net$
^(.+\.)?amp\..+\.com$
^(.+\.)?ampproject\.org$
^(.+\.)?amp\.cloudflare\.com$
^(.+\.)?cdn\.ampproject\.org$
([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo\.com/
([A-Za-z0-9.-]*\.)?secure\.footprint\.net/
([A-Za-z0-9.-]*\.)?match\.com/
([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?sitescout(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?appnexus(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?evidon(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?mediamath(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?scorecardresearch(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?flashtalking(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?turn(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?mathtag(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?googlesyndication(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?s\.yimg\.com/cv/ae/us/audience/
([A-Za-z0-9.-]*\.)?clicks\.beap/
([A-Za-z0-9.-]*\.)?.doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?yieldmanager(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?w55c(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?adnxs(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?advertising\.com/
([A-Za-z0-9.-]*\.)?evidon\.com/
([A-Za-z0-9.-]*\.)?scorecardresearch\.com/
([A-Za-z0-9.-]*\.)?flashtalking\.com/
([A-Za-z0-9.-]*\.)?turn\.com/
([A-Za-z0-9.-]*\.)?mathtag\.com/
([A-Za-z0-9.-]*\.)?surveylink/
([A-Za-z0-9.-]*\.)?info\.yahoo\.com/
([A-Za-z0-9.-]*\.)?ads\.yahoo\.com/
([A-Za-z0-9.-]*\.)?global\.ard\.yahoo\.com/
^(.*\.)*(ad-(balancer|brix|center|cloud|delivery|delivery|locus|maven|move|plus|score|srv|stir))\.([a-z]{2,3}\.)*[a-z]{2,6}$
```

<h2 <h2 align="center"><a href="">[Mkb2091 - Blockconvert](https://github.com/mkb2091/blockconvert)

```
[_.-]analytics?[_.-]
```

<h2 <h2 align="center"><a href="">[NocutralArchives - BlockLists](https://github.com/nocturnalarchives/BlockLists)

```
(\.|^)*-alert*\.
(\.|^)*-alerts?\.
(\.|^)*-analytic*\.
(\.|^)*-geo*\.
(\.|^)*aaxads*\.
(\.|^)*aboutads*\.
(\.|^)*ad-?block*\.
(\.|^)*ad-?blocker*\.
(\.|^)*ad-?engine*\.
(\.|^)*ad-?form*\.
(\.|^)*ad-?log*\.
(\.|^)*ad-?serve*\.
(\.|^)*ad-?srvr*\.
(\.|^)*ad-?system*\.
(\.|^)*ads-*\.
(\.|^)*ads?-?server*\.
(\.|^)*adsafeprotected*\.
(\.|^)*adserver*\.
(\.|^)*adsrvr*\.
(\.|^)*advertising*\.
(\.|^)*alert*\.
(\.|^)*alerts*\.
(\.|^)*analytic*\.
(\.|^)*analytics*\.
(\.|^)*baidu*\.
(\.|^)*click*\.
(\.|^)*click-?funnel*\.
(\.|^)*click-?stream*\.
(\.|^)*clickcease*\.
(\.|^)*clicks?\.
(\.|^)*clickserv*\.
(\.|^)*clickstream*\.
(\.|^)*clickstream-producer*\.
(\.|^)*track*\.
(\.|^)*tracker*\.
(\.|^)*tracking*\.
(\.|^)*traffic*\.
(\.|^)*traffic\.
(\.|^)*trend*\.
(\.|^)ad\.
(\.|^)ads?\.
(\.|^)ads\.
(\.|^)geo\.
(\.|^)log*\.
(\.|^)log\.
(\.|^)logs?-?([0-9a-z]+)\.
(\.|^)logs?\.
(\.|^)metrics?\.
(\.|^)telemetry\.
(\.|^)traffic*\.
```

```
^.*survey.*\.
^.*trac(k|x|xx)?(e|ed|er|ing).*\.
^.*track-?(tivation)?.*\.
^.*track-?t?ivation.*\.
^.*track?-?(x|xx)?(e|ed|er|ing)?.*\.
^.*track.*\.
^.*traffick?-?junky.*\.
```

```
(^|\.)fonts?\.(www|clicks?|ads?|offers?|ww([w0-9]+))?\.?
(www|clicks?|ads?|offers?|ww[0-9])\.fonts?\.
```

```
(\.|^)geolocation\.
```

```
^.*pubads.*\.
^.*([a-z0-9]?-?diagnostics?.*\.
^.*([a-z0-9])?-?stats?.*\.
^.*([a-z0-9])?-?trust.*\.
^.*([a-z0-9])([-a-z0-9])?-?adserver?s?.*\.
^.*(ab|ui)-?test(s|er|ing)?.*\.
^.*(clients?|data|deactivat(e|ed|es|ion)|dcapps|info(rmation)?|keys?|metri(c|x)s?|recycl(e|ed|er|or|ing)|sonar|stat(s|istics?)|users?)\.*([-a-z0-9]+.)?sonos([-a-z0-9]+.)?\.
^.*(firmware|updat(e|ed|er|es|ing)|upgrad(e|ed|er|es|ing))\.*([-a-z0-9]+.)?sonos([-a-z0-9]+.)?\.
^.*(no)?-?cookie-?(s|bot|pro).*\.
^.*(no)?-?cookies?-?(test))?(s|er|ed|ing)?.*\.
^.*(no)?-?cookies?-test(s|er|ed|ing).*\.
^.*(ui|ab)?-?experiments?.*\.
^.*(update)?-?time(zones?)?.*\.
^.*1e100.*\.
^.*2mdn.*\.
^.*3lift.*\.
^.*aaxads.*\.
^.*aaxdetect.*\.
^.*abtest(s|ed|er|ing)?.*\.
^.*accounts?.*\.
^.*activity.*\.
^.*ad-?cache.*\.
^.*ad-?forms?.*\.
^.*ad-?nexus.*\.
^.*ad-?service.*\.
^.*ad(s|v|verts?|vertising|vertisers?)?-?servers?.*\.
^.*ad(s|v|verts?|vertising|vertisers?)?-?systems?.*\.
^.*ad(s|v|verts?|vertising|vertisers?)?-?trackers?.*\.
^.*ad(s|v|verts?|vertising|vertisers?)?-?tracking.*\.
^.*ad(v|verts?|vertising|vertisers?).*\.
^.*add-?this.*\.
^.*addtoany.*\.
^.*admitad.*\.
^.*adnxs.*\.
^.*adobedtm.*\.
^.*adrotat(e|ed|er|es|ion|ing).*\.
^.*ads?-?twitter.*\.
^.*ads?-?you-?like.*\.
^.*adsafeprotected.*\.
(^|\.)ad(s|v)?-
(^|\.)ad(s|v)?\.
^.*([a-z0-9])?-?diagnostics?.*\.
^.*([a-z0-9])?-?stats?.*\.
^.*([a-z0-9])?-?trust.*\.
^.*([a-z0-9])([-a-z0-9])?-?adserver?s?.*\.
^.*banners?.*\.
^.*beacons?.*\.
```

<h2 <h2 align="center"><a href="">[RPiList - Specials](https://github.com/RPiList/specials)

```
\.ru$
\.link$
```

<h2 <h2 align="center"><a href="">[Slyfox1186 - Pihole Regex](https://github.com/slyfox1186/pihole-regex)

```
(\.|^)dataplicity\.com$
(\.|^)iij\.ad\.jp$
(\.|^)ahoravideo.*$
(\.|^)bideo.*$
(\.|^)buybuggle\.com$
(\.|^)client\.mchsi\.com$
(\.|^)fairu.*$
(\.|^)gardensuny\.com$
(\.|^)hokaclearances\.com$
(\.|^)lstartanalystconcepts\.org\.uk$
(\.|^)privatproxy.*$
(\.|^)shadowadcity\.com$
(\.|^)steamcommurnily\.com$
(\.|^)stickyadstv\.com\.akadns\.net$
(\.|^)trafyield\.com$
(\.|^)usage\.trackjs\.com$
(\.|^)wmail.*$
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^[a-z]+ad\.[a-z]+\.com\.edgesuite\.net$
^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]]
^adim(age|g)s?[0-9]*[_.-]
^adserver-.*\.amazonaws\.com$
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]]
^api\..*\.hismarttv\.com$--OtherTV
^banners?[_.-]]
^beacons?[0-9]*[_.-]]
^content(|-geo)\.uplynk\.com$
^count(ers?)?[0-9]*[_.-]]
^cs[0-9]+\.wpc\.thetacdn\.net$
^dms-[a-z0-9]+report\.wc\.yahoodns\.net$
^dns-[a-z0-9]+\.sombrero\.yahoo\.net$
^ds-beap[0-9]\.[a-z]{2}\.[a-z0-9]+\.yahoodns\.net$
^ds-global[0-9]\.l[0-9].search\.[a-z0-9]+\.yahoo\.com$
^mads\.]
^nado-ecs-lb-[a-z]+-[a-z]+-[0-9]-[0-9]+\.[a-z]+-[a-z]+-[0-9]\.elb\.amazonaws\.com$
^pixels?[-.]]
^prod-elb-ats-[0-9]+\.[a-z]{2}-[a-z]+-[0-9]\.elb\.amazonaws\.com$
^ssp-ats-prod-[a-z\-]+-[0-9]\.one-mobile-prod\.aws\.oath\.cloud$
^stat(s|istics)?[0-9]*[_.-]]
^uplynk-beacon-newvpc-[0-9]+\.[a-z]{2}-[a-z]+-[0-9]\.elb\.amazonaws\.com$
^v-[a-z0-9]+\.wc\.yahoodns\.net$
```

<h2 <h2 align="center"><a href="">[Cbuijs - Unbound DNS Firewall](https://github.com/cbuijs/unbound-dns-firewall)

```
/^(.*\.)*(accountant|ad|an|analytic[s]*|bar|bi[dt]|biz|christmas|click|club|country|cricket|date|dclk|diet|docs|download|exit|faith|free|fun|gdn|guru|i2p|info|kim|link|loan|men|mobi|mom|name|ninja|office|on(ion|line)|ovh|party|pro|racing|realtor|reise|ren|review|rocks|science|shop|site|space|stream|study|tec(h|hnology)|to[pr]|trade|vip|web(cam|site)|work|win|xin|xyz|yokohama|zone)$/
/^(.*[\.\-])*[0-9]*(php|web|[mwxy])*ad[sxz]*[0-9]*[\.\-]/
/^(.*[\.\-])*ad(aly[sz]er|am|banner|bureau|click|dynamo|farm|hese|im[a]*g[e]*|info|ition|just|k2|load|log|media|ma(n|nager|x)|ne(t[a-z]+|xus)|nxs|ocean|renaline|revolver|rotat(e|or)|science|script|sense|spirit|[v\-]*s[e]*r(v|ve|ver|vi(ce|ng))|stat|stream)[sxz]*[0-9]*[\.\-]/
/^(.*[\.\-])*ad([v]*server[a-z]*|shuffle|sl|sy(s|stem)|test|(v|ve(r|rt|rtis(e|er|ing)))|trac(k|king|ker)|wise|word)[sxz]*[0-9]*[\.\-]/
/^(banner[a-z]*|open[-]*(ad|x)|page[-]*ad|reklam|(secure[-]*)*pub[-]*ad|smart[-]*ad[s]*([-]*server)*|unityad)[sz]*[0-9]*[\.\-]/
/^(.*[\.\-])*(affiliate|([s]*anal|local)[iy](s[iy]s|ti[ck])|click|clk|cooki(e|ex)|cnt|coun(t[y]*|t[e]*[dr])|datacollect|hit|(amp|[s]*)metr[iy][ck]|open[-]*(ad|x)|partner|ping|pixel|sta(t|tisti[ck])|tag|(web|[uv]*)stat)[sz]*[0-9]*[\.\-]/
/^(.*[\.\-])*(telemetr[iy]|(evil|[s]*)trac(k|king|ker)|[s]*trk|utm|video[-]*stat)[sz]*[0-9]*[\.\-]/
/^(creatives|gcirm[0-9]*|marketing|oa(s|scentral)|o(x|x-d)|prom(o|otion)|qwe|.*servedby|syndication|traffic)[\.\-]/
/^[a-z]\.([0-9]+|ad[^d]|click)/
/^(.*\.)*(atdmt|beget|bango|casalemedia|clickbank|extreme[-]*dm|flurry|krxd|liveadvert|moatads|mookie[1-9]*|nuggad|omtrdc|p2l|quants[e]*rv[e]*|onestat|onthe|pop(cash|check|test|under|up)|revsci|scorecardresearch|sitestat|tacoda|tynt)\./
/^(.*\.)*(o0bc|2mdn|2o7|302br|51yes|adtech([-]*[a-z]+)*|amazon[-]*adsystem|atwola|bkrtx|bluekai|chartbeat|crwdcntrl|d(e|o)mdex|effectivemeasure|falkag|free|fwmrm|gemius)\./
/^(.*\.)*(hit(box|tail)|hotjar|imrworldwide|intellitxt|lijit|mixpanel|ms[-]*adcenter|netklix|outbrain|petrovka|pixel|syndication|rubiconproject|sitemeter|skimresources|smaato|smartadserver|(fast|stat)counter|suprnova|taboola|tradedouble[r]*|xiti|usergrid|visualrevenue|volumetrk)\./
#/^(.*[\.\-])*(advert|banner|beacon|cash|click[y]*|coin|count|megavolt|ms[-]*edge|([ens0-9]+)*(omni|over)ture|pop(cash|check|test|under|up)|tracker)/
#/^.*(advert|banner|beacon|cash|click[y]*|coin|coun(t|ter[s]*)|megavolt|ms[-]*edge|([ens0-9]+)*(omni|over)ture|pop(cash|check|test|under|up)|track(er|ing))[\.\-]/
```

<h2 align="center">##  Common AD labels

```
/^(.*[\.\-])*[0-9]*(php|web|[mwxy])*ad[sxz]*[0-9]*[\.\-]/
/^(.*[\.\-])*ad(aly[sz]er|am|banner|bureau|click|dynamo|farm|hese|im[a]*g[e]*|info|ition|just|k2|load|log|media|ma(n|nager|x)|ne(t[a-z]+|xus)|nxs|ocean|renaline|revolver|rotat(e|or)|science|script|sense|spirit|[v\-]*s[e]*r(v|ve|ver|vi(ce|ng))|stat|stream)[sxz]*[0-9]*[\.\-]/
/^(.*[\.\-])*ad([v]*server[a-z]*|shuffle|sl|sy(s|stem)|test|(v|ve(r|rt|rtis(e|er|ing)))|trac(k|king|ker)|wise|word)[sxz]*[0-9]*[\.\-]/
/^(banner[a-z]*|open[-]*(ad|x)|page[-]*ad|reklam|(secure[-]*)*pub[-]*ad|smart[-]*ad[s]*([-]*server)*|unityad)[sz]*[0-9]*[\.\-]/
```

<h2 align="center">##  Common Tracking/Stats labels

```
/^(.*[\.\-])*(affiliate|([s]*anal|local)[iy](s[iy]s|ti[ck])|click|clk|cooki(e|ex)|cnt|coun(t[y]*|t[e]*[dr])|datacollect|hit|(amp|[s]*)metr[iy][ck]|open[-]*(ad|x)|partner|ping|pixel|sta(t|tisti[ck])|tag|(web|[uv]*)stat)[sz]*[0-9]*[\.\-]/
/^(.*[\.\-])*(telemetr[iy]|(evil|[s]*)trac(k|king|ker)|[s]*trk|utm|video[-]*stat)[sz]*[0-9]*[\.\-]/
```

<h2 align="center">##  Top-N advertisers/trackers domain(parts)

```
/^(.*\.)*(atdmt|beget|bango|casalemedia|clickbank|extreme[-]*dm|flurry|krxd|liveadvert|moatads|mookie[1-9]*|nuggad|omtrdc|p2l|quants[e]*rv[e]*|onestat|onthe|pop(cash|check|test|under|up)|revsci|scorecardresearch|sitestat|tacoda|tynt)\./
/^(.*\.)*(o0bc|2mdn|2o7|302br|51yes|adtech([-]*[a-z]+)*|amazon[-]*adsystem|atwola|bkrtx|bluekai|chartbeat|crwdcntrl|d(e|o)mdex|effectivemeasure|falkag|free|fwmrm|gemius)\./
/^(.*\.)*(hit(box|tail)|hotjar|imrworldwide|intellitxt|lijit|mixpanel|ms[-]*adcenter|netklix|outbrain|petrovka|pixel|syndication|rubiconproject|sitemeter|skimresources|smaato|smartadserver|(fast|stat)counter|suprnova|taboola|tradedouble[r]*|xiti|usergrid|visualrevenue|volumetrk)\./
```

<h2 align="center">##  Google

```
/^(.*\.)*google[-]*(analytic|syndication|(ad[a-z0-9]*|tag)[-]*service)[s]*\./
/^(.*\.)*(www[-]*)*google[-]*(analytic[s]*|(ad|tag)[-]*manager)\./
/^(.*\.)double[-]*clic(k|k[-]*by[-]*google)\./
/^(google|partner|pub)ad[s]*(api[s]*)*\./
```

<h2 <h2 align="center"><a href="">[SystemJargon - Filters](https://github.com/SystemJargon/filters)


<h2 align="center">##  Facebook

```
(\.|^)facebook\.com$
(^|\.)fbsbx\.com$
(^|\.)fbsbx\.com\.online-metrix\.net$
(^|\.)m\.me$
(^|\.)messenger\.com$
(^|\.)tfbnw\.net$
(^|\.)instagram\.com$
(^|\.)facebook\.[A-Za-z0-9]+$
(^|\.)fb\.[A-Za-z0-9]+$
(^|\.)fbcdn\.[A-Za-z0-9]+$
(\.|^)muscdn\.com$
(\.|^)musical\.ly$
(\.|^)ttlivecdn\.com$
(\.|^)atomile\.com$
(\.|^)tiktokv\.com$
(\.|^)tiktokcdn\.com$
(\.|^)tiktok\.com$
(\.|^)snapchat\.com$
(\.|^)snap\.com$
(\.|^)sc-cdn\.net$
(\.|^)sc-prod\.net$
(\.|^)whatsapp\.com$
(\.|^|-)(facebook|fb|instagram|tiktok|whatsapp|snapchat)[.]
```

<h2 align="center">##  Tracking

```
(\.)(adult|ads|adverts|advertising|click|porn|sex|telemetry|tracking|tracing)$
```

<h2 <h2 align="center"><a href="">[Smokingwheels-SmokingWheels.github.io](https://github.com/smokingwheels/smokingwheels.github.io)

```
(\.|^)clickbank\.net$
```

<h2 <h2 align="center"><a href="">[Greg-2600-PiholeBlocklist](https://github.com/Greg-2600/pihole_block_list)

<h2 align="center">##  Advertisments

```
(^|\.)qualtrics\.com$
^(.+[_.-])?ad[sxv]?[0-9]*[_.-]
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^(www[0-9]*\.)?xn--
^adim(age|g)s?[0-9]*[_.-]
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
^mads\.
^pixels?[-.]
^stat(s|istics)?[0-9]*[_.-]
^track(ing)?[0-9]*[_.-]
```

<h2 <h2 align="center"><a href="">[HL2Guide- Filterlists for Adguard or PiHole](https://github.com/hl2guide/Filterlist-for-AdGuard-or-PiHole)

<h2 align="center">##  FileTypes

```
/(.*).(aif|cda|mid|midi|mpa|wma|wpl|arj|z|dmg|toast|vcd|gadget)/
/(.*).(wsf|fon|cfm|swift|vb|3g2|3gp|avi|flv|mov|rm|swf|vob|wmv)/
```

<h2 align="center">##  [A1] Tracking and Stats

```
/(.*)(cookie|pixel|stat|telemetry|tracker|pixel|analytic|metric)(s\b|\b)(.*)/
/(.*)(tracking|xiaomi)(s\b|\b)(.*)/
```

<h2 align="center">##  [B1] Scams

```
/(.*)(g2a)(.*)/
```

<h2 align="center">##  [C1] Banned Words

```
/(.*)(chatroom|cheat|drug|casino|liveshow|weapon|coin)(s\b|\b)(.*)/
```

<h2 align="center">##  [C2] Horrible Words

```
/(.*)(rape|forcedsex|animalsex|bestiality|beastsex|monstersex|zoosex|snuff)(s\b|\b)(.*)/
/(.*)(death|kill|murder|incest)(s\b|\b)(.*)/
/(.*)(pedophilia|necrophilia|incapacitatedsex|blood|mutilation)(s\b|\b)(.*)/
```

<h2 align="center">##  Blocks all insecure HTTP traffic

```
/http\:/
```

<h2 align="center">##  Blocks some coinmining websites

```
/(coinmin)/
```

<h2 align="center">##  Blocks Advertisments

```
/(ad(service|sdk|vert|serv|s))/
/(banner|doubleclick|groovinads|liveadvert|popupad)/
```

<h2 <h2 align="center"><a href="">[HomemadeAdvanced - PiHole](https://codeberg.org/HomemadeAdvanced/PiHole)

<h2 align="center">##  Advertisments & Tracking

```
^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^adim(age|g)s?[0-9]*[_.-]
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
^mads\.
^pixels?[-.]
^https?://([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo\.com/
^https?://([A-Za-z0-9.-]*\.)?secure\.footprint\.net/
^https?://([A-Za-z0-9.-]*\.)?match\.com/
^https?://([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?sitescout(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?appnexus(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?evidon(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?mediamath(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?scorecardresearch(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?flashtalking(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?turn(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?mathtag(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?googlesyndication(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?s\.yimg\.com/cv/ae/us/audience/
^https?://([A-Za-z0-9.-]*\.)?clicks\.beap/
^https?://([A-Za-z0-9.-]*\.)?.doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?yieldmanager(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?w55c(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?adnxs(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?advertising\.com/
^https?://([A-Za-z0-9.-]*\.)?evidon\.com/
^https?://([A-Za-z0-9.-]*\.)?scorecardresearch\.com/
^https?://([A-Za-z0-9.-]*\.)?flashtalking\.com/
^https?://([A-Za-z0-9.-]*\.)?turn\.com/
^https?://([A-Za-z0-9.-]*\.)?mathtag\.com/
^https?://([A-Za-z0-9.-]*\.)?surveylink/
^https?://([A-Za-z0-9.-]*\.)?info\.yahoo\.com/
^https?://([A-Za-z0-9.-]*\.)?ads\.yahoo\.com/
^https?://([A-Za-z0-9.-]*\.)?global\.ard\.yahoo\.com/
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]
^adim(age|g)s?[0-9]*[-_.]
^adtrack(er|ing)?[0-9]*[-.]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-.]
^analytics?[-.]
^banners?[-.]
^beacons?[0-9]*[-.]
^count(ers?)?[0-9]*[-.]
^hpopenbid?[-.]
^outbrain?[-.]
^prebid?[-.]
^revcontent?[-.]
^rubiconproject?[-.]
^taboola?[-.]
^telemetry[-.]
^traff(ic)?[-.]
^(ad\.)
^(ad1\.)
^(ad2\.)
^(ad3\.)
^(adimages\.)
^(ads\.)
^(ads1\.)
^(ads2\.)
^(ads3\.)
^(ads4\.)
^(ads5\.)
^(adserv\.)
^(adserve\.)
^(adserver\.)
^(adserver1\.)
^(adserver2\.)
^(adsrv\.)
^(adv\.)
^(advertising\.)
^(adx\.)
^(aff\.)
^(affiliate\.)
^(affiliates\.)
^(analytics\.)
^(banner\.)
^(banners\.)
^(clicks\.)
^(counter\.)
^(gcirm\.)
^(oas\.)
^(oascentral\.)
^(phorm\.)
^(pixel\.)
^(protection\.)
^(reklam\.)
^(scrooge\.)
^(stat\.)
^(track\.)
^(tracker\.)
^(tracking\.)
```

<h2 align="center">##  Advertisments & Tracking (logs included)

```
((^)|(.))adchoice.
((^)|(.))ads.roku.com
((^)|(.))adsdk.
((^)|(.))adserv.
((^)|(.))analytic.
((^)|(.))logs.roku.com
((^)|(.))metric.
((^)|(.))telemetry.
(.*)\.g00\.(.*)
(^|\.)xn--.*$
```

<h2 align="center">##  Advertisments & Tracking

```
(ads|captive|cloudservices|logs).roku.com$
.*\.g00\..*
^ad([sxv]?[0-9]*|system)[-_.]([^.[:space:]]+\.){1,}|[-_.]ad([sxv]?[0-9]*|system)[-_.]
^(.+[-_.])?adse?rv(er?|ice)?s?[0-9]*[-_.]
^(.+[-_.])?telemetry[-_.]
^adtrack(er|ing)?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-_.]
^analytics?[-_.]
^banners?[-_.]
^beacons?[0-9]*[-_.]
^count(ers?)?[0-9]*[-_.]
^pixels?[-_.]
```

<h2 align="center">##  Analytics & Tracking

```
(^|\.)analytics$
(^|\.)adsterra\.com$
(^|\.)clicky\.com$
^(.+[-_.])??telemetry[-.]
google-{0,}(analytic|syndication|(ad[a-z0-9]*|tag)-{0,}service)[s]\.[a-z]{2,7}$
google-{0,}(analytics{0,}|(ad|tag)manager)\.[a-z]{2,7}$
double-{0,}clic(k|k[.]*by-{0,}google)\.[a-z]{2,7}$
(google|partner|pub)-{0,}ads{0,}-{0,}(apis{0,})\.[a-z]{2,7}$
([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo\.com/
([A-Za-z0-9.-]*\.)?secure\.footprint\.net/
([A-Za-z0-9.-]*\.)?match\.com/
([A-Za-z0-9.-]*\.)?sitescout(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?appnexus(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?evidon(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?mediamath(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?scorecardresearch(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?flashtalking(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?turn(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?mathtag(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?googlesyndication(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?s\.yimg\.com/cv/ae/us/audience/
([A-Za-z0-9.-]*\.)?clicks\.beap/
([A-Za-z0-9.-]*\.)?.doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?yieldmanager(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?w55c(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?adnxs(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?advertising\.com/
([A-Za-z0-9.-]*\.)?evidon\.com/
([A-Za-z0-9.-]*\.)?scorecardresearch\.com/
([A-Za-z0-9.-]*\.)?flashtalking\.com/
([A-Za-z0-9.-]*\.)?turn\.com/
([A-Za-z0-9.-]*\.)?mathtag\.com/
([A-Za-z0-9.-]*\.)?surveylink/
([A-Za-z0-9.-]*\.)?info\.yahoo\.com/
([A-Za-z0-9.-]*\.)?ads\.yahoo\.com/
([A-Za-z0-9.-]*\.)?global\.ard\.yahoo\.com/
/ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]/
/(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]/
/(.+[_.-])?telemetry[_.-]/
/adim(age|g)s?[0-9]*[_.-]/
/^adtrack(er|ing)?[0-9]*[_.-]/
/^advert(s|is(ing|ements?))?[0-9]*[_.-]/
/aff(iliat(es?|ion))?[_.-]/
/analytics?[_.-]/
/banners?[_.-]/
/beacons?[0-9]*[_.-]/
/count(ers?)?[0-9]*[_.-]/
/mads\./
/pixels?[-.]/
/stat(s|istics)?[0-9]*[_.-]/```
(x[n]?xx|xvideo|porn|sex).*\.
```

<h2 <h2 align="center"><a href="">[Cbuijs - Accomplist](https://github.com/cbuijs/accomplist)

<h2 align="center">##  Google

```
^(.*[_.-])?double[-]*[ck]li([c]*k[sz]*|que)[_.-]
^(.*[_.-])?google[-]*(analy(se|ti([ck]|que))|syndi[ck]ation|(ad[a-z0-9]*|tag)[-]*(manager|service))[sz]*[_.-]
(^|\.)firebase
(^|\.)adservice\.google\.
```

<h2 align="center">##  Tracking Statistics

```
^.*-dnsotls-ds\.metric\.gstatic\.com\.$
^.*\.(ds|v[46])\.metric\.gstatic\.com\.$
```

<h2 <h2 align="center"><a href="">[Revolveruk30 - Pihole Regex](https://github.com/revolveruk30/pihole-regex)

```

```

<h2 <h2 align="center"><a href="">[Hemiipatu - Pihole Blocklists](https://github.com/hemiipatu/PiHoleBlocklists)

<h2 align="center">##  Advertisments & Tracking

```
^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]
^(.+[-_.])??telemetry[-.]
^(.+[-_.])??xn--
^adim(age|g)s?[0-9]*[-_.]
^adtrack(er|ing)?[0-9]*[-.]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-.]
^analytics?[-.]
^banners?[-.]
^beacons?[0-9]*[-.]
^count(ers?)?[0-9]*[-.]
^mads\.
^pixels?[-.]
^stat(s|istics)?[0-9]*[-.]
^track(ers?|ing)?[0-9]*[-.]
^traff(ic)?[-.]
.*\.g[0-9]+\..*
```

<h2 <h2 align="center"><a href="">[Liamengland1 - Mischosts](https://github.com/liamengland1/mischosts)

<h2 align="center">##  Block Tiktok Traffic

```
(\.|^)bytecdn\.cn$
(\.|^)bytedance\.com$
(\.|^)bytedance\.net$
(\.|^)bytedns\.net$
(\.|^)byteicdn\.com$
(\.|^)byteimg\.com$
(\.|^)byteoversea\.com$
(\.|^)byteoversea\.net$
(\.|^)bytetcdn\.com$
(\.|^)hypstarcdn\.com$
(\.|^)ibytedtos\.com$
(\.|^)ibyteimg\.com$
(\.|^)ipstatp\.com$
(\.|^)isnssdk\.com$
(\.|^)muscdn\.com$
(\.|^)musemuse\.cn$
(\.|^)musical\.ly$
(\.|^)pstatp\.com$
(\.|^)sgpstatp\.com$
(\.|^)sgsnssdk\.com$
(\.|^)snssdk\.com$
(\.|^)tiktok\.com$
(\.|^)tiktokcdn\.com$
(\.|^)tiktokv\.com$
(\.|^)toutiao\.com$
(\.|^)worldfcdn\.com$
(\.|^)wsdvs\.com$
```

<h2 <h2 align="center"><a href="">[AIRFORCE1 - PiHoleRepositorys](https://github.com/AlRFORCE1/PiHoleRepositorys)

```
(^|\.)casino$
```

<h2 <h2 align="center"><a href="">[HeribertoKubuntu - Pihole](https://github.com/HeribertoKubuntu/pihole)

```
^(.+[_.-])?ad[sxv]?[0-9]*[_.-]
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^(www[0-9]*\.)?xn--
^adim(age|g)s?[0-9]*[_.-]
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
^mads\.
^pixels?[-.]
^stat(s|istics)?[0-9]*[_.-]
^track(ers?|ing)?[0-9]*[_.-]
(googlesyndication\.com)$
(1stok\.com)$
(strip\.alicdn\.com)$
(247realmedia\.com)$
(2cnt\.net)$
(2mdn\.net)$
(2o7\.net)$
(302br\.net)$
(51yes\.com)$
(about-tabs\.com)$
(adalyser\.com)$
(adbrite\.com)$
(adbureau\.net)$
(addthis\.com)$
(adk2\.co)$
(admob\.com)$
(adnxs\.com)$
(adocean\.pl)$
(adprotect\.net)$
(adsafeprotected\.com)$
(adscience\.nl)$
(adserver\.com)$
(adtech\.de)$
(adtech\.fr)$
(adtech\.us)$
(adtlgc\.com)$
(advance\.net)$
(advertising\.com)$
(advertserve\.com)$
(am15\.net)$
(amazon-adsystem\.com)$
(appier\.net)$
(applovin\.com)$
(atdmt\.com)$
(bannerbank\.ru)$
(bbelements\.com)$
(bravenet\.com)$
(casalemedia\.com)$
(cedexis-radar\.net)$
(checkm8\.com)$
(cjt1\.net)$
(cnzz\.com)$
(cqcounter\.com)$
(crashlytics\.com)$
(crypto-loot\.com)$
(doubleclick\.be)$
(doubleclick\.net)$
(dynamic\.dol\.ru)$
(economicoutlook\.net)$
(esomniture\.com)$
(estat\.com)$
(extreme-dm\.com)$
(ezcybersearch\.com)$
(falkag\.net)$
(fastclick\.net)$
(focalink\.com)$
(gemius\.pl)$
(geovisite\.com)$
(glam\.com)$
(glpals\.com)$
(googleadservices\.com)$
(google-analytics\.com)$
(googlezip\.net)$
(groovinads\.com)$
(hitbox\.com)$
(hotlog\.ru)$
(hpg\.com\.br)$
(hpg\.ig\.com\.br)$
(hut1\.ru)$
(hyperbanner\.net)$
(imrworldwide\.com)$
(intellitxt\.com)$
(iovation\.com)$
(kaffnet\.com)$
(kontera\.com)$
(linkpulse\.com)$
(liteweb\.net)$
(liveadvert\.com)$
(marketgid\.com)$
(marketscore\.com)$
(mydas\.mobi)$
(oewabox\.at)$
(omniture\.com)$
(omtrdc\.net)$
(opentracker\.net)$
(ourtablets\.com)$
(p2l\.info)$
(paycount\.com)$
(petrovka\.info)$
(polybuild\.ru)$
(pop6\.com)$
(popmarker\.com)$
(popupad\.net)$
(pos\.baidu\.com)$
(sapo\.pt)$
(servedbyopenx\.com)$
(sextracker\.be)$
(sextracker\.com)$
(sextracker\.de)$
(shengen\.ru)$
(sitemeter\.com)$
(smartadserver\.com)$
(spylog\.com)$
(startappexchange\.com)$
(startappnetwork\.com)$
(startappservice\.com)$
(statcounter\.com)$
(surf-town\.net)$
(thruport\.com)$
(tradedoubler\.com)$
(tsyndicate\.com)$
(tynt\.com)$
(vkuservideo\.net)$
(voluumtrk\.com)$
(voodoo\.com)$
(web3000\.com)$
(webtrekk\.net)$
(xiti\.com)$
(xxxcounter\.com)$
(youku\.com)$
(zedo\.com)$
^(ad\.)
^(ad1\.)
^(ad2\.)
^(ad3\.)
^(adimages\.)
^(ads\.)
^(ads1\.)
^(ads2\.)
^(ads3\.)
^(ads4\.)
^(ads5\.)
^(adserv\.)
^(adserve\.)
^(adserver\.)
^(adserver1\.)
^(adserver2\.)
^(adsrv\.)
^(adv\.)
^(advertising\.)
^(adx\.)
^(aff\.)
^(affiliate\.)
^(affiliates\.)
^(analytics\.)
^(banner\.)
^(banners\.)
^(click\.)
^(clicks\.)
^(counter\.)
^(gcirm\.)
^(oas\.)
^(oascentral\.)
^(phorm\.)
^(pixel\.)
^(protection\.)
^(reklam\.)
^(scrooge\.)
^(stat\.)
^(stats\.)
^(track\.)
^(tracker\.)
^(tracking\.)
```

<h2 <h2 align="center"><a href="">[SystemJargon - Blockist](https://github.com/SystemJargon/blocklists)

```
(\.|^)(adserve|adtrack|advert|affiliate|analytics|banners|beacons|click|counters|pixels|stats|statistics|telemetry|track|tracking)
```

```
/^telemetry?[-.]/
/^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]/
/^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]/
/^(.+[-_.])??telemetry[-.]/
/^(.+[-_.])??xn--/
/^adim(age|g)s?[0-9]*[-_.]/
/^adtrack(er|ing)?[0-9]*[-.]/
/^advert(s|is(ing|ements?))?[0-9]*[-_.]/
/^aff(iliat(es?|ion))?[-.]/
/^analytics?[-.]/
/^banners?[-.]/
/^beacons?[0-9]*[-.]/
/^count(ers?)?[0-9]*[-.]/
/^pixels?[-.]/
/^stat(s|istics)?[0-9]*[-.]/
/^track(ers?|ing)?[0-9]*[-.]/
/^traff(ic)?[-.]/
/google-{0,}(analytic|syndication|(ad[a-z0-9]*|tag)-{0,}service)[s]\.[a-z]{2,7}$/
/google-{0,}(analytics{0,}|(ad|tag)manager)\.[a-z]{2,7}$/
/double-{0,}clic(k|k[.]*by-{0,}google)\.[a-z]{2,7}$/
/(google|partner|pub)-{0,}ads{0,}-{0,}\.[a-z]{2,7}$/
/(/^|\.)fbsbx\.com\.online-metrix\.net$/
/(/^|\.)m\.me$/
/^(.+\.)?amp\..+\.com$/
/^(.+\.)?ampproject\.org$/
/^(.+\.)?amp\.cloudflare\.com$/
/^(.+\.)?cdn\.ampproject\.org$/
/([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo\.com/
/([A-Za-z0-9.-]*\.)?secure\.footprint\.net/
/([A-Za-z0-9.-]*\.)?match\.com/
/([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?sitescout(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?appnexus(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?evidon(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?mediamath(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?scorecardresearch(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?flashtalking(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?turn(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?mathtag(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?googlesyndication(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?s\.yimg\.com/cv/ae/us/audience/
/([A-Za-z0-9.-]*\.)?clicks\.beap/
/([A-Za-z0-9.-]*\.)?.doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?yieldmanager(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?w55c(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?adnxs(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?advertising\.com/
/([A-Za-z0-9.-]*\.)?evidon\.com/
/([A-Za-z0-9.-]*\.)?flashtalking\.com/
/([A-Za-z0-9.-]*\.)?turn\.com/
/([A-Za-z0-9.-]*\.)?mathtag\.com/
/([A-Za-z0-9.-]*\.)?surveylink/
/([A-Za-z0-9.-]*\.)?info\.yahoo\.com/
/([A-Za-z0-9.-]*\.)?ads\.yahoo\.com/
/([A-Za-z0-9.-]*\.)?global\.ard\.yahoo\.com/
/(/^|\.)lgsmartad\.com$/
/(/^|\.)buffpanel\.com$/
/(/^|\.)bugsnag\.com$/
/(/^|\.)redshell\.io$/
/(/^|\.)treasuredata\.com$/
/(/^|\.)unity(|3d)\.com$/
/(/^|\.)unityads(|\.co)\.com$/
```

```
/^mads\./
/([A-Za-z0-9.-]*\.)?[a-z]{2,7}\.footprintdns\.com/
/([A-Za-z0-9.-]*\.)?fbsbx\.com/
/^graph?[-.]/
```

<h2 <h2 align="center"><a href="">[Cparsell - Blocklists-Whitelists](https://github.com/cparsell/Blocklists-Whitelists)

```
/^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]/
/^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]/
/^(.+[-_.])??telemetry[-.]/
/^adtrack(er|ing)?[0-9]*[-.]/
/^advert(s|is(ing|ements?))?[0-9]*[-_.]/
/^aff(iliat(es?|ion))?[-.]/
/^analytics?[-.]/
/^beacons?[0-9]*[-.]/
/^count(ers?)?[0-9]*[-.]/
/^(s)?stat(s|istics)?[0-9]*[-.]/
/^track(ers?|ing)?[0-9]*[-.]/
/^traff(ic)?[-.]/
/google-{0,}(analytic|syndication|(ad[a-z0-9]*|tag)-{0,}service)[s]\.[a-z]{2,7}$/
/google-{0,}(analytics{0,}|(ad|tag)manager)\.[a-z]{2,7}$/
/double-{0,}clic(k|k[.]*by-{0,}google)\.[a-z]{2,7}$/
/(google|partner|pub)-{0,}ads{0,}-{0,}\.[a-z]{2,7}$/
/(/^|\.)fbsbx\.com\.online-metrix\.net$/
/(/^|\.)m\.me$/
/^(.+\.)?amp\..+\.com$/
/^(.+\.)?ampproject\.org$/
/^(.+\.)?amp\.cloudflare\.com$/
/([A-Za-z0-9.-]*\.)?secure\.footprint\.net/
/([A-Za-z0-9.-]*\.)?scorecardresearch(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?mathtag(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?googlesyndication(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?s\.yimg\.com/cv/ae/us/audience/
/([A-Za-z0-9.-]*\.)?.doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
/([A-Za-z0-9.-]*\.)?adnxs(\.\w{2}\.\w{2}|\.\w{2,4})/
/(/^|\.)lgsmartad\.com$/
/(/^|\.)bugsnag\.com$/
/(/^|\.)unity(|3d)\.com$/
```

```
^telemetry?[-.]
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]
^(.+[-_.])??telemetry[-.]
^(.+[-_.])??xn--
^adim(age|g)s?[0-9]*[-_.]
^adtrack(er|ing)?[0-9]*[-.]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-.]
^analytics?[-.]
^banners?[-.]
^beacons?[0-9]*[-.]
^count(ers?)?[0-9]*[-.]
^pixels?[-.]
^stat(s|istics)?[0-9]*[-.]
^track(ers?|ing)?[0-9]*[-.]
^traff(ic)?[-.]
google-{0,}(analytic|syndication|(ad[a-z0-9]*|tag)-{0,}service)[s]\.[a-z]{2,7}$
google-{0,}(analytics{0,}|(ad|tag)manager)\.[a-z]{2,7}$
double-{0,}clic(k|k[.]*by-{0,}google)\.[a-z]{2,7}$
(google|partner|pub)-{0,}ads{0,}-{0,}\.[a-z]{2,7}$
(^|\.)fbsbx\.com\.online-metrix\.net$
(^|\.)m\.me$
^(.+\.)?amp\..+\.com$
^(.+\.)?ampproject\.org$
^(.+\.)?amp\.cloudflare\.com$
^(.+\.)?cdn\.ampproject\.org$
([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo\.com/
([A-Za-z0-9.-]*\.)?secure\.footprint\.net/
([A-Za-z0-9.-]*\.)?match\.com/
([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo(\.\w{2}|\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?sitescout(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?appnexus(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?evidon(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?mediamath(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?scorecardresearch(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?flashtalking(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?turn(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?mathtag(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?googlesyndication(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?s\.yimg\.com/cv/ae/us/audience/
([A-Za-z0-9.-]*\.)?clicks\.beap/
([A-Za-z0-9.-]*\.)?.doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?yieldmanager(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?w55c(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?adnxs(\.\w{2}\.\w{2}|\.\w{2,4})/
([A-Za-z0-9.-]*\.)?advertising\.com/
([A-Za-z0-9.-]*\.)?evidon\.com/
([A-Za-z0-9.-]*\.)?scorecardresearch\.com/
([A-Za-z0-9.-]*\.)?flashtalking\.com/
([A-Za-z0-9.-]*\.)?turn\.com/
([A-Za-z0-9.-]*\.)?mathtag\.com/
([A-Za-z0-9.-]*\.)?surveylink/
([A-Za-z0-9.-]*\.)?info\.yahoo\.com/
([A-Za-z0-9.-]*\.)?ads\.yahoo\.com/
([A-Za-z0-9.-]*\.)?global\.ard\.yahoo\.com/
```

```
/^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]/
/^(.+[_.-])?telemetry[_.-]/
/^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]/
/^adim(age|g)s?[0-9]*[_.-]/
/^adtrack(er|ing)?[0-9]*[_.-]/
/^advert(s|is(ing|ements?))?[0-9]*[_.-]/
/^aff(iliat(es?|ion))?[_.-]/
/^analytics?[_.-]/
/^banners?[_.-]/
/^beacons?[0-9]*[_.-]/
/^count(ers?)?[0-9]*[_.-]/
/^mads\./
/^pixels?[-.]/
/^popup?[_.-]/
/^stat(s|istics)?[0-9]*[_.-]/
```

<h2 <h2 align="center"><a href="https://github.com/mmotti/pihole-regex">Mmotti - Pihole Regex</a></h2>

```
^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^adim(age|g)s?[0-9]*[_.-]
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
^mads\.
^pixels?[-.]
^stat(s|istics)?[0-9]*[_.-]
```

```
^(.+[_.-])?(facebook|fb(cdn|sbx)?|tfbnw)\.[^.]+$
```

```
^(.+[_.-])?(twitter|twimg|cms-twdigitalassets)\.(co\.)?[^.]+$
```

<h2 <h2 align="center"><a href="https://github.com/MajkiIT/polish-ads-filter">MajkiIT - Polish Ads Filters</a></h2>

```
^adserver\.
^adv\.
^advserver\.
^pixel\.
#
#[imported]
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[-_.])??ad[sxv]?[0-9]*[-_.]
^(.+[-_.])??telemetry[-.]
^(.+[-_.])??xn--
^adim(age|g)s?[0-9]*[-_.]
^adtrack(er|ing)?[0-9]*[-.]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-.]
^analytics?[-.]
^banners?[-.]
^beacons?[0-9]*[-.]
^count(ers?)?[0-9]*[-.]
^pixels?[-.]
^stat(s|istics)?[0-9]*[-.]
^track(ers?|ing)?[0-9]*[-.]
^traff(ic)?[-.]
(.*)\.g00\.(.*).
```

<h2 <h2 align="center"><a href="">[Levi2288 - Advanced Blocklist](https://github.com/Levi2288/AdvancedBlockList)

```
^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^adim(age|g)s?[0-9]*[_.-]
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
^mads\.
^pixels?[-.]
^stat(s|istics)?[0-9]*[_.-]
```

<h2 <h2 align="center"><a href="">[x0uid - SpotifyAdBlock](https://github.com/x0uid/SpotifyAdBlock)

```
(\.|^)google-analytics\.com$
(\.|^)googlesyndication\.com$
(\.|^)googleadservices\.com$
(\.|^)2mdn\.net$
(\.|^)moatads\.com$
(\.|^)doubleclick\.net$
(\.|^)safeframe\.googlesyndication\.com$
(\.|^)smaato\.net$
(\.|^)fastclick\.net&
```

<h2 <h2 align="center"><a href="">[Stevoh6  - Pihole---Allow-and-Block-lists](https://github.com/stevoh6/Pihole---Allow-and-Block-lists)

```
^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|^.+[_.-]ad([sxv]?[0-9]*|system)[_.-]
^adim(age|g)s?[0-9]*[_.-]
^adtrack(er|ing)?[0-9]*[-.]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
^mads\.
^pixels?[-.]
^stat(s|istics)?[0-9]*[_.-]
^track(ers?|ing)?[0-9]*[-.]
^track(ing)?[0-9]*[_.-]
```

```
(\.|^)doubleclick\.net$
(\.|^)etargetnet\.com$
(\.|^)google-analytics\.com$
(\.|^)googlesyndication\.com$
(\.|^)googletagmanager\.com$
(\.|^)safeframe\.googlesyndication\.com$
(\.|^)t\.eloqua\.com$
```

```
(\.|^)wpc\.*\.net$
(\.|^)yovoads\.com$
(^|.)geo[-.]?
(^|.)telemetry[-.]
(^|\.)disqus\.com$
(^|\.)experience\.tinypass\.com$
(^|\.)scontent\.[\s]+\.fbcdn\.net$
(^|\.)tile\.openweathermap\.org$
(ads|captive|logs)\.roku\.com$
.*\.g00\..*
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[-_.])??xn--
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
```

<h2 align="center">##  https://github.com/mmotti/pihole-regex/blob/master/miscellaneous/amp.list

```
^(.+[_.-])?amp(project)?\.
```

<h2 align="center">##  https://github.com/mmotti/pihole-regex/blob/master/user%20suggested/first-party%20trackers.list

```
^(.+[_.-])?dnsdelegation\.io$
```

<h2 align="center">##  https://github.com/mmotti/pihole-regex/blob/master/user%20suggested/first-party%20trackers.list

```
^(.+[_.-])?eulerian\.net$
^(.+[_.-])?telemetry[_.-]
```

<h2 align="center">##  https://github.com/mmotti/pihole-regex/blob/master/miscellaneous/internationalized%20domains.list

```
^(www[0-9]*\.)?xn--
```

<h2 <h2 align="center"><a href="">[Peatrick - My Pihole Lists](https://github.com/peatrick/my-pihole-lists)

```
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]
^(.+[-_.])??xn--
^adim(age|g)s?[0-9]*[-_.]
^adtrack(er|ing)?[0-9]*[-.]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-.]
^analytics?[-.]
^banners?[-.]
^beacons?[0-9]*[-.]
^count(ers?)?[0-9]*[-.]
^pixels?[-.]
^stat(s|istics)?[0-9]*[-.]
^telemetry[-.]
^track(ers?|ing)?[0-9]*[-.]
^traff(ic)?[-.]
(^|\.)roku\.com$
```

<h2 <h2 align="center"><a href="">[Anthony-wang - PiHole Blocklist](https://github.com/anthony-wang/PiHoleBlocklist)


```
((^)|(.))adchoice.
((^)|(.))ads.roku.com
((^)|(.))adsdk.
((^)|(.))adserv.
((^)|(.))analytic.
((^)|(.))logs.roku.com
((^)|(.))metric.
((^)|(.))telemetry.
((^)|(.))tracking.
(.*)\.g00\.(.*)
(^|\.)xn--.*$
(ads|captive|cloudservices|logs).roku.com$
.*\.g00\..*
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]
^(.+[-_.])??xn--
^adim(age|g)s?[0-9]*[-_.]
^adtrack(er|ing)?[0-9]*[-.]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-.]
^analytics?[-.]
^banners?[-.]
^beacons?[0-9]*[-.]
^count(ers?)?[0-9]*[-.]
^pixels?[-.]
^stat(s|istics)?[0-9]*[-.]
^telemetry[-.]
^track(ers?|ing)?[0-9]*[-.]
^traff(ic)?[-.]
```

```
^ad([sxv]?[0-9]*|system)[-_.]([^.[:space:]]+\.){1,}|[-_.]ad([sxv]?[0-9]*|system)[-_.]
^(.+[-_.])?adse?rv(er?|ice)?s?[0-9]*[-_.]
^(.+[-_.])?telemetry[-_.]
^adtrack(er|ing)?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-_.]
^analytics?[-_.]
^banners?[-_.]
^beacons?[0-9]*[-_.]
^count(ers?)?[0-9]*[-_.]
^mads\.
^pixels?[-_.]
^stat(s|istics)?[0-9]*[-_.]
```

<h2 <h2 align="center"><a href="">[Reddit - Pihole](https://www.reddit.com/r/pihole/comments/awvk13/can_anyone_recommend_some_good_regex_filters/)

```
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]

^adim(age|g)s?[0-9]*[-_.]

^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]

^adtrack(er|ing)?[0-9]*[-.]

^advert(s|is(ing|ements?))?[0-9]*[-_.]

^aff(iliat(es?|ion))?[-.]

^analytics?[-.]

^banners?[-.]

^beacons?[0-9]*[-.]

^count(ers?)?[0-9]*[-.]

^pixels?[-.]

^stat(s|istics)?[0-9]*[-.]

^telemetry[-.]

^track(ers?|ing)?[0-9]*[-.]

^traff(ic)?[-.]

(^|\.)xn--.*$
```

<h2 <h2 align="center"><a href="">[Xlimit91 - Xlimit91 Blocklist](https://github.com/xlimit91/xlimit91-block-list)

```
^(.+[_.-])?ad[sxv]?[0-9]*[_.-]
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^(www[0-9]*\.)?xn--
^adim(age|g)s?[0-9]*[_.-]
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
^pixels?[-.]
^stat(s|istics)?[0-9]*[_.-]
^track(ing)?[0-9]*[_.-]
```


<h2 <h2 align="center"><a href="">[PebbleOG - Pihole Regex](https://github.com/PebbleOG/pihole-regex)

```
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]
^(.+[-_.])??xn--
^adim(age|g)s?[0-9]*[-_.]
^adtrack(er|ing)?[0-9]*[-.]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^aff(iliat(es?|ion))?[-.]
^analytics?[-.]
^banners?[-.]
^beacons?[0-9]*[-.]
^count(ers?)?[0-9]*[-.]
^pixels?[-.]
^stat(s|istics)?[0-9]*[-.]
^telemetry[-.]
^track(ers?|ing)?[0-9]*[-.]
^traff(ic)?[-.]
(.*\.|^)((think)?with)?google($|((adservices|apis|mail|static|syndication|tagmanager|tagservices|usercontent|zip|-analytics)($|\..+)))
(.*)\.g0[0-9]\.(.*)
^.+\.(accountant|biz|bid|christmas|click|country|cricket|date|download)$
^.+\.(faith|gdn|gq|kim|life|loan|world|xin|xyz|zip|link)$
^.+\.(men|mom|ninja|pro|racing|realtor|science|space|stream|top|win|work)$
^.+\.(ru|cn|ro|ml|ga|gq|cf|tk|pw|ua|ug|ve|site|club|host|party)$
^.+\.(in|hosting|online|cc|sh|pl|network|la|me|bg|br|website|live)$
^.+\.(id|cash|za|red|ltd|cloud|ae|trade|name|store)$
^.+\.(love|luxe|realestate)$
^https?://([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo\.com/
^https?://([A-Za-z0-9.-]*\.)?secure\.footprint\.net/
^https?://([A-Za-z0-9.-]*\.)?match\.com/
^https?://([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo(\.\w{2}\.\w{2}|\.\w{2 ,4})/
^https?://([A-Za-z0-9.-]*\.)?sitescout(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?appnexus(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?evidon(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?mediamath(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?scorecardresearch(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?flashtalking(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?turn(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?mathtag(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?googlesyndication(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?s\.yimg\.com/cv/ae/us/audience/
^https?://([A-Za-z0-9.-]*\.)?clicks\.beap/
^https?://([A-Za-z0-9.-]*\.)?.doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?yieldmanager(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?w55c(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?adnxs(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?advertising\.com/
^https?://([A-Za-z0-9.-]*\.)?evidon\.com/
^https?://([A-Za-z0-9.-]*\.)?scorecardresearch\.com/
^https?://([A-Za-z0-9.-]*\.)?flashtalking\.com/
^https?://([A-Za-z0-9.-]*\.)?turn\.com/
^https?://([A-Za-z0-9.-]*\.)?mathtag\.com/
^https?://([A-Za-z0-9.-]*\.)?surveylink/
^https?://([A-Za-z0-9.-]*\.)?info\.yahoo\.com/
^https?://([A-Za-z0-9.-]*\.)?ads\.yahoo\.com/
^https?://([A-Za-z0-9.-]*\.)?global\.ard\.yahoo\.com/
```

```
^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^adim(age|g)s?[0-9]*[_.-]
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
^mads\.
^pixels?[-.]
^stat(s|istics)?[0-9]*[_.-]
```

<h2 <h2 align="center"><a href="">[Ojmarcelino - Blocklists](https://github.imc.re/ojmarcelino/blocklists)

```
^(.+[_.-])?graph[_.-]
^adim(age|g)s?[0-9]*[-_.]
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|[_.-]ad([sxv]?[0-9]*|system)[_.-]
(\.|^)adsystem\.com$
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[-_.]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
(\.|^)doubleclick\.net$
^mads\.
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]
^pixels?[-.]
^stat(s|istics)?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^track(ers?|ing)?[0-9]*[-.]
^traff(ic)?[-.]
^(.+[-_.])??xn--
^([A-Za-z0-9.-]*\.)?mp.microsoft\.com\.?/
^https?://([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo\.com/
^https?://([A-Za-z0-9.-]*\.)?secure\.footprint\.net/
^https?://([A-Za-z0-9.-]*\.)?match\.com/
^https?://([A-Za-z0-9.-]*\.)?clicks\.beap\.bc\.yahoo(\.\w{2}\.\w{2}|\.\w{2 ,4})/
^https?://([A-Za-z0-9.-]*\.)?sitescout(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?appnexus(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?evidon(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?mediamath(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?scorecardresearch(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?flashtalking(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?turn(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?mathtag(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?googlesyndication(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?s\.yimg\.com/cv/ae/us/audience/
^https?://([A-Za-z0-9.-]*\.)?clicks\.beap/
^https?://([A-Za-z0-9.-]*\.)?.doubleclick(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?yieldmanager(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?w55c(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?adnxs(\.\w{2}\.\w{2}|\.\w{2,4})/
^https?://([A-Za-z0-9.-]*\.)?advertising\.com/
^https?://([A-Za-z0-9.-]*\.)?evidon\.com/
^https?://([A-Za-z0-9.-]*\.)?scorecardresearch\.com/
^https?://([A-Za-z0-9.-]*\.)?flashtalking\.com/
^https?://([A-Za-z0-9.-]*\.)?turn\.com/
^https?://([A-Za-z0-9.-]*\.)?mathtag\.com/
^https?://([A-Za-z0-9.-]*\.)?surveylink/
^https?://([A-Za-z0-9.-]*\.)?info\.yahoo\.com/
^https?://([A-Za-z0-9.-]*\.)?ads\.yahoo\.com/
^https?://([A-Za-z0-9.-]*\.)?global\.ard\.yahoo\.com/
(^|\.)buffpanel\.com$
(^|\.)bugsnag\.com$
(^|\.)redshell\.io$
(^|\.)treasuredata\.com$
(^|\.)unity(|3d)\.com$
(^|\.)unityads(|\.co)\.com$
```

<h2 <h2 align="center"><a href="https://surajdeshpande.wordpress.com/2021/01/23/pihole-adlist-and-regex-blacklist/">A Programming Blog</a></h2>

```
^adim(age|g)s?[0-9]*[-_.]	
	
^(.+[-_.])??adse?rv(er?|ice)?s?[0-9]*[-.]	
	
^adtrack(er|ing)?[0-9]*[-.]	
	
^advert(s|is(ing|ements?))?[0-9]*[-_.]	
	
^aff(iliat(es?|ion))?[-.]	
	
^analytics?[-.]	
	
^banners?[-.]	
	
^beacons?[0-9]*[-.]	
	
^count(ers?)?[0-9]*[-.]	
	
^(.+[-_.])??m?ad[sxv]?[0-9]*[-_.]	
	
^pixels?[-.]	
	
^stat(s|istics)?[0-9]*[-.]	
	
^telemetry[-.]	
	
^track(ers?|ing)?[0-9]*[-.]	
	
^traff(ic)?[-.]	
	
^(.+[-_.])??xn--	
	
^tiles\..*services\.mozilla\.com$	
	
(^|\.)xbcs\.net$	
	
(^|\.)ads\.roku\.com$	
	
(^|\.)logs\.roku\.com$	
	
(^|\.)avcdn\.net$	
	
(^|\.)cn$
```

<h2 align="center"><a href="https://www.bentasker.co.uk/posts/documentation/general/refreshing-piholes-regex-block-list-from-external-sources.html">Bentasker</a></h2>

```
^tracking\..+\.miui.com$
^tracking\..+\.miui.(com){#3}$
```

<h2 align="center"><a href="https://gitlab.com/nezu81/pihole-mega-lists">Pihole Mega Lists</a></h2>

```
/^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]/
/^(.+[_.-])?telemetry[_.-]/
/^ad([sxv]?[0-9]*|system)[_.-]([^.[:space:]]+\.){1,}|^.+[_.-]ad([sxv]?[0-9]*|system)[_.-]/
/^adim(age|g)s?[0-9]*[_.-]/
/^adtrack(er|ing)?[0-9]*[_.-]/
/^advert(s|is(ing|ements?))?[0-9]*[_.-]/
/^aff(iliat(es?|ion))?[_.-]/
/^analytics?[_.-]/
/^banners?[_.-]/
/^beacons?[0-9]*[_.-]/
/^count(ers?)?[0-9]*[_.-]/
/^mads\./
/^pixels?[-.]/
/^stat(s|istics)?[0-9]*[_.-]/
/^track(ing)?[0-9]*[_.-]/
/(^|.)bid$/
/(^|.)biz$/
/(^|.)br$/
/(^|.)by$/
/(^|.)cc$/
/(^|.)cf$/
/(^|.)club$/
/(^|.)cn$/
/(^|.)cz$/
/(^|.)degree$/
/(^|.)download$/
/(^|.)ga$/
/(^|.)gdn$/
/(^|.)gq$/
/(^|.)haus$/
/(^|.)jp$/
/(^|.)ke$/
/(^|.)kr$/
/(^|.)link$/
/(^|.)live$/
/(^|.)lt$/
/(^|.)market$/
/(^|.)me$/
/(^|.)ml$/
/(^|.)mx$/
/(^|.)my$/
/(^|.)name$/
/(^|.)online$/
/(^|.)pk$/
/(^|.)pl$/
/(^|.)post$/
/(^|.)pro$/
/(^|.)pt$/
/(^|.)pw$/
/(^|.)re$/
/(^|.)ro$/
/(^|.)rocks$/
/(^|.)ru$/
/(^|.)sale$/
/(^|.)shop$/
/(^|.)site$/
/(^|.)sk$/
/(^|.)space$/
/(^|.)su$/
/(^|.)tech$/
/(^|.)tk$/
/(^|.)trade$/
/(^|.)host$/
/(^|.)science$/
/(^|.)services$/
/(^|.)fi$/
/(^|.)review$/
/(^|.)date$/
/(^|.)support$/
/(^|.)life$/
/(^|.)loan$/
/(^|.)ltd$/
/(^|.)stream$/
/(^|.)icu$/
/(^|.)top$/
/(^|.)tr$/
/(^|.)tv$/
/(^|.)tw$/
/(^|.)ua$/
/(^|.)vn$/
/(^|.)website$/
/(^|.)win$/
/(^|.)world$/
/(^|.)ws$/
/(^|.)xyz$/
/(^|.)za$/
/(^|.)app$/
/(^|.)asia$/
/(^|.)cloud$/
/(^|.)today$/
/(^|.)ge$/
/(^|.)si$/
/(^|.)am$/
/(^|.)ph$/
/(^|.)rs$/
/(^|.)business$/
/(^|.)fun$/
/(^|.)realestate$/
/(^|.)network$/
/(^|.)global$/
/(^|.)world$/
/(^|.)ooo$/
/(^|.)agency$/
/(^|.)work$/
/(^|.)tc$/
/(^|.)no$/
```



```
^pixels?[-.]
^(.+[_.-])?ad[sxv]?[0-9]*[_.-]
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^(www[0-9]*\.)?xn--
^adim(age|g)s?[0-9]*[_.-]
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
^mads\.
^stat(s|istics)?[0-9]*[_.-]
^track(ers?|ing)?[0-9]*[_.-]
^traff(ic)?[.-]
^ad-js\.
^static\.
^pixel(s*)?[-.]
^shop((ping)*)\.
\.ru$
```

```
((([-,a-z,1-9]*)\.)*([-,a-z,1-9]*)banner(([-,a-z,1-9]*)\.)*([a-z])*)
((([-,a-z,1-9]*)\.)*([-,a-z,1-9]*)analy(se|tik|tic)(([-,a-z,1-9]*)\.)*([a-z])*)
((([-,a-z,1-9]*)\.)*([-,a-z,1-9]*)connect(([-,a-z,1-9]*)\.)*([a-z])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)click(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)ad(ver(tising)*|(tisment)*)*(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)track((ing)*)(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)count((er|ing)*)(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)traf((fic)*)(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)sponsor((ing)*)(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)spy(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)samsungad(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)samsungcr(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)banner(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)aff(iliat(es?|ion))(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)deals(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)telemetr(ie|y)*(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)gstatic(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)1px(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
((([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)pixel(([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$]*)\.)*([-,_,a-z,A-Z,1-9,:,/,\\,=,?,&,%,$])*)
^(.+[_.-])?ad[sxv]?[0-9]*[_.-]
^(.+[_.-])?adse?rv(er?|ice)?s?[0-9]*[_.-]
^(.+[_.-])?telemetry[_.-]
^(www[0-9]*\.)?xn--
^adim(age|g)s?[0-9]*[_.-]
^adtrack(er|ing)?[0-9]*[_.-]
^advert(s|is(ing|ements?))?[0-9]*[_.-]
^aff(iliat(es?|ion))?[_.-]
^analytics?[_.-]
^banners?[_.-]
^beacons?[0-9]*[_.-]
^count(ers?)?[0-9]*[_.-]
^mads\.
^cdn\.
^stat(s|istics)?[0-9]*[_.-]
^track(ers?|ing)?[0-9]*[_.-]
^traff(ic)?[.-]
\.doubleclick\. net$
^static\.
^pubads.\?\.doubleclick\.net
^pixel(s*)?[-.]
^shop((ping)*)\.
^deal(s*)\.
doubleclick\.(net|org|com|de)$
^(ad)[a-z,1-9]*\.
^([a-z,1-9]*)\.ad([a-z,1-9]*)\.((de)|(eu)|(com)|(org)|(net))














