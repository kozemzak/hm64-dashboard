import React, { Component } from 'react';

class Home extends Component {
  
  constructor() {
    super();
    this.state = {}
    this.fetchGameState = this.fetchGameState.bind(this)
    this.updateData = this.updateData.bind(this)
  }

  componentDidMount() {
    var poll = setInterval(this.updateData, 100);
    this.setState({poll});
  }

  componentWillUnmount() {
    clearInterval(this.state.poll);
  }

  fetchGameState(category) {
    fetch('http://127.0.0.1/' + category)
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          console.log(response);
          throw new Error('Failed request to ' + category);
        }
      })
      .then(data => this.setState(data));
  }

  updateData() {
    fetchGameState('time')
  }

  /*
  updateData() {
    fetch('http://127.0.0.1:3000/time')
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          console.log(response);
          throw new Error('Something went wrong ...');
        }
      })
      .then(data => this.setState(data));
  }
  */
  render() {
    return (
      <div className="Home">
        <div>Year {this.state.time_year}</div>
        <div>{this.state.time_season} {this.state.time_day_number}</div>
        <div>{this.state.time_weekday}</div>
        <div>{this.state.time_hours}:{this.state.time_minutes}</div>
      </div>
    );
  }
}

export default Home;
