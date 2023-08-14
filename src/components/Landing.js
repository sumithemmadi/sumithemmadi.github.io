import React from 'react';
// import './App.css';

function App() {
    return (
        <section className={`home`} id="home">
            <div className="profile-pic-container">
                <img
                    src="/assets/images/profile-pic.jpg"
                    alt="sumith"
                    loading="lazy"
                    className="home-img"
                />
            </div>
            <div className="bio">
                <div className="bio-info">
                    <span className="bio-hey">Hey, I'm</span>
                    <br></br>
                    <span className="bio-name">
                        <strong>Sumith Emmadi</strong>
                    </span>
                    <p className="bio-text">
                        Hey I'm sumith I'm web developer and undergraduate student at Indian
                        Institute of Information Technology, Surat.
                        <span className="bio-text-extra">
                            Dreaming up ideas and making them come true is where my passion lies.
                        </span>
                    </p>
                </div>
                <div className="social-account">
                    <div className="bio-social-account">
                        <a href="mailto:sumithemmadi244@gmail.com" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/gmail.svg"
                                alt="Gmail-Logo"
                                loading="lazy"
                                className="social-logo"
                            />
                        </a>
                        <a href="https://in.linkedin.com/in/sumithemmadi" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/linkedin.svg"
                                alt="LinkedIn-Logo"
                                loading="lazy"
                                className="social-logo"
                            />
                        </a>
                        <a href="https://github.com/sumithemmadi/" id="github" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/github.svg"
                                alt="GitHub-Logo"
                                loading="lazy"
                                className="social-logo"
                            />
                        </a>
                        <a href="https://www.facebook.com/sumithemmadi" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/facebook.svg"
                                alt="Facebook-Logo"
                                loading="lazy"
                                className="social-logo"
                            />
                        </a>
                        <a href="https://www.instagram.com/sumithemmadi/" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/instagram.svg"
                                alt="Instagram-Logo"
                                loading="lazy"
                                className="social-logo"
                            />
                        </a>
                        <a href="https://t.me/sumithemmadi/" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/telegram.svg"
                                alt="Telegram_-Logo"
                                loading="lazy"
                                className="social-logo"
                            />
                        </a>
                    </div>
                </div>
                <div className="go-down">
                    <a href="#about">
                        <img src="/assets/icons/go-down.svg" alt="Go Down" />
                    </a>
                </div>
            </div>
        </section>
    );
}

export default App;
