import React, {useState} from 'react';
import logo from './assets/img/githublink.png';
import button from './assets/img/header.gif';
import divider from './assets/img/anotherworld.jpe';
import divider2 from './assets/img/2ndImg.jpg';
import divider3 from './assets/img/3rdImg.jpg';
import divider4 from './assets/img/4thImg.jpg';
import ending from './assets/img/ending.gif';
import border from './assets/img/border.gif';
import end from './assets/img/pikachu-running.gif';
import goodbye from './assets/img/goodbye.gif';
import tab from './assets/img/logo.gif';
import './App.css';

function App() {
    {/*Button Definitions*/ }
    const [isCurryDetailsExpanded, setIsCurryDetailsExpanded] = useState(false);

    const toggleCurryDetails = () => {
        setIsCurryDetailsExpanded(!isCurryDetailsExpanded);
    };
    const [isRamenDetailsExpanded, setIsRamenDetailsExpanded] = useState(false);

    const toggleRamenDetails = () => {
        setIsRamenDetailsExpanded(!isRamenDetailsExpanded);
    };
    const [isHotpotDetailsExpanded, setIsHotpotDetailsExpanded] = useState(false);

    const toggleHotpotDetails = () => {
        setIsHotpotDetailsExpanded(!isHotpotDetailsExpanded);
    };
    const [isRdmDetailsExpanded, setIsRdmDetailsExpanded] = useState(false);

    const toggleRdmDetails = () => {
        setIsRdmDetailsExpanded(!isRdmDetailsExpanded);
    };

    return (
        <div className="App">
            <header className="App-header">
                <img src={button} className="App-logo" alt="logo" /> 
            </header>
            {/*Making a github button*/}
            <a href="https://github.com/khangwen/Platform-Computing-Project.git" target="_blank">
                <button className="Button1">
                    <img src={logo} className="GITHUB-LOGO" width="50" alt="GITHUB"></img>
                </button>
            </a>

            {/*<hr className="Line" />*/}

            {/*First Tester/Blog Entry*/ }
            <header className="First">
                <p style={{ color: 'black' }}>
                    <h1 style={{ color: 'bisque', fontWeight: 'bold', fontFamily:'Copperplate, Papyrus, fantasy' }}>
                    OuterWorld Delicacies
                </h1>
                    <hr />
                    Wanna taste something otherwordly? Something familar with a fantastical twist? Something you never tried before?
                    Or do you just enjoy the show you watch and want to replicate or make it better? Well, welcome to OuterWorld
                    Delicacies! Jump into different worlds, and expand your taste buds to make a boring night into some colorful memories!
                </p>
            </header>


            {/*Spruce it up*/}
            <img src={divider} className="Divider-Break" alt="break" />
            <img src={divider2} className="Divider-Break2" alt="break2" />
            <img src={divider3} className="Divider-Break3" alt="break3" />
            <img src={divider4} className="Divider-Break4" alt="break4" />
            <img src={ending} className="Ending-Gif" alt="ending" />
            <img src={end} className="Pika" alt="Pika Pika" />
            <img src={border} className="Border" alt="beg" />

            {/*Second Paragraph*/}
            <header className="Second">
                <p style={{ color: 'black' }}>
                    <h1 style={{ color: 'darkcyan', fontWeight: 'bold', fontFamily: 'Copperplate, Papyrus, fantasy' }}>
                        Curry From Another World
                    </h1>
                    <hr />
                    <h2 style={{ color:'brown', fontFamily: 'Malgun Gothic', fontWeight: 'bold' }}>Chicken Curry</h2>
                    Let's start easy! What is something that is easy to make and can be made towards your personal preference? Curry!
                    You can make curry with any type of protein if you want or simply with just vegetables as well! Today the main focus is
                    the Chicken Curry from Restaurant to Another World!
                </p>
                <hr />

                <h3>Ingredients:</h3>
                {/*Ingredient List*/}
                <button style={{ backgroundColor: 'olive', border: 'groove' }} onClick={toggleCurryDetails}>
                    {isCurryDetailsExpanded ? 'Hide Details' : 'Show Details'}
                </button>

                {/* Conditionally render the recipe details */}
                {isCurryDetailsExpanded && (
                    <div>
                        <p>
                            1lb boneless, skinless chicken breast <br />
                            1lb carrots<br />
                            1 White/Purple Onion<br />
                            1lb Yukon Gold Potatoes
                            2 Garlic Cloves<br />
                            1 tsp Ground Ginger<br />
                            1/4 cup Olive Oil<br />
                            1 tsp Ground Cumin<br />
                            1 tsp Ground Coriander<br />
                            1 tsp Ground Turmeric<br />
                            1 tsp Garlic Salt<br />
                            1 tbsp Soy <br />
                            1 tbsp <br />
                            1 tbsp Oyster <br />
                            6 Cups Water<br />
                        </p>
                    </div>
                )}
            </header>

            {/*Third Paragraph*/}
            <header className="Third">
                <p>
                    <h1 style={{ color: 'darkcyan', fontWeight: 'bold', fontFamily: 'Copperplate, Papyrus, fantasy' }}>
                        Max Passion!
                    </h1>
                    <hr />
                    <h2 style={{ color: 'brown', fontWeight: 'bold', fontFamily: 'Malgun Gothic' }}>African Ramen</h2>
                    Using peanuts to enchance the flavor of the chili peppers, rolled pork shoulder smothered in chashu glaze,
                    this ramen will satisfy every craving a hardy soup you've ever had!
                </p>
                <hr />
                <h3>Ingredients:</h3>

                <button style={{ backgroundColor: 'olive', border: 'groove' }} onClick={toggleRamenDetails}>
                    {isRamenDetailsExpanded ? 'Hide Details' : 'Show Details'}
                </button>

                {/* Conditionally render the recipe details */}
                {isRamenDetailsExpanded && (
                    <div>
                        <p>
                            Muamba Chicken Soup <br />
                            <hr />
                            Chicken Bone Stock <br />
                            Chicken Bones<br />
                            Garlic <br />
                            Red Peppers <br />
                            Onions <br />
                            Tomatoes <br />
                            Chicken Drumettes <br />
                            Peanut Butter <br />
                            <hr />
                            Chashu Topping <br />
                            <hr />
                            Chashu <br />
                            Rolled Pork Shoulder Roast <br />
                            Chashu Glaze <br />
                            Garlic <br />
                            Soy Sauce <br />
                            Sugar <br />
                            Wine <br />
                            Peanuts <br />
                            <hr />
                            Wide Style Ramen Noodles<br />
                        </p>
                    </div>
                )}
            </header>

            {/*Fourth Paragraph*/}
            <header className="Fourth">
                <p>
                    <h1 style={{ color: 'darkcyan', fontWeight: 'bold', fontFamily: 'Copperplate, Papyrus, fantasy' }}>
                        Huge Scorpion and Walking Mushroom Hotpot <br />
                    </h1>
                    <hr />
                    <h2 style={{ color: 'brown', fontFamily: 'Malgun Gothic', fontWeight: 'bold' }}>Crustation and Mushroom Hotpot <br /> </h2>
                    What's better than a big ol' pot huge scorpion and possibly sentient mushrooms? I can't think of much. This early adventurer friendly recipe does have some pre-prepared ingredients, but don't worry! They're not neccesary for a well rounded, nutricious meal!
                    <hr />
                </p>
                <h3>Ingredients:</h3>

                <button style={{ backgroundColor: 'olive', border: 'groove' }} onClick={toggleHotpotDetails}>
                    {isHotpotDetailsExpanded ? 'Hide Details' : 'Show Details'}
                </button>

                {/* Conditionally render the recipe details */}
                {isHotpotDetailsExpanded && (
                    <div>
                        <p>
                            1 Huge Scorpion <br />
                            1 Walking Mushroom <br />
                            2 Mushroom Feet <br />
                            Seaweed (as needed) <br />
                            5 Medium sized Invertatoes <br />
                            Dried Slime (To preference) <br />
                            Water (as needed) <br />
                        </p>
                    </div>
                )}
            </header>

            {/*Fifth Paragraph*/}
            <header className="Fifth">
                <p>
                    <h1 style={{ color: 'darkcyan', fontWeight: 'bold', fontFamily: 'Copperplate, Papyrus, fantasy' }}>
                        Red Dragon Meal <br />
                    </h1>
                    <hr />
                    <h2 style={{ color: 'brown', fontFamily: 'Malgun Gothic', fontWeight: 'bold' }}>Roast, Soup, Pizza <br/> </h2>
                    Have you ever killed a red dragon and thought to yourself, 'What am I gonna do with all this meat?' Well here's your answer! Enjoy a feast fit for even the maddest of mages including a nice Roast Red Dragon, Dragon Tail Soup, and Onion Pizza Bread
                    <hr />
                </p>
                <h3>Ingredients:</h3>

                <button style={{ backgroundColor: 'olive', border: 'groove' }} onClick={toggleRdmDetails}>
                    {isRdmDetailsExpanded ? 'Hide Details' : 'Show Details'}
                </button>

                {/* Conditionally render the recipe details */}
                {isRdmDetailsExpanded && (
                    <div>
                        <p>
                            Roast Red Dragon <br />
                            1 kilogram Red Dragon meat<br />
                            50 ml Wine <br />
                            Salt and Pepper (to taste)<br />
                            <hr />
                            Dragon Tail Soup <br />
                            1 kilogram Red Dragon Tail<br />
                            1 Onion<br />
                            5 Turnip<br />
                            Salt and Pepper (to taste)<br />
                            <hr />
                            Onion Pizza Bread <br />
                            Pizza Dough <br />
                            2 Onions<br />
                            Cheese (as desired)<br />
                        </p>
                    </div>
                )}
            </header>

            {/*Ending Space*/}
            <header className="Ending">
                <footer>
                Developed By
                    &copy;OWD
                </footer>
            </header>
                {/*making favorite song at the moment button link*/}
                <a href="https://youtu.be/9rVKos-oGnQ?si=Y6wTFRB0Z7kEkcZZ" target="_blank" alt="Fave song at the moment">
                    <button className="GoodbyeDivider">
                        <img src={goodbye} className="Music" width="65" alt="Totoro"></img>
                    </button>
                </a>
                {/*making a button link for the page in general*/}
            <a href="http://localhost:3000/" target="_blank" alt="Homepage">
                <button className="GoodbyeDivider2">
                        <img src={tab} className="Homepage" width="50" alt="Cute Doggo"></img>
                    </button>
                </a>
        </div>
        
    );
}
export default App;
