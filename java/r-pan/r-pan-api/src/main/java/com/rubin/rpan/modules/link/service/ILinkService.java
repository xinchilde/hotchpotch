package com.rubin.rpan.modules.link.service;

/**
 * 短链接处理接口
 * Created by RubinChu on 2021/1/22 下午 4:11
 */
public interface ILinkService {

    /**
     * 保存短链接
     * @param url
     */
    String saveLink(String url);

    /**
     * 短链接解析
     * @param randomCode
     * @return
     */
    String urlParse(String randomCode);
}
