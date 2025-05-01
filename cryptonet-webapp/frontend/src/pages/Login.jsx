import { useState } from 'react'
import api from '../api/api'
import { useNavigate } from 'react-router-dom'

export default function Login() {
  const [u, setU] = useState('')
  const [p, setP] = useState('')
  const nav = useNavigate()
  const submit = async e => {
    e.preventDefault()
    const { data } = await api.post('/auth/login', { username: u, password: p })
    localStorage.setItem('token', data.access_token)
    nav('/')
  }
  return (
    <form onSubmit={submit} className="p-4">
      <input value={u} onChange={e=>setU(e.target.value)} placeholder="Username" />
      <input type="password" value={p} onChange={e=>setP(e.target.value)} placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  )
}
