import React from 'react';

class Events extends React.Component {
  clickMe = () => {
    alert('I was clicked');
  };
  handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      const inputValue = event.target.value;
      alert(`You pressed Enter key! Input value: ${inputValue}`);
    }
  };
  

  render() {
    return (
      <div>
        <button onClick={this.clickMe}>Click Me</button>
        <input type="text" onKeyDown={this.handleKeyDown} />
      </div>
    );
  }
}

export default Events;