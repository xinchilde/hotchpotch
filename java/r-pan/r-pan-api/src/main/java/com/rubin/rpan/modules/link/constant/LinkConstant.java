package com.rubin.rpan.modules.link.constant;

/**
 *
 */
public class LinkConstant {

    /**
     * 短链redis key名称
     */
    public static final String REDIS_LINK = "short_url";

    /**
     * url正则匹配规则
     */
    public static final String REGEX_VERIFY_URL = "^((https|http|ftp|rtsp|mms)?://)"  //https、http、ftp、rtsp、mms
            + "?(([0-9a-z_!~*'().&=+$%-]+: )?[0-9a-z_!~*'().&=+$%-]+@)?" //ftp的user@
            + "(([0-9]{1,3}\\.){3}[0-9]{1,3}" // IP形式的URL- 例如：199.194.52.184
            + "|" // 允许IP和DOMAIN（域名）
            + "([0-9a-z_!~*'()-]+\\.)*" // 域名- www.
            + "([0-9a-z][0-9a-z-]{0,61})?[0-9a-z]\\." // 二级域名
            + "[a-z]{2,6})" // 第一级域名- .com or .museum
            + "(:[0-9]{1,5})?" // 端口号最大为65535,5位数
            + "((/?)|" // 如果没有文件名，则不需要斜杠
            + "(/[0-9a-z_!~*'().;?:@&=+$,%#-]+)+/?)$";
}
