"use client"

import { useState } from "react"
import axios from "axios"

export default function Home() {
  const [file, setFile] = useState(null)
  const [result, setResult] = useState(null)

  const uploadBill = async () => {
    const formData = new FormData()
    formData.append("file", file)

    const response = await axios.post(
      "http://localhost:8000/explain",
      formData
    )

    setResult(response.data)
  }

  return (
    <div style={{ padding: 40 }}>
      <h1>BillSenser</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={uploadBill}>
        Analyze Bill
      </button>

      {result && (
        <div>
          <h2>AI Explanation</h2>
          <p>{result.explanation}</p>

          <h2>Forecast</h2>
          <p>₹{result.forecast}</p>

          <h2>Savings</h2>
          <p>{result.savings}</p>
        </div>
      )}
    </div>
  )
}