// import logo from './logo.svg';
import './App.css';
import ItemList from'./components/itemList'

function App() {
  return (
    <>
      <div className="serach-filter">
        <p className="hit-count"><strong>'워치4 골드 케이스'</strong>에 대한 검색결과</p>
      </div> 
      <div>
        <header id="intro">
          <nav>
            <ul>
              <li id="rank"><a href="#">쿠팡 랭킹순</a></li>
              <li><a href="#">낮은가격순</a></li>
              <li><a href="#">높은가격순</a></li>
              <li><a href="#">판매량순</a></li>
              <li><a href="#">최신순</a></li>
            </ul>
          </nav>
        </header>
      </div>
      <div className="clear"></div>
      <div></div>
      <ul id="product-list">

        <ItemList name="case1.png"></ItemList>
        <ItemList name="case2.png"></ItemList>
        <ItemList name="case3.png"></ItemList>
        <ItemList name="case4.png"></ItemList>

        
        <div className="clear"></div>
        <div className="line"></div>

        <ItemList name="case5.png"></ItemList>
        <ItemList name="case6.png"></ItemList>
        <ItemList name="case7.png"></ItemList>
        <ItemList name="case8.png"></ItemList>
        <div className="clear"></div>
        <div className="line"></div>
      </ul>
    </>

  );
}

export default App;
