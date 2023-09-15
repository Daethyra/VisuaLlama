
// Function to handle form submission
async function handleFormSubmit(event: Event) {
    event.preventDefault();
  
    // Capture form elements
    const imageUpload = document.getElementById('imageUpload') as HTMLInputElement;
    const objectList = document.getElementById('objectList') as HTMLInputElement;
    const resultDiv = document.getElementById('result') as HTMLElement;
  
    // Prepare FormData
    const formData = new FormData();
    formData.append('image', imageUpload.files[0]);
    formData.append('objects', objectList.value);
  
    // Make API call to the backend
    try {
      const response = await fetch('http://localhost:5000/count_objects', {
        method: 'POST',
        body: formData
      });
      
      const data = await response.json();
  
      // Display the result
      resultDiv.innerHTML = data.message;
    } catch (error) {
      resultDiv.innerHTML = 'An error occurred. Please try again.';
    }
  }
  
  // Attach event listener to the form
  const uploadForm = document.getElementById('uploadForm') as HTMLFormElement;
  uploadForm.addEventListener('submit', handleFormSubmit);
  