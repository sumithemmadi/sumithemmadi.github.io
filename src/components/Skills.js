import React from "react";
import styled from "styled-components";

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

const skillsData = [
  {
    id: 1,
    name: "C",
    category: "Languages",
    imgUrl: "/assets/icons/pl/c.svg",
  },
  {
    id: 2,
    name: "C++",
    category: "Languages",
    imgUrl: "/assets/icons/pl/cpp.svg",
  },
  {
    id: 3,
    name: "bash",
    category: "Languages",
    imgUrl: "/assets/icons/pl/bash.svg",
  },
  {
    id: 4,
    name: "JavaScript",
    category: "Languages",
    imgUrl: "/assets/icons/pl/js.svg",
  },
  {
    id: 5,
    name: "Python",
    category: "Languages",
    imgUrl: "/assets/icons/pl/python.svg",
  },
  {
    id: 6,
    name: "TypeScript",
    category: "Languages",
    imgUrl: "/assets/icons/pl/typescript.svg",
  },
  {
    id: 7,
    name: "React.js",
    category: "Frontend",
    imgUrl: "/assets/icons/pl/reactjs.svg",
  },
  {
    id: 8,
    name: "Next.js",
    category: "Frontend",
    imgUrl: "/assets/icons/pl/nextjs.svg",
  },
  {
    id: 9,
    name: "HTML",
    category: "Frontend",
    imgUrl: "/assets/icons/pl/html.svg",
  },
  {
    id: 10,
    name: "CSS",
    category: "Frontend",
    imgUrl: "/assets/icons/pl/css.svg",
  },
  {
    id: 11,
    name: "Node.js",
    category: "Backend",
    imgUrl: "/assets/icons/pl/node.svg",
  },
  {
    id: 12,
    name: "Express.js",
    category: "Backend",
    imgUrl: "/assets/icons/pl/expressjs.svg",
  },
  {
    id: 13,
    name: "Python Flask",
    category: "Backend",
    imgUrl: "/assets/icons/pl/python-flask.svg",
  },
  {
    id: 14,
    name: "MongoDB",
    category: "Databases",
    imgUrl: "/assets/icons/pl/mongodb.svg",
  },
  {
    id: 15,
    name: "MySQL",
    category: "Databases",
    imgUrl: "/assets/icons/pl/mysql.svg",
  },
  {
    id: 16,
    name: "Scikit-learn",
    category: "Machine Learning",
    imgUrl: "/assets/icons/pl/scikitlearn.svg",
  },
  {
    id: 17,
    name: "Pandas",
    category: "Machine Learning",
    imgUrl: "/assets/icons/pl/pandas.svg",
  },
  {
    id: 18,
    name: "NumPy",
    category: "Machine Learning",
    imgUrl: "/assets/icons/pl/numpy.svg",
  },
  {
    id: 19,
    name: "Git",
    category: "Version Control",
    imgUrl: "/assets/icons/pl/git.svg",
  },
];

const Skills = () => {
  const paragraphStyle = {
    marginBottom: "2rem",
    fontSize: "1.5rem",
    fontWeight: "normal",
    textAlign: "center",
  };

  const categoriesStyle = {
    display: "flex",
    justifyContent: "center",
    flexWrap: "wrap",
    margin: "1rem 0",
  };

  const skills = {
    backgroundImage: "url('/assets/images/skill-bg.jpg')",
    backgroundSize: "cover",
  };
  const buttonStyle = {
    width: "150px",
    height: "150px",
    margin: "0.5rem",
    padding: "0.5rem 1rem",
    borderRadius: "1rem",
    border: "none",
    // backgroundColor: 'rgba(74, 45, 197, 0.1)',
    backgroundColor: "rgba(255, 255, 255, 0.5)",
    boxShadow:
      ".125rem .125rem .375rem 0 rgba(74, 45, 197, .04), .5rem .5625rem 1.625rem 0 rgba(74, 45, 197, .07), 1.375rem 1.5rem 5rem 0 rgba(74, 45, 197, .11)",
    backdropFilter: "blur(10px)",
    cursor: "pointer",
    transition: "background-color 0.3s ease",
  };

  const plLogo = {
    width: "80px",
    height: "80px",
    marginBottom: "0.5rem",
  };
  return (
    <Section>
      <Container>
        <div>
          <h1 className="heading-style" id="skills">
            Skills
          </h1>
          <p style={paragraphStyle}>
            My technical skills in various categories.
          </p>
          <div className="about-section" style={skills}>
            <div style={categoriesStyle}>
              {skillsData.map((skill) => (
                <button key={skill.name} style={buttonStyle}>
                  <img
                    src={skill.imgUrl}
                    style={plLogo}
                    alt={skill.name}
                    width="32"
                    height="32"
                  />
                  <br></br>
                  <b>{skill.name}</b>
                </button>
              ))}
            </div>
          </div>
        </div>
      </Container>
    </Section>
  );
};

export default Skills;
