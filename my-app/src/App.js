import React from 'react';
import logo from './assets/img/githublink.png';
import button from './assets/img/coraline.jpg';
import divider from './assets/img/divider.gif';
import end from './assets/img/pikachu-running.gif';
import goodbye from './assets/img/goodbye.gif';
import tab from './assets/img/logo.gif';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={button} className="App-logo" alt="logo" />
      </header>
      {/*Making a github button*/}
      <a href="https://github.com/michilcutt/Platform_Computing.git" target="_blank">
        <button className="Button1">
          <img src={logo} className="GITHUB-LOGO" width="50" alt="GITHUB"></img>
        </button>
      </a>

      {/*First Paragraph*/}
      <header className="First">
        <p style={{ color: 'black' }}>
          <header style={{ color: 'darkcyan', fontWeight: 'bold', fontFamily: 'Franklin Gothic Medium' }}>
            Nonstop grind? Coffee coded? Me too!
          </header>
          <hr />
          Afro Code is like a DNA Sequence from Jurassic Park, always changing and editing
          lines of code throughout the different evolutions of themselves. Transferring from a community college
          to a university was a step that was new, intriguing but frightening. Few things of comfort came through the
          hard journey: coffee(put emoji here), animals(put emoji here), and new surroundings. Along with
          these new surroundings, new interests came as well.
        </p>
      </header>
      {/*Spruce it up*/}
      <img src={divider} className="Divider-Break" alt="break" />
      <img src={end} className="Pika" alt="Pika Pika" />

      {/*Second Paragraph*/}
      <header className="Second">
        <p style={{ color: 'black' }}>
          <header style={{ color: 'darkcyan', fontWeight: 'bold', fontFamily: 'Franklin Gothic Medium' }}>
            Rediscovered Hobbies!
          </header>
          <hr />
          <h2 style={{ color: 'mediumvioletred', fontFamily: 'Chiller', fontWeight: 'bold' }}>Photography</h2>
          While Photography, isn't necessarly a new interest I've had it only became stronger when I took an actual class
          here. I always only took photos on my phone and before I started Uni here I was given an old video camera by my pops.
          It took off from there but once I started taking a class and realized the beauty and bigger picture(ha!) of it all,
          it was like rediscovering your favorite song from when you were in high school. It's refreshing and suddenly everything is
          reignited again. Reminds me of my everygrowing passion and fear of my field.
        </p>
      </header>

      {/*Third Paragraph*/}
      <header className="Third">
        <p>
          <header style={{ color: 'darkcyan', fontWeight: 'bold', fontFamily: 'Franklin Gothic Medium' }}>
            Max Passion!
          </header>
          <hr />
          <h2 style={{ color: 'palegoldenrod', fontWeight: 'bold', fontFamily: 'Chiller' }}>My Major</h2>
          My major is in Computer Systems: Game Development Concentration. I want to make video games and I've always wanted to make
          games since I could remember playing my first game on V.SMILE a game console for kids and while it was for educational purposes
          I still fell inlove with the comfort and excitement of playing a video game. It is not my end goal to make video games, AstroPhysicist,
          it's still a passion I adore and fear at the same time. I am always scared that I'll lose my admiration and determination to make
          games because of the complexity and difficulty of that world in general. But that fear is still driving me to finish this degree
          and continue my dreams.
        </p>
      </header>

      {/*Ending Space*/}
      <header className="Ending">
        <footer>
          &copy;MKC
        </footer>
        {/*making favorite song at the moment button link*/}
        <a href="https://youtu.be/uTMuqL0qx08?si=BnEA0GLLQZW7gW6V" target="_blank" alt="Fave song at the moment">
          <button className="Button2">
            <img src={goodbye} className="GoodbyeDivider" width="50" alt="Totoro"></img>
          </button>
        </a>
        {/*making a button link for the page in general*/}
        <a href="http://localhost:3000/" target="_blank" alt="Homepage">
          <button className="Button3">
            <img src={tab} className="GoodbyeDivider2" width="50" alt="Cute Doggo"></img>
          </button>
        </a>
      </header>
    </div>

  );
}
export default App;