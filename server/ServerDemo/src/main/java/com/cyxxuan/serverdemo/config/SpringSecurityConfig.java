package com.cyxxuan.serverdemo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SpringSecurityConfig {
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests(c -> c.requestMatchers("/login").permitAll()
                .requestMatchers("/sup").hasRole("supervisor")
                .requestMatchers("/exp").hasRole("experimenter")
                .anyRequest().authenticated());
        http.csrf(c -> c.disable());
        http.formLogin(c -> c.defaultSuccessUrl("/"));
        return http.build();
    }
}
