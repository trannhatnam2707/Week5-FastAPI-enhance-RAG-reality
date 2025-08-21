import './App.css';
import PostDetail from './Page/PostDetail';
import PostList from './Page/PostList';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<PostList />} />
        <Route path="/PostDetail/:id" element={<PostDetail />} />
      </Routes>
    </div>
  );
}

export default App;
