// src/components/Header.js
import React, { useState } from 'react';

const Header = () => {
    const [theme, setTheme] = useState('light');

    const toggleTheme = () => {
        setTheme(theme === 'light' ? 'dark' : 'light');
    };

    return (
        <div className='site-width'>
            <header>
                <div className="site-nav">
                    <div className="site-logo-name">
                        <img src='/assets/icons/logo.svg' alt='logo' />
                        <h1 className='site-name'>Sumith Emmadi</h1>
                    </div>

                    <div className="site-menu">
                        <div className="menus">
                            <ul className="navigation">
                                <li><a href="#about" className="nav-link">About</a></li>
                                <li><a href="#skills" className="nav-link">Skills</a></li>
                                <li><a href="#projects" className="nav-link">Projects</a></li>
                                <li><a href="#contact" className="nav-link">Contact</a></li>
                            </ul>
                        </div>
                        <div className="theme-switcher">
                            <label htmlFor="theme-toggle" className="theme-toggle-label">
                                <input
                                    type="checkbox"
                                    id="theme-toggle"
                                    className="theme-toggle-checkbox"
                                    onChange={toggleTheme}
                                    checked={theme === 'dark'}
                                />
                                <div className="theme-toggle-slider"></div>
                            </label>
                        </div>
                        <button className="burger-menu" id="burger-menu">
                            <ion-icon className="bars" name="menu-outline"></ion-icon>
                        </button>
                    </div>
                </div>
            </header>
        </div>
    );
};

export default Header;
