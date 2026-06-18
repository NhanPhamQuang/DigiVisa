let selectedRegion = 'all';

function toggleMenu() {
  const nav = document.getElementById('navLinks');
  nav.classList.toggle('show');
}

function setRegion(region) {
  selectedRegion = region;
  filterCountries();
}

function filterCountries() {
  const input = document.getElementById('countrySearch');
  const query = input ? input.value.toLowerCase() : '';
  const cards = document.querySelectorAll('.filter-card');

  cards.forEach(card => {
    const name = card.dataset.name || '';
    const region = card.dataset.region || '';
    const matchName = name.includes(query);
    const matchRegion = selectedRegion === 'all' || region === selectedRegion;
    card.style.display = matchName && matchRegion ? 'block' : 'none';
  });
}

function updateContactInput() {
  const tags = Array.from(document.querySelectorAll('#contactTags .contact-tag'));
  const input = document.getElementById('contactByInput');
  if (!input) return;
  input.value = tags.map(tag => tag.dataset.value).join(',');
}

function addContactTag() {
  const select = document.getElementById('contactSelect');
  const container = document.getElementById('contactTags');
  if (!select || !container || !select.value) return;

  const value = select.value;
  const exists = Array.from(container.querySelectorAll('.contact-tag'))
    .some(tag => tag.dataset.value === value);

  if (!exists) {
    const tag = document.createElement('span');
    tag.className = 'contact-tag';
    tag.dataset.value = value;
    tag.innerHTML = `${value} <button type="button" onclick="removeContactTag(this)">×</button>`;
    container.appendChild(tag);
    updateContactInput();
  }

  select.value = '';
}

function removeContactTag(button) {
  const tag = button.closest('.contact-tag');
  if (tag) tag.remove();
  updateContactInput();
}
