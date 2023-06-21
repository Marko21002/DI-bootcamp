import React, { Component } from 'react';

class Color extends Component {
  constructor(props) {
    super(props);
    this.state = {
      favoriteColor: "pink"
    };
  }

  componentDidMount() {
    setTimeout(() => {
      this.setState({ favoriteColor: "yellow" });
    }, 5000);
  }

  changeColor = () => {
    this.setState({ favoriteColor: "blue" });
  }

  render() {
    return (
      <div>
        <h2>Favorite Color</h2>
        <h1>{this.state.favoriteColor}</h1>
        <button onClick={this.changeColor}>Change to Blue</button>
      </div>
    );
  }
}

export default Color;
