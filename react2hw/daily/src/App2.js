import React, { Component } from 'react';
import './App2.css'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      languages: [
        { name: "Php", votes: 0 },
        { name: "Python", votes: 0 },
        { name: "JavaScript", votes: 0 },
        { name: "Java", votes: 0 }
      ]
    };
  }

  handleVote = (index) => {
    const updatedLanguages = [...this.state.languages];
    updatedLanguages[index].votes += 1;

    this.setState({
      languages: updatedLanguages
    });
  }

  render() {
    const { languages } = this.state;

    return (
      <div>
        <h2>Languages Vote</h2>
        {languages.map((language, index) => (
          <div key={index} className='vote'>
            <span>{language.name}: {language.votes}</span>
            <button onClick={() => this.handleVote(index)}>Vote</button>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
