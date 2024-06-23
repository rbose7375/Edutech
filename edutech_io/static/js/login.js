const triggerPillList = document.querySelectorAll('.nav-item a')

triggerPillList.forEach((triggerEl) => {
  const pillTrigger = new Tab(triggerEl)

  triggerEl.addEventListener('click', (e) => {
    e.preventDefault()
    pillTrigger.show()
  })
})

const triggerEl = document.querySelector('#myTab a[href="#profile"]')
Tab.getInstance(triggerEl).show() // Select tab by name

const triggerFirstPillEl = document.querySelector('#myTab li:first-child a')
Tab.getInstance(triggerFirstPillEl).show() // Select first tab