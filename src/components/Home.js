// import {AiOutlineLeft} from 'react-icons/ai';
// import {AiOutlineRight} from 'react-icons/ai';
import img1 from "../assets/lap1.jpg";
import img2 from "../assets/lap2.jpg";
import img3 from "../assets/lap3.jpg";
import img4 from "../assets/lap4.jpg";
import img5 from "../assets/lap5.jpg";
import ImageSlider from './ImageSlider';
const Home = () => {
    return (  
    <div className="home">
      <ImageSlider images={[img1,img2,img3,img4,img5]} >
      <div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              color: "#fff",
            }}
          >
            <h1>Welcome to Dell</h1>
          </div>
        </ImageSlider>
    </div>
    );
}
 
export default Home;