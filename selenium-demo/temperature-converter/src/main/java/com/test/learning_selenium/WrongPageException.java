package com.test.learning_selenium;

/**
 * Created by Ilya on 4/20/2016.
 */
public class WrongPageException extends RuntimeException {
    public WrongPageException(String message) {
        super(message);
    }
}
