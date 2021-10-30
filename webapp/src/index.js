import React from 'react'
import ReactDOM from 'react-dom'
import App from './routes/App'

ReactDOM.render(<App />, document.getElementById('app'))

window.addEventListener('DOMContentLoaded', event => {
  const sidebarToggle = document.body.querySelector('#sidebarToggle')
  if (sidebarToggle) {
    sidebarToggle.addEventListener('click', event => {
      event.preventDefault()
      document.body.classList.toggle('sb-sidenav-toggled')
      localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'))
    })
  }
})
