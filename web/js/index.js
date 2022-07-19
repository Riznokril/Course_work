const cardsContainer = document.getElementById("cards_container");

const BASE_URL = "http://127.0.0.1:5000";
const RESOURSE_URL = `${BASE_URL}/`;

const cardTemplate = ({ id, open_close, time, user_id}) => `
<li id="${id}" class="card">
  <div>
    <p>Id: ${id} Open_close: ${open_close} Time: ${time} User_id ${user_id}</p>
  </div>
</li>`;

const addCardToPage = ({ Id: id, open_close, exit, time, user_id}) => {
    cardsContainer.insertAdjacentHTML(
      "beforeend",
      cardTemplate({ id, open_close, exit, time, user_id})
    );
};

const baseRequest = async ({ urlPath = "", method = "GET", body = null }) => {
    try {
      const reqParams = {
        method,
        headers: {
          "Content-Type": "application/json",
        },
      };
  
      if (body) {
        reqParams.body = JSON.stringify(body);
      }
  
      return await fetch(`${RESOURSE_URL}${urlPath}`, reqParams);
    } catch (error) {
      console.error("HTTP ERROR: ", error);
    }
  };
  
  export const getAllData = async () => {
    const rawResponse = await baseRequest({ method: "GET" });
  
    return await rawResponse.json();
  };

  const renderCardsList = (cards) => {
    cardsContainer.innerHTML = "";
    for (const card of cards) {
      addCardToPage(card);
    }
}; 

const data = await getAllData();
console.log(data)

renderCardsList(data);

