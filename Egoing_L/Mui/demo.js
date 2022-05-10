import './App.css';
import React, { useState } from 'react';
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import { StyledEngineProvider } from '@mui/material/styles';

import NavTabss from './components/graph/NavTabs';
import ResponsiveDrawer from './components/graph/ResposiveDrawer';

function Header(props) {
  return <header>
    <h1><a href="/" onClick={function (event) {
      event.preventDefault();
      props.onChangeMode();
    }}>{props.title}</a></h1>
  </header>

}


function SideTabs(props) {
  const lis = []
  for (let i=0; i<props.topics.length; i++){
    let t = props.topics[i];
    lis.push(<li key={t.id}>
      <a id={t.id} href={"/read/" + t.id} onClick={event => {
        event.preventDefault();
        props.onChangeMode(Number(event.target.id));
      }}>{t.title}</a>
    </li>)
  }
  return <nav>
    <ol>
      {lis}
    </ol>
  </nav>
}

function Article(props) {
  return <article>
    <h2>{props.title }</h2>
    {props.body}
    
    <br />
    <br />
    
    <ButtonGroup>
      <Button variant='contained'>create</Button>
      <Button variant='contained'>Update</Button>
    </ButtonGroup>
    <Button variant='contained'>delete</Button>
  </article>
  
}

function App() {
  const [mode, setMode] = useState('WELCOME');
  const [id, setId] = useState(null);
  const topics = [
    { id: 1, title: 'Top10', body: 'Top10 is ...' },
    { id: 2, title: 'Pie chart', body: 'Pie chart is ...' },
    { id: 3, title: 'Bar chart', body: 'Bar chart is ...' }
  ]
  let content = null;
  if (mode === 'WELCOME') {
    content = <Article title="Welcome" body = "Hello, WEB"></Article>

  } else if (mode === 'READ') {
    let title, body = null;
    for (let i = 0; i < topics.length; i++){
      if (topics[i].id === id) {
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content = <Article title={title} body = {body}></Article>
  }
  return (
    <Container fixed>
      <Grid container>
        <Grid item xs={7}>
          <Header title="Nutrients" onChangeMode={() => {
            setMode('WELCOME');
          }}></Header>
        </Grid>
        <Grid item xs={5}>
          <NavTabss></NavTabss>
        </Grid>
      </Grid>
      <Grid container>
        <Grid item xs={2}>
          <SideTabs topics={topics} onChangeMode={(_id) => {
            setMode('READ');
            setId(_id);
          }}></SideTabs>
        </Grid>
        <Grid item xs={10}>{content}</Grid>
      </Grid>
      
    </Container>
  );
}

export default App;
