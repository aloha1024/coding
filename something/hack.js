var CryptoJS = require('crypto-js')
var request = require('request-promise')

function encrypt(text, originKey) {
    var originKey = originKey.slice(0, 16),
        key = CryptoJS.enc.Utf8.parse(originKey),
        iv = CryptoJS.enc.Utf8.parse(originKey),
        msg = JSON.stringify(text)
    var ciphertext = CryptoJS.AES.encrypt(msg, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return ciphertext.toString()
}

function decrypt(text, originKey) {
    var originKey = originKey.slice(0, 16),
        key = CryptoJS.enc.Utf8.parse(originKey),
        iv = CryptoJS.enc.Utf8.parse(originKey)
    var bytes = CryptoJS.AES.decrypt(text, key, {
        iv: iv
    })
    var plaintext = CryptoJS.enc.Utf8.stringify(bytes)
    return plaintext
}

function extend(target) {
    var sources = [].slice.call(arguments, 1)
    sources.forEach(function (source) {
        for (var prop in source) {
            target[prop] = source[prop]
        }
    })
    return target
}

//修改此处的version和session_id,score是你想修改的分数,最高为100000
var version = 9,
    score = 412,
    session_id = 'TacxSz2ZnZo+S2JgJL6/5pEO2eU72aUGmFlDZdyOQxS98T8LOQXxXJN2x1kmosVhLeICMNz8f6g9OxMu1sJgEKpd3xbDwcUsdyx9TUFvhZT3gdQ3YawM2xMe+Ge/jdpLLedhllgTuxDT1W3039CA2g=='

var headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wx7c8d593b2c3a7703/' + version + '/page-frame.html',
    'Content-Type': 'application/json',
    'Accept-Language': 'zh-cn',
    'Accept': '*/*'
}
var base_req = {
    'base_req': {
        'session_id': session_id,
        'fast': 1
    }
}
var base_site = 'https://mp.weixin.qq.com/wxagame/'

var path = 'wxagame_getuserinfo'
request({
    method: 'POST',
    url: base_site + path,
    headers: headers,
    json: true,
    body: base_req
}).then(function (response) {
    // console.log(path, response) 
})

path = 'wxagame_getfriendsscore'
request({
    method: 'POST',
    url: base_site + path,
    headers: headers,
    json: true,
    body: base_req
}).then(function (response) {
    // console.log(response.my_user_info)
    var times = response.my_user_info.times + 1
    path = 'wxagame_init'
    request({
        method: 'POST',
        url: base_site + path,
        headers: headers,
        json: true,
        body: extend({}, { version: 9 }, base_req)
    }).then(function (response) {
        // console.log(path, response)
        var action = [],
            musicList = [],
            touchList = []
        // for (var i = 0; i < score; i++) {
        //     action.push([0.752, 1.32, false])
        //     musicList.push(false)
        //     touchList.push([185, 451])
        // }
        var data = {
            score: score,
            times: times,
            game_data: JSON.stringify({
                seed: Date.now(),
                action: action,
                musicList: musicList,
                touchList: touchList,
                version: 1
            })
        }
        path = 'wxagame_settlement'
        request({
            method: 'POST',
            url: base_site + path,
            headers: headers,
            json: true,
            body: extend({}, { action_data: encrypt(data, session_id) }, base_req)
        }).then(function (response) {
            // console.log(path, response)
            console.log('2018! Happy new year! 🎉')
        }).catch(function (error) {
            console.log(error)
        })
    })
}).catch(function (error) {
    console.log('something crash')
})