import React, { Component } from 'react';

class EventONOF extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isToggleOn: true
    };
  }

  handleClick = () => {
    this.setState(prevState => ({
      isToggleOn: !prevState.isToggleOn
    }));
  }

  getOutput = () => {
    return this.state.isToggleOn ? 'ON' : 'OFF';
  }

  render() {
    return (
      <div>
        <button onClick={this.handleClick}>
          {this.getOutput()}
        </button>
      </div>
    );
  }
}

export default EventONOF;
