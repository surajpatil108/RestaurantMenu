
  function openModal(id) {
    const modal = document.getElementById(id);
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal(id) {
    const modal = document.getElementById(id);
    modal.classList.remove('active');
    // Only re-enable scroll if no other modals are active
    if (!document.querySelector('.modal-overlay.active')) {
      document.body.style.overflow = 'auto';
    }
  }

  // Close on background click
  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', function (e) {
      if (e.target === this) {
        closeModal(this.id);
      }
    });
  });