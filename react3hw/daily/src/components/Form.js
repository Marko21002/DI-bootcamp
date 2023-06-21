// import React, { useState } from 'react';

// function App() {
//   const [formData, setFormData] = useState({
//     firstName: '',
//     lastName: '',
//     age: '',
//     gender: '',
//     destination: '',
//     lactoseFree: false,
//   });

//   const handleChange = (event) => {
//     const { name, value, type, checked } = event.target;
//     const fieldValue = type === 'checkbox' ? checked : value;

//     setFormData((prevData) => ({
//       ...prevData,
//       [name]: fieldValue,
//     }));
//   };

//   const handleSubmit = (event) => {
//     event.preventDefault();
//     const { firstName, lastName, age, gender, destination, lactoseFree } = formData;
//     const queryString = `?firstName=${firstName}&lastName=${lastName}&age=${age}&gender=${gender}&destination=${destination}&lactoseFree=${lactoseFree ? 'on' : 'off'}`;
//     const url = `${window.location.origin}/${queryString}`;
//     window.location.href = url;
//   };

//   return (
//     <div>
//       <form onSubmit={handleSubmit}>
//         <label>
//           First Name:
//           <input
//             type="text"
//             name="firstName"
//             value={formData.firstName}
//             onChange={handleChange}
//           />
//         </label>
//         <br />
//         <label>
//           Last Name:
//           <input
//             type="text"
//             name="lastName"
//             value={formData.lastName}
//             onChange={handleChange}
//           />
//         </label>
//         <br />
//         <label>
//           Age:
//           <input
//             type="number"
//             name="age"
//             value={formData.age}
//             onChange={handleChange}
//           />
//         </label>
//         <br />
//         <label>
//           Gender:
//           <select name="gender" value={formData.gender} onChange={handleChange}>
//             <option value="">Select</option>
//             <option value="male">Male</option>
//             <option value="female">Female</option>
//             <option value="other">Other</option>
//           </select>
//         </label>
//         <br />
//         <label>
//           Destination:
//           <input
//             type="text"
//             name="destination"
//             value={formData.destination}
//             onChange={handleChange}
//           />
//         </label>
//         <br />
//         <label>
//           Lactose Free:
//           <input
//             type="checkbox"
//             name="lactoseFree"
//             checked={formData.lactoseFree}
//             onChange={handleChange}
//           />
//         </label>
//         <br />
//         <button type="submit">Submit</button>
//       </form>
//     </div>
//   );
// }

// export default App;
