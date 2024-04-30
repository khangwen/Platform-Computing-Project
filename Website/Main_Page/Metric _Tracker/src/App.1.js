import React from 'react';
import logo from './githublink.png';
import button from './coraline.jpg';

export function App() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={button} className="App-logo" alt="logo" />
            </header>
            <a href="https://github.com/michilcutt/Platform_Computing.git" target="_blank">
                <button>
                    <img src={logo} className="GITHUB-LOGO" width="50" alt="GITHUB"></img>
                </button>
            </a>
        </div> /*Creating a github link button & changing react logo from before*/
    );
    function First() {
        return (
            <div className="First">
                <p>
                    <header>
                        Nonstop grind? Coffee coded? Me too!
                    </header>
                    <hr />
                    Afro Code is like a DNA Sequence from Jurassic Park, always changing and editing
                    lines of code throughout the different evolutions of themselves. Transferring from a community college
                    to a university was a step that was new, intriguing but frightening. Few things of comfort came through the
                    hard journey: coffee(put emoji here), animals(put emoji here), and new surroundings. Along with
                    these new surroundings, new interests came as well.
                </p>
            </div>

        );
        /*putting images here to make aesthetic breaks in between paragraphs*/
        /*note: width and height cannot be changed
 in css when width here has a value*/
    }
    function Second() {
        return (
            <div className="Second">
                <p>
                    <header>
                        <h1 style={{ fontFamily: 'Chiller' }}>Photography</h1>
                    </header>
                    <hr />
                    While Photography, isn't necessarly a new interest I've had it only became stronger when I took an actual class
                    here. I always only took photos on my phone and before I started Uni here I was given an old video camera by my pops.
                    It took off from there but once I started taking a class and realized the beauty and bigger picture(ha!) of it all,
                    it was like rediscovering your favorite song from when you were in high school. It's refreshing and suddenly everything is
                    reignited again. Reminds me of my everygrowing passion and fear of my field.
                </p>
            </div>
        );
    }
}
