package com.rubin.rpan;

import org.apache.commons.lang3.StringUtils;

import java.util.Random;

public class Test {

    public static void main(String[] args) {
        Random random = new Random();
        int count = -1;
        for (int i = 0; i < 10000; i++) {
            int ascii = random.nextInt(123 - 48) + 48;
            System.out.println(ascii);
            if(count>=122){
                count++;
            }
        }
        System.out.println("count："+count);
    }
    /**
     * 初始化随机字符池子
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
            randomCode[i] = (char)ascii;
        }
        return StringUtils.join(randomCode,"");
    }
}
