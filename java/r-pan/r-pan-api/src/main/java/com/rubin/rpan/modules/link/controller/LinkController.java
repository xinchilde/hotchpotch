package com.rubin.rpan.modules.link.controller;

import com.rubin.rpan.common.response.R;
import com.rubin.rpan.modules.link.service.ILinkService;
import io.swagger.annotations.Api;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

@Controller
@Validated
@Api(tags = "短链接接口")
public class LinkController {

    private static final Logger log = LoggerFactory.getLogger(LinkController.class);

    @Autowired
    @Qualifier(value = "linkServiceImpl")
    private ILinkService linkService;

    /**
     * 短链接转发
     *
     * @param randomCode
     * @return
     */
    @GetMapping("/link/{randomCode}")
    public String skipAddres(@PathVariable(required = true, name = "randomCode") String randomCode) {
        String redirectUrl = "redirect:" + linkService.urlParse(randomCode);
        return redirectUrl;
    }

    /**
     * 生成短链
     *
     * @param url
     * @return
     */
    @PostMapping("/link/createShortLink")
    @ResponseBody
    public R<String> saveLink(@RequestParam(required = true, name = "urlAddress") String url) {
        return R.data(linkService.saveLink(url));
    }
}
