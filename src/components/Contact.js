import React from 'react';
import "./Contact.css";

const ContactForm = () => {
    return (
        <section className="contactform-container" id='contact'>
            <div className="contactform-image">
                <div className="image-container1">
                    <img
                        src="/assets/images/contactme.png"
                        alt="sumith"
                        className="contactform-contact-image"
                    />
                </div>
            </div>
            <div className="contactform-content">
                <h2 className="contactform-heading">Contact Me</h2>
                <p className="contactform-paragraph">You can contact me from here</p>
                <div className="contactform-social-account">
                    <div className="contactform-bio-social-account">
                        <a href="mailto:sumithemmadi244@gmail.com" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/gmail.svg"
                                alt="Gmail-Logo"
                                loading="lazy"
                                className="contactform-social-logo"
                            />
                        </a>
                        <a href="https://in.linkedin.com/in/sumithemmadi" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/linkedin.svg"
                                alt="LinkedIn-Logo"
                                loading="lazy"
                                className="contactform-social-logo"
                            />
                        </a>
                        <a href="https://github.com/sumithemmadi/" id="github" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/github.svg"
                                alt="GitHub-Logo"
                                loading="lazy"
                                className="contactform-social-logo"
                            />
                        </a>
                        <a href="https://www.facebook.com/sumithemmadi" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/facebook.svg"
                                alt="Facebook-Logo"
                                loading="lazy"
                                className="contactform-social-logo"
                            />
                        </a>
                        <a href="https://www.instagram.com/sumithemmadi/" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/instagram.svg"
                                alt="Instagram-Logo"
                                loading="lazy"
                                className="contactform-social-logo"
                            />
                        </a>
                        <a href="https://t.me/sumithemmadi/" target="_blank" rel="noreferrer" >
                            <img
                                src="/assets/icons/sa/telegram.svg"
                                alt="Telegram_-Logo"
                                loading="lazy"
                                className="contactform-social-logo"
                            />
                        </a>
                    </div>
                </div>
                <hr className="divider" />
                <form style={{ marginTop: '2rem', marginRight: '15px' }}>
                    <div style={{ marginBottom: '1rem' }}>
                        <label htmlFor="email" style={{ marginBottom: '0.5rem', fontSize: '0.875rem', fontWeight: 'medium' }}>Your email</label>
                        <input type="email" id="email" className="contactform-input" placeholder="name@example.com" required />
                    </div>
                    <div style={{ marginBottom: '1rem' }}>
                        <label htmlFor="subject" style={{ marginBottom: '0.5rem', fontSize: '0.875rem', fontWeight: 'medium' }}>Subject</label>
                        <input type="text" id="subject" className="contactform-input" placeholder="Let me know why you are contacting me" required />
                    </div>
                    <div style={{ marginBottom: '1rem' }}>
                        <label htmlFor="message" style={{ marginBottom: '0.5rem', fontSize: '0.875rem', fontWeight: 'medium' }}>Your message</label>
                        <textarea id="message" rows="6" className="contactform-textarea" placeholder="Leave a message here..." />
                    </div>
                    <button type="submit" className="contactform-button">Send message</button>
                </form>
            </div>
        </section>
    );
};

export default ContactForm;


