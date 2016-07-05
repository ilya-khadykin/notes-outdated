package com.test.learning_selenium;

import org.openqa.selenium.WebDriver;

/**
 * Created by Ilya on 4/20/2016.
 */
public class GoogleHomePage {
    private WebDriver driver;
    private String baseURL;

    public GoogleHomePage(WebDriver driver) {
        this.driver = driver;
        baseURL = "https://www.google.com/";
    }
}
