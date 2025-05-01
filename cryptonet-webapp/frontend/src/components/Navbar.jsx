import { Link } from 'react-router-dom'

export default function Navbar() {
  return (
    <nav className="p-4 bg-gray-100">
      <Link to="/">Files</Link> |
      <Link to="/crypto">Crypto</Link> |
      <Link to="/login">Login</Link>
    </nav>
  )
}
