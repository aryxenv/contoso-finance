import { NavLink } from 'react-router-dom'

const navItems = [
  { to: '/', label: 'Dashboard' },
  { to: '/billing', label: 'Billing' },
  { to: '/payments', label: 'Payments' },
  { to: '/reporting', label: 'Reporting' },
  { to: '/settlements', label: 'Settlements' },
]

export function Sidebar() {
  return (
    <nav className="app-sidebar">
      <ul>
        {navItems.map((item) => (
          <li key={item.to}>
            <NavLink
              to={item.to}
              end={item.to === '/'}
              className={({ isActive }) => (isActive ? 'active' : '')}
            >
              {item.label}
            </NavLink>
          </li>
        ))}
      </ul>
    </nav>
  )
}
