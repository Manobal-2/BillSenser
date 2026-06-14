
"use client"

import { useState } from "react"
import axios from "axios"

export default function Home() {
  const [file, setFile] = useState<File | null>(null)
  const [response, setResponse] = useState("")

  const uploadBill = async () => {
    if (!file) return

    const formData = new FormData()
    formData.append("file", file)

    const res = await axios.post("http://127.0.0.1:8000/analyze", formData)
    setResponse(JSON.stringify(res.data, null, 2))
  }

  return (
    <main className="min-h-screen p-10">
      <h1 className="text-4xl font-bold mb-6">BillSense AI</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
        className="mb-4"
      />

      <button
        onClick={uploadBill}
        className="bg-black text-white px-6 py-3 rounded-lg"
      >
        Analyze Bill
      </button>

      <pre className="mt-8 whitespace-pre-wrap">{response}</pre>
    </main>
  )
}
