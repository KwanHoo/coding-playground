import './App.css';
import React, { useState } from 'react';
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';


function Header(props) {
  return <header>
    <h1><a href="/" onClick={function (event) {
      event.preventDefault();
      props.onChangeMode();
    }}>{props.title}</a></h1>
    </header>
}

function Nav(props) {
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
    { id: 1, title: 'html', body: 'html is ...' },
    { id: 2, title: 'css', body: 'css is ...' },
    { id: 3, title: 'javascript', body: 'javascript is ...' }
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
      <Header title="WEB" onChangeMode={() => {
        setMode('WELCOME');
      }}></Header>
      <Header title="REACT!!" onChangeMode={function () { alert('header'); }}></Header>
      <Header title="JavaScript??" onChangeMode={() => { alert('JAVA??'); }}></Header>
      <Grid container>
        <Grid item xs={2}>
          <Nav topics={topics} onChangeMode={(_id) => {
            setMode('READ');
            setId(_id);
          }}></Nav>
        </Grid>
        <Grid item xs={10}>{content}</Grid>
      </Grid>
    </Container>
  );
}

export default App;
