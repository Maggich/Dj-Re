import { useEffect, useState } from "react";

type Product = {
  id: number;
  title: string;
  description: string;
  price: number;
  image: string;
};

function Main() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadProducts() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/products/");

        if (!response.ok) {
          throw new Error("Не удалось загрузить данные");
        }

        const data: Product[] = await response.json();
        setProducts(data);
        console.log(data);
      } catch (err) {
        const message =
          err instanceof Error ? err.message : "Неизвестная ошибка";
        setError(message);
      } finally {
        setLoading(false);
      }
    }

    loadProducts();
  }, []);

  if (loading) {
    return <p>Идет загрузка...</p>;
  }

  if (error) {
    return <p>Ошибка: {error}</p>;
  }

  return (
    <div>
      <h1>Список товаров</h1>

      {products.length === 0 ? (
        <p>Товаров пока нет</p>
      ) : (
        <ul>
          {products.map((product) => (
            <li key={product.id}>
              <h3>{product.title}</h3>
              <p>{product.description}</p>
              <p>Цена: {product.price}</p>

              {product.image ? (
                <img
                  src={`http://127.0.0.1:8000${product.image}`}
                  alt={product.title}
                  width={150}
                />
              ) : (
                <p>Нет изображения</p>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Main;