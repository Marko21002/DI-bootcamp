import React from 'react';
import Garage from './Garage';

class Car extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      color: "blue" // Default color, you can change it to your desired initial color
    };
  }

  render() {
    const { carInfo } = this.props;
    const { color } = this.state;

    return (
      <div>
        <h1>This car is {color} {carInfo.name} {carInfo.model}</h1>
        <Garage size="small" />
      </div>
    );
  }
}

export default Car;
