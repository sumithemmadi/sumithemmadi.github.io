import React from 'react';

const Footer = () => {
    return (
        <div className='site-width'>
            <footer className="footer-container">
                <div className="content-container2">
                    <div className="logo-section">
                        <a href="/" className="logo-link">
                            <img src="/assets/icons/logo.svg" className="logo" alt="sumith Logo" />
                            <span className="logo-text">Sumith Emmadi</span>
                        </a>
                    </div>
                    <ul className="links-section">
                        <li><a href="#about" className="footer-link">About</a></li>
                        <li><a href="#skills" className="footer-link">Skills</a></li>
                        <li><a href="#projects" className="footer-link">Projects</a></li>
                        <li><a href="#contact" className="footer-link">Contact</a></li>
                    </ul>
                </div>
                <hr className="divider" />
                <span className="copyright-text">© 2023 <a href="/" className="copyright-link">Sumith Emmadi™</a>. All Rights Reserved.</span>
            </footer>
        </div>
    );
}

export default Footer;
