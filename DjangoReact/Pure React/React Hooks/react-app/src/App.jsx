import { useState } from 'react'

import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [name, setname] = useState("")

  return (
    <>
    <h1>{count}{name}</h1>
    <button onClick={() => setCount(count + 1)}>
      Increase
    </button><br /><br />
    <button onClick={() => setCount(count - 1)}>
      Decrease
    </button>
    <input type="text" onChange={e => setname(e.target.value)}/>
    </>
  )
}

export default App
