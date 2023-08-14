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
  gap: 20px; 
  margin: 0 auto;
  max-width: 1200px;
`;

const Card = styled.div`
  background-color: #fff;
  border-radius: 10px;
  padding: 10px;
  width: 20rem;
  max-width: 350px; /* Increased card size */
  text-align: left;
  background-color: rgba(255, 255, 255, 0.5);
  box-shadow: .125rem .125rem .375rem 0 rgba(74, 45, 197, .04), .5rem .5625rem 1.625rem 0 rgba(74, 45, 197, .07), 1.375rem 1.5rem 5rem 0 rgba(74, 45, 197, .11);
  backdrop-filter: blur(10px);
  margin: 20px;
`;
/* Decreased padding between images */
const CardImage = styled.img`
  max-width: 100%;
  height: 200px;
  border-radius: 8px;
`;

const CardTitle = styled.h2`
  margin-top: 15px;
  font-size: 24px;
`;

const BadgeWrapper = styled.div`
  margin-top: 10px;
`;

const Badge = styled.img`
  margin-right: 5px;
`;

const CardDescription = styled.p`
  margin-top: 10px;
  font-size: 16px;
  text-align: justify;
`;


const GoToProjectButton = styled.button`
  background-color: ${props => props.color};
  border: none;
  padding: 10px 20px;
  color: white;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
  margin: 10px;
`;


const headingStyle = {
    marginBottom: '1rem',
    fontSize: '2.5rem',
    fontWeight: 'bold',
    textAlign: 'center',
};


const ProjectCard = ({ imageSrc, alt, title, description, color, type }) => {
    const openProjectLink = (url) => {
        window.open(url, '_blank');
    };
    return (
        <Card>
            <div style={{
                display: "flex",
                height: "100%",
                flexDirection: "column",
                justifyContent: "space-between"
            }}>
                <div style={{ order: 1 }}>
                    <CardImage src={imageSrc} alt={alt} />

                    <CardTitle><a href={"https://github.com/sumithemmadi/" + title} style={{ textDecoration: "none", color: color }}>{title}</a></CardTitle>
                    <BadgeWrapper>
                        {type === 'npm' && (
                            <span>
                                <Badge src={"https://img.shields.io/npm/v/" + title + ".svg"} alt="version" />
                                <Badge src={"https://img.shields.io/npm/dt/" + title + ".svg"} alt="Download" />
                            </span>
                        )}
                        {type === 'pip' && (
                            <span>
                                <Badge src={"https://img.shields.io/pypi/dm/" + title + ".svg"} alt="version" />
                            </span>
                        )}

                        <Badge src={"https://img.shields.io/github/stars/sumithemmadi/" + title} alt="GIT Stars" />
                        <Badge src={"https://img.shields.io/github/forks/sumithemmadi/" + title} alt="GIT Forks" />
                        <Badge src={"https://img.shields.io/github/stars/sumithemmadi/" + title} alt="GIT Stars" />
                        <Badge src={"https://img.shields.io/github/issues/sumithemmadi/" + title} alt="GIT Stars" />
                        <Badge src="https://img.shields.io/github/sponsors/sumithemmadi" alt="GitHub Sponsors" />

                    </BadgeWrapper>
                    <div style={{ overflow: 'hidden' }}>
                        <CardDescription>{description}</CardDescription>
                    </div>
                </div>
                <div style={{
                    order: 2,
                    display: "flex",
                    justifyContent: "space-between"
                }}>
                    <GoToProjectButton color={color} onClick={() => openProjectLink("https://github.com/sumithemmadi/" + title)}>GO TO PROJECT</GoToProjectButton>
                    <GoToProjectButton color={color} onClick={() => openProjectLink("URL_TO_VIEW_DEMO")}>VIEW DEMO</GoToProjectButton>
                </div>
            </div>
        </Card>
    );
};

const Projects = () => {
    return (
        <Section>
            <h1 style={headingStyle} id="projects" >Projects</h1>
            <br></br>
            <br></br>
            <Container>
                <ProjectCard
                    imageSrc="https://opengraph.githubassets.com/83b8abc33a7b26898a4846558d1c70d88bb7c08a9ac0493e8eccf7cd2e683d47/sumithemmadi/truecallerjs"
                    alt="truecaller-logo"
                    title="truecallerjs"
                    description="TruecallerJS is a library for retrieving phone number details using the Truecaller API. It provides a simple and convenient way to access information about phone numbers in your Node.js, JavaScript, and TypeScript projects."
                    color="rgb(26, 146, 245)"
                    type="npm"
                />
                <ProjectCard
                    imageSrc="https://opengraph.githubassets.com/83b8abc33a7b26898a4846558d1c70d88bb7c08a9ac0493e8eccf7cd2e683d47/sumithemmadi/json-to-plain-text"
                    alt="json-logo"
                    title="json-to-plain-text"
                    description="json-to-plain-text is a npm module that converts JSON-like data or plain JavaScript objects to a formatted plain text representation. It allows you to convert JSON-like data or plain JavaScript objects into human-readable format."
                    color="rgb(255, 7, 110)"
                    type="npm"
                />
                <ProjectCard
                    imageSrc="https://opengraph.githubassets.com/83b8abc33a7b26898a4846558d1c70d88bb7c08a9ac0493e8eccf7cd2e683d47/sumithemmadi/truecallerpy"
                    alt="truecaller-logo"
                    title="truecallerpy"
                    description="TruecallerPy is a Python package that provides functionalities to interact with the Truecaller API. It allows you to perform login, OTP verification, and phone number search using Truecaller."
                    color="rgb(26, 146, 245)"
                    type="pip"
                />
                <ProjectCard
                    imageSrc="https://opengraph.githubassets.com/83b8abc33a7b26898a4846558d1c70d88bb7c08a9ac0493e8eccf7cd2e683d47/sumithemmadi/bhimupijs"
                    alt="json-logo"
                    title="bhimupijs"
                    description="Bhimupijs is an npm module that can be used to validate, verify, and generate QR codes for UPI IDs. It is a lightweight and easy-to-use library, making it ideal for use in web applications."
                    color="rgb(255, 7, 110)"
                    type="npm"
                />
                <ProjectCard
                    imageSrc="https://opengraph.githubassets.com/83b8abc33a7b26898a4846558d1c70d88bb7c08a9ac0493e8eccf7cd2e683d47/sumithemmadi/totpjs"
                    alt="tor-logo"
                    title="totpjs"
                    description="totpjs/node-totpjs is a JavaScript library that implements the Time-based One-time Password (TOTP) algorithm. TOTP is a widely used method for two-factor authentication (2FA). It generates a unique one-time password (OTP) every 30 seconds, which can be used to authenticate a user."
                    color="rgb(144, 21, 245)"
                    type="npm1"
                />
                <ProjectCard
                    imageSrc="/assets/icons/tor-1200.png"
                    alt="tor-logo"
                    title="Tor-Onion-Service-On-Heroku"
                    description="Tor-Onion-Service-On-Heroku is a project that allows you to host an onion service on Heroku. An onion service is an anonymous network service that is exposed over the Tor network. This means that your service will be accessible through the Tor network, but it will be difficult to trace back to you."
                    color="rgb(144, 21, 245)"
                    type="github"
                />
            </Container>
        </Section>
    );
};

export default Projects;
