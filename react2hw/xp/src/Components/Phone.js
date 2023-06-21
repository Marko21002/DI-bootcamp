import React from 'react';

class Phone extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      brand: "Samsung",
      model: "Galaxy S20",
      color: "black",
      year: 2020
    };
  }

  changeColor = () => {
    this.setState({
      color: "blue"
    });
  }

  render() {
    return (
      <div>
        <h2>Phone Information</h2>
        <p>Brand: {this.state.brand}</p>
        <p>Model: {this.state.model}</p>
        <p>Color: {this.state.color}</p>
        <p>Year: {this.state.year}</p>
        <button onClick={this.changeColor}>changeColor</button>
      </div>
    );
  }
}

export default Phone;
