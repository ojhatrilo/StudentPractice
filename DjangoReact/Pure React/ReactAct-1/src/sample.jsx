
const App = () => {
    const x = 10
    const y = 20
    const names = ['Abhi','John','Jane','Kirthi']
    return (
      <>
      <div className='text-5xl'>
        App
      </div>
      <p>The total of {x} and {y}={x+y}</p>
      <ul>
        {names.map((crane,index)=>(
          <li key={index}>{crane}</li>
        ))}  
      </ul>
      </>
    ); 
  };
  
  export default App;
  