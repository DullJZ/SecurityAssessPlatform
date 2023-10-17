package com.cyxxuan.serverdemo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/exp")
public class ExpController {
    @GetMapping
    public String test(){
        return "hello exp";
    }
}
