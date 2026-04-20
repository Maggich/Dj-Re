import { useState, useEffect, type FormEvent } from 'react'

type Product = {
  id: number
  title: string
  price: number
}

function App() {

  const [products, setProducts] = useState<Product[]>([])
  const [title, setTitle] = useState("")
  const [price, setPrice] = useState("")

  async function loadProduct() {
    const response = await fetch("http://127.0.0.1:8000/api/products/")
    const data = await response.json()
    setProducts(data)
  }

  async function hendlerSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()

    const response = await fetch("http://127.0.0.1:8000/api/products/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: title,
        price: Number(price),
      }),
    })

    if (response.ok){
      setTitle("")
      setPrice("")
      loadProduct()
    } else {
      console.log("Ошибка при сохранении")
    }
  }

  useEffect(() => {
    loadProduct()
  }, [])

  return (
    <div style={{ padding: "20px" }}>
      <h1>Товары</h1>

      <form onSubmit={hendlerSubmit}>
        <input
          type="text"
          placeholder="Название"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <input
          type="number"
          placeholder="Цена"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />

        <button type="submit">Сохранить</button>
      </form>

      <hr />

      {products.map((product) => (
        <div key={product.id}>
          <h3>{product.title}</h3>
          <p>{product.price} тг</p>
        </div>
      ))}
    </div>
  )
}

export default App