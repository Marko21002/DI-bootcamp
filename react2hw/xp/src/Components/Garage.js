import React from 'react';

class Garage extends React.Component {
  render() {
    const { size } = this.props;

    return (
      <div>
        <h2>Who lives in my {size} Garage?</h2>
        
      </div>
    );
  }
}

export default Garage;