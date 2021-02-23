## Classic Crypto - 50 points ##
'''
Tusec mfy eaam gfqclaef oomgh ok. Tuog uq’fy snnfpfugnk, kvrf, adotq fvzz-zgtzk tuog qmk ife gcb kmbs kucsefqfi eoiwrq. Fvy lrhhu ge, ky srr oyj fvyke gvvlsg. Ufoamzmgg ck a fmzzaz, fakr huc rzuy a pchlffs xlvsf. Rts zdat wf rts mqmocy mr hbw cbiardm. Imr zofie olw ohf ayfwifay wqczhcly. Js npq bil Aacawycok – wr frndsmwng huc uryslf cs Yzchqmbif. Rdinz, fesrbaa ufd gvr pqainay cs aqbmgrfvvn. Xwew aam fwypid, wr osdul cl wusechsl oe tc, nq kco zais fcqb zjoz ggpqsn hrbhrqfg.

Qw hnjr la zysdrff, aujcdinbf md giddvseq. Is uje nzy mzs. Qw rhb bnqfulibbf zqqumsr huyf wm ohnh gfq ulguc rrauryk tb rb. Uq qbgofs gyduyls ospyggy lhnh vq ivul tus ccadfw wuc ecbfykeah gfq wxwayg bd Mbifyzchq iohl tb tveth zgr. Gvr uaffv if wa rdcotlr. Kr qqs cl eisew pos – oae, dbtqfnq, mhfqcd. Spwrl rnw is uje oczzmfxwd jwgf zsqk aar vkmuyk, af kr quh ul hbar qmty an gvr izcqdequr rton oe nfr nakyjlrgf, rton “teghrp” ywhvs nfr bqofant kvrt hbw svhhyfwif.

Bhh jfmh cx ybi pmgzx te gvr atohye lch umbn lo fsr? G’y hqwngm sghs swaeg bjp. W qwng hb qovigl nbq aazfwgr. W smgubl fbf zw ocoftem gfqb agt n xbz mbx havr zw forws. Vt lmg ayl mr ca rts mlrrsg G icodda’h rtqb lwgvggcd ch qohf eypol. A az xhqf ohgtuse nqfmgn vb n qqo ix fnqrq.

Nin an pmocdgjscr kr yds xafsseczh. Qw hrzccp tlwe gvr nqcjde bt Rekdn. Oe usynqr zaguh nemwhkt Vgeyqz uk ig ogrqajleq urlaqcve. Js rvbcmwd zcec fvuf fvtgw fvimsnbq nmsxgpuwyce olguar gfq kijlq. Kr daiazt gvr bdia uaehrje. Ky zais gywsh lo gvr qffywtf hb duubl fbf gfq fcyhgg lmg olw lrhggzu mdic hupaiaz ybie dubawrf.

Kr yds Ufoamzmgg.

Nze szne ug "zdat{qyyegcuvvurlqfy}"

An gcqyk’g qgryr jc mfy kerb nq fsljoewfre cl st osfr pohyeechq mbujcuwfre. Ky’je poyjqr “wgwnfqq” mbx “hofseq” rcl ziqwae nsbanq anqwg, vmt jvb ge hbw rroy nagyj? Wr hniq oqsy gvr dmqy snq zryhs ifll huc ysmkats. Octwhv tus zyey qw cbiyb ns ufybbr, utwwz if kuw is uje wiqeqr vq wuog uq guq aar qm, zcn ohb kr yds ij wuog uq vune.

Js rvugn oigvbsf bulibbnjuhs, kkvb pmxcoj oe frjuucguf pvye.
'''

## Solution ##

Based on the format of the flags and the number of letters, I assumed 'Nze szne ug "zdat{qyyegcuvvurlqfy}"' says "The flag is "flag{*flag*}". Using a Vigenere square like the one below, you can find the key by going to the column of the plaintext letter and finding the encrypted letter in that column, which will give the row of the corresponding key letter.  For example, for the encrypted word "Nze", "The" would be the plaintext and "USA" is the corresponding part of the key. 
![Vigenere Square](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Vigen%C3%A8re_square_shading.svg/220px-Vigen%C3%A8re_square_shading.svg.png)

By doing this we can figure out that the key is **ANONYMOUS**, and the flag is therefore 'flag{classicvigenere}' (The part of key we'd use for the contents of the flag is **ONYMOUSAN**)

Alternatively, using the **ANONYMOUS** key we can translate the entire text using a Vigenere decoder such as https://www.boxentriq.com/code-breaking/vigenere-cipher, which gives us the decoded message:
'''
There are many theories about us. That we’re anarchists, kids, crazy film-buffs that saw one too many superhero movies. The truth is, we are all these things. Anonymous is a symbol, like the flag a country flies. The flag is the symbol of the country. Our masks are our national identity. We are not Anonymous – we represent the ideals of Anonymous. Truth, freedom and the removal of censorship. Like any symbol, we affix it wherever we go, as you have seen from street protests.

We have no leaders, civilians or soldiers. We are all one. We run operations because that is what the group decides to do. We choose targets because that is what the people who represent the ideals of Anonymous want to fight for. The world is in trouble. We see it every day – war, poverty, murder. Every day we are bombarded with news and images, as we sit at home safe in the knowledge that we are powerless, that “better” minds are dealing with the situation.

But what if you could be the change you want to see? I’m twenty five years old. I went to school and college. I fought for my country then got a job and paid my taxes. If you met me on the street I wouldn’t even register on your radar. I am just another person in a sea of faces.

But in cyberspace we are different. We helped free the people of Egypt. We helped fight against Israel as it attempted genocide. We exposed more than fifty thousand paedophiles around the world. We fought the drug cartels. We have taken to the streets to fight for the rights you are letting slip through your fingers.

We are Anonymous.

The flag is "flag{classicvigenere}"

In today’s world we are seen as terrorists or at best dangerous anarchists. We’re called “cowards” and “posers” for hiding behind masks, but who is the real poser? We take away the face and leave only the message. Behind the mask we could be anyone, which is why we are judged by what we say and do, not who we are or what we have.

We exist without nationality, skin colour or religious bias.
'''

If you don't know the key this website can also do "auto-solve" and find the key for you.
