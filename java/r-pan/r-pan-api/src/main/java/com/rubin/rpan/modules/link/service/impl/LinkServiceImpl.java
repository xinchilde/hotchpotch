package com.rubin.rpan.modules.link.service.impl;

import cn.hutool.core.util.ReUtil;
import com.rubin.rpan.common.exception.RPanException;
import com.rubin.rpan.common.util.RedisUtil;
import com.rubin.rpan.modules.link.constant.LinkConstant;
import com.rubin.rpan.modules.link.service.ILinkService;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import java.util.Random;

@Service("linkServiceImpl")
public class LinkServiceImpl implements ILinkService {

    @Autowired
    @Qualifier(value = "redisUtil")
    private RedisUtil redisUtil;

    private String linkDomain = "http://localhost:7000/link/";

    @Override
    public String saveLink(String url)  {
        //地址校验
        if (!ReUtil.isMatch(LinkConstant.REGEX_VERIFY_URL, url.toLowerCase())) {
            throw new RPanException("链接格式错误");
        }

        //获取随机码
        String randomCode = null;
        do {
            randomCode = getRandomCode();
        } while (redisUtil.getCacheMapValue(LinkConstant.REDIS_LINK, randomCode) != null);

        //缓存地址
        redisUtil.setCacheMapValue(LinkConstant.REDIS_LINK, randomCode, url);

        //返回短链地址
        String skipAddres = linkDomain + randomCode;
        return skipAddres;
    }

    @Override
    public String urlParse(String randomCode) {
        String cacheMapValue = redisUtil.getCacheMapValue(LinkConstant.REDIS_LINK, randomCode);
        return cacheMapValue;
    }

    /**
     * 获取随机字符串
     *
     * @return
     */
    private static String getRandomCode() {
        Character[] randomCode = new Character[6];
        Random random = new Random();

        for (int i = 0; i < randomCode.length; i++) {
            int ascii = 58;
            do {
                //ASCII: 数字(0~9) 48->57  小写字母(a~z)：64->90 大写字母(A~Z)：97->122
                ascii = random.nextInt(123 - 48) + 48;
            } while ((ascii > 57 && ascii < 65) || (ascii > 90 && ascii < 97));
            randomCode[i] = (char) ascii;
        }
        return StringUtils.join(randomCode, "");
    }
}
