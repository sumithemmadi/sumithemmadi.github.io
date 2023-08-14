import React from 'react';
import styled from 'styled-components';

const Section = styled.section`
//   background-color: #f6f6f6;
  padding: 60px 0;
  text-align: center;
`;

const Container = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px; /* Decreased padding between images */
  margin: 0 auto;
  max-width: 1200px;
`;

const About = () => {
    return (
        <Section>
            <Container>
                <div className="about-section" id="about">
                    <h1 className="heading-style">About Me</h1>
                    <div className="about-container">
                        <div className="image-container">
                            <img
                                src="/assets/images/profile-pic.jpg"
                                alt="sumith"
                                className="profile-image"
                            />
                        </div>
                        <div className="content-container">
                            {/* <div className="logo-container">
                            <img
                                src="/assets/icons/logo.svg"
                                alt="sumith"
                                className="logo"
                            />
                            </div> */}
                            <h2 className="name-heading">
                                <img
                                    src="/assets/icons/logo.svg"
                                    alt="sumith"
                                    className="logo"
                                />
                                Sumith Emmadi
                            </h2>
                            <div className="image-container2">
                                <img
                                    src="/assets/images/profile-pic.jpg"
                                    alt="sumith"
                                    className="profile-image"
                                />
                                <span className='abouttext1'>Hello there! 👋 I'm Sumith Emmadi, a passionate computer science engineering student currently pursuing my studies in the CSE branch at IIIT Surat. With a strong passion for coding and a background in computer science engineering, I have developed a solid foundation in software development. My dedication and enthusiasm drive me to constantly expand my skill set and stay up-to-date with the latest industry trends.</span>
                            </div>
                            <div className="description">
                                <span className='abouttext'>Hello there! 👋 I'm Sumith Emmadi, a passionate computer science engineering student currently pursuing my studies in the CSE branch at IIIT Surat. With a strong passion for coding and a background in computer science engineering, I have developed a solid foundation in software development. My dedication and enthusiasm drive me to constantly expand my skill set and stay up-to-date with the latest industry trends.</span>
                                <br></br>
                                <br></br>
                                I'm a versatile full stack developer with hands-on experience in various technologies. From crafting responsive front-end interfaces to building robust back-end systems, I enjoy the process of transforming ideas into functional applications. I also have a keen interest in machine learning, which allows me to apply data-driven approaches to solve complex problems and gain valuable insights from data.
                            </div>
                            <div className="cta-button">
                                <a
                                    className="cta-link"
                                    href="/resume"
                                >
                                    <span className="cta-text">
                                        <span className="cta-label">View my resume</span>
                                    </span>
                                    <svg
                                        width="24"
                                        height="24"
                                        viewBox="0 0 24 24"
                                        fill="none"
                                        xmlns="http://www.w3.org/2000/svg"
                                        className="cta-icon"
                                    >
                                        <path
                                            d="M13.5 4.5L21 12M21 12L13.5 19.5M21 12H3"
                                            stroke="currentColor"
                                            strokeWidth="2.5"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                        ></path>
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </Container>
        </Section>
    );
};

export default About;
