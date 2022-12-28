// Get search forma and page links
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

// Ensure search for exists
if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener('click', function (e) {
      e.preventDefault()

      // Get the data attribute
      let page = this.dataset.page

      // Add hidden search input to form
      searchForm.innerHTML += `<input value=${page} name="page" hidden />`

      // Submit form
      searchForm.submit()
    })
  }
}

let tags = document.getElementsByClassName('project-tag')
for (let i = 0; tags.length > i; i++) {
  tags[i].addEventListener('click', (e) => {
    let tagId = e.target.dataset.tag
    let projectId = e.target.dataset.project
    // console.log('TAG ID:', tagId, 'PROJECT ID:', projectId)

    fetch('http://127.0.0.1:8000/api/remove-tag/', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ project: projectId, tag: tagId }),
    })
      .then((response) => response.json())
      .then((data) => {
        e.target.remove()
      })
  })
}
